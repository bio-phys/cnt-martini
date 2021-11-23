==========
 Contents
==========

cg-em.mdp                --- MDP file for Energy Minimising the CG System
1000ns.mdp               --- MDP file for 1000 ns of Molecular Dynamics
coarsegrained-system.pdb --- PDB file of the system
topol2.top               --- Topology File for system
coarsegrained-system.ndx --- Index file for system
martini_v2.1.itp         --- Martini Parameters 
protein-cg.itp           --- Protein Parameters 

================
 Example Usage 
================

Energy Minimise:

mkdir EM

grompp -f cg-em.mdp -o EM/em -c coarsegrained-system.pdb -n coarsegrained-system.ndx -p topol2.top

cd EM

mdrun -deffnm em -v

=========================================================================================================

Run 1000 ns of Coarse Grained Molecular Dynamics Simulation:

mkdir 1000ns

grompp -f 1000ns.mdp -o 1000ns/md -c EM/em.gro -n coarsegrained-system.ndx -p topol2.top

cd 1000ns

mdrun -deffnm md -v

=========================================================================================================
