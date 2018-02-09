# Open Carbon Nanotubes for the Martini Model

Generates a Martini model for an open carbon nanotube (CNT) for use with the Gromacs simulation package.
It provides a structure file (.gro), a topology-include file (.itp) and a position-restraints file (.itp).

Tools to analyze Martini CNT simulations can be found here: https://github.com/bio-phys/cnt-martini-analysis. 

# Requirements

Python 2.7 with packages math and sys

# Usage

For a new nanotube model, run

    python martini-cnt-generator.py [number of rings] [number of beads per ring] [number of functionalized rings at one end] [number of functionalized rings at the other end] [bead type of the functional groups]

for example

    python martini-cnt-generator.py 12 8 1 1 SNda

The type of functionalized end group can be changed within this script, e.g. to SP3.

# Literature

If the script or the model is helpful, please cite:
 - M. Vögele, J. Köfinger, G. Hummer: 
Simulations of Carbon Nanotube Porins in Lipid Bilayers.
Faraday Discussions (submitted, February 2018)

The model is based on previous work:
 - R. M. Bhaskara, S. M. Linker, M. Vögele, J. Köfinger, G. Hummer 
Carbon Nanotubes Mediate Fusion of Lipid Vesicles.
ACS Nano, 2017, 11 (2), pp 1273–1280
 - M. Vögele, G. Hummer:
Divergent Diffusion Coefficients in Simulations of Fluids and Lipid Membranes.
J. Phys. Chem. B, 2016, 120 (33), pp 8722–8732
DOI: 10.1021/acs.jpcb.6b05102
 - S. Baoukina, L. Monticelli, D.P. Tieleman:
Interaction of Pristine and Functionalized Carbon Nanotubes with Lipid Membranes. 
J. Phys. Chem. B (2013), 117, 12113-23.
 - L. Monticelli
On atomistic and coarse-grained models for C60 fullerene. 
J. Chem. Theory Comput. (2012), 8, 1370−1378 (DOI: 10.1021/ct3000102). 


