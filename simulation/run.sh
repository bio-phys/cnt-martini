set -ex

EDGE=10
HEIGHT=10

mkdir -p output
cd output

cp ../parameters/* .
cp ../../nanotubes/cnt-12-8-a470-CNP-f11-SNda.gro cnt.gro
cp ../../nanotubes/cnt-12-8-a470-CNP-f11-SNda.itp cnt.itp

insane -l POPC:1 -salt 0.15 -x $EDGE -y $EDGE -z $HEIGHT -center -pbc cubic -sol W:9 -sol WF:1 -f cnt.gro -p system.top -o system.gro

sed -i 's/Protein       /cnt-12-8-f11-SNda/g' system.top

printf '2|3|9|10 \n 4|5|6|7|8|11|12|13|14 \n name 15 Membrane \n name 16 Water \n q \n' | gmx make_ndx -f system.gro -o index.ndx

# Energy minimization
gmx grompp -c system.gro -f martini_em.mdp -p system.top -o martini_em.tpr
gmx mdrun -v -deffnm martini_em

# Short Equilibration
gmx grompp -c martini_em.gro -f martini_eq.mdp -p system.top -o martini_eq.tpr -n index.ndx
gmx mdrun -v -deffnm martini_eq -cpi martini_eq.cpt -cpt 5

# MD simulation
gmx grompp -c martini_eq.gro -f martini_md.mdp -p system.top -o martini_md.tpr -n index.ndx
gmx mdrun -v -deffnm martini_md -cpi martini_md.cpt -cpt 5

cd ..

