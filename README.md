# Open Carbon Nanotubes for the Martini Model

Generates a Martini model for an open carbon nanotube (CNT) for use with the Gromacs simulation package.
It provides a structure file (.gro), a topology-include file (.itp) and a position-restraints file (.itp).

Tools to analyze Martini CNT simulations can be found here: https://github.com/bio-phys/cnt-martini-analysis. 

# Requirements

Python (2/3) with packages argparse, math, and sys

# Usage

For a new nanotube model, run 

    python martini-cnt-generator.py -nr [number of rings] -rs [number of beads per ring] -bl [bond length] -bt [bead type] -ft [bead type of the functional groups] -nb [number of functionalized rings at one end] -ne [number of functionalized rings at the other end]

for example

    python martini-cnt-generator.py -nr 12 -rs 8 -bl 0.47 -bt CNP -ft SNda -nb 1 -ne 1

All arguments are optional. If an argument is not used, the default value for the standard CNT porin [1] is used.

# Literature

If the script or the model is helpful, please cite:
- [1]  M. Vögele, J. Köfinger, G. Hummer: 
    Simulations of Carbon Nanotube Porins in Lipid Bilayers.
    Faraday Discuss., 2018, Accepted Manuscript, DOI: 10.1039/C8FD00011E  
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


