# Open Carbon Nanotubes for the Martini Model

Generates a Martini model for an open carbon nanotube (CNT) for use with the Gromacs simulation package.
It provides a structure file (.gro), a topology-include file (.itp) and a position-restraints file (.itp).

Tools to analyze Martini CNT simulations can be found here: https://github.com/bio-phys/cnt-martini-analysis. 

## Requirements

Python (2/3) with packages argparse, math, and sys

## Usage

For a new nanotube model, run 

    python martini-cnt-generator.py -nr [number of rings] \
                                    -rs [number of beads per ring] \
                                    -bl [bond length] \
                                    -bf [bond force const.] \
                                    -af [angle force const.] \
                                    -bt [bead type] \
                                    -ft [bead type of the functional groups] \
                                    -fb [number of functionalized rings at one end] \
                                    -fe [number of functionalized rings at the other end] \
                                    --base36

for example

    python martini-cnt-generator.py -nr 12 -rs 8 -bl 0.47 -bt CNP -ft SNda -fb 1 -fe 1

All arguments are optional. If an argument is not used, the default value for the standard CNT porin [1] is used.

## Notes

* By default, atom names are a letter denoting their function (C - plain carbon grid, F - funcional group) plus the last three digits of their atom number (decimal system). The flag `--base36` switches to a base of 36 (including letters) to expand the number of unique atom names from 10^3 = 1000 (decimal) to 36^3 = 46656.
* For large CNTs, a higher force constant than the standard value of 5000 should be used. A rule of thumb is to use a value of 20000 if the circumference exceeds 10 beads/ring or the length exceeds 15 rings. 
* The script produces position restraints, too. These are usually inteded for equilibration. They will not work with a Parrinello-Rahman barostat. 

## Literature

If the script or the model is helpful, please cite:
- [1]  M. Vögele, J. Köfinger, G. Hummer: 
    Simulations of Carbon Nanotube Porins in Lipid Bilayers.
    Faraday Discuss., 2018, 209, 341-358, DOI: 10.1039/C8FD00011E  
    http://pubs.rsc.org/en/content/articlelanding/2018/fd/c8fd00011e

The model is based on previous work:
- [2] R. M. Bhaskara, S. M. Linker, M. Vögele, J. Köfinger, G. Hummer 
    Carbon Nanotubes Mediate Fusion of Lipid Vesicles.
    ACS Nano, 2017, 11 (2), pp 1273–1280
- [3] M. Vögele, G. Hummer:
    Divergent Diffusion Coefficients in Simulations of Fluids and Lipid Membranes.
    J. Phys. Chem. B, 2016, 120 (33), pp 8722–8732
    DOI: 10.1021/acs.jpcb.6b05102
- [4] S. Baoukina, L. Monticelli, D.P. Tieleman:
    Interaction of Pristine and Functionalized Carbon Nanotubes with Lipid Membranes. 
    J. Phys. Chem. B (2013), 117, 12113-23.
- [5] L. Monticelli
    On atomistic and coarse-grained models for C60 fullerene. 
    J. Chem. Theory Comput. (2012), 8, 1370−1378 (DOI: 10.1021/ct3000102). 


