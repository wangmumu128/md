#!/usr/bin/env python3
"""Generate a minimal multi-stage LAMMPS input deck."""

from __future__ import annotations

import argparse
from pathlib import Path


def write(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate baseline LAMMPS input files.")
    parser.add_argument("--system", default="md-system", help="Human-readable system name.")
    parser.add_argument("--units", default="real", choices=["real", "metal", "lj"], help="LAMMPS units.")
    parser.add_argument("--atom-style", default="full", help="LAMMPS atom_style.")
    parser.add_argument("--data", default="data.lammps", help="LAMMPS data file name.")
    parser.add_argument("--output", default=".", help="Output directory.")
    args = parser.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    common = f"""
# Generated baseline for {args.system}
units           {args.units}
atom_style      {args.atom_style}
boundary        p p p

read_data       {args.data}

# TODO: Replace these placeholder force-field styles/coefs with validated parameters.
pair_style      lj/cut/coul/long 10.0
bond_style      harmonic
angle_style     harmonic
dihedral_style  opls
improper_style  cvff
kspace_style    pppm 1.0e-4

neighbor        2.0 bin
neigh_modify    delay 0 every 1 check yes
"""

    write(
        out / "in.minimize",
        common
        + """
thermo          100
thermo_style    custom step temp pe etotal press vol density

min_style       cg
minimize        1.0e-4 1.0e-6 10000 100000

write_data      minimized.data
write_restart   minimized.restart
""",
    )

    write(
        out / "in.equilibration",
        common.replace(f"read_data       {args.data}", "read_data       minimized.data")
        + """
timestep        1.0
thermo          1000
thermo_style    custom step temp pe ke etotal press vol density

velocity        all create 300.0 4928459 mom yes rot yes dist gaussian

fix             nvt_eq all nvt temp 300.0 300.0 100.0
run             100000
unfix           nvt_eq

fix             npt_eq all npt temp 300.0 300.0 100.0 iso 1.0 1.0 1000.0
run             200000
unfix           npt_eq

write_data      equilibrated.data
write_restart   equilibrated.restart
""",
    )

    write(
        out / "in.production",
        common.replace(f"read_data       {args.data}", "read_data       equilibrated.data")
        + """
timestep        1.0
thermo          1000
thermo_style    custom step temp pe ke etotal press vol density

dump            traj all custom 1000 traj.lammpstrj id type mol x y z ix iy iz
dump_modify     traj sort id

fix             prod all nvt temp 300.0 300.0 100.0
run             1000000
unfix           prod

write_restart   production.restart
""",
    )

    write(
        out / "submit.slurm",
        f"""
#!/bin/bash
#SBATCH --job-name={args.system}
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --time=24:00:00
#SBATCH --output=lammps-%j.out

module load lammps
lmp -in in.minimize
lmp -in in.equilibration
lmp -in in.production
""",
    )

    print(f"Wrote LAMMPS template files to {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
