set -ex

EDGE=10
HEIGHT=10

mkdir -p run
cd run

cp ../../cnt-12-8-a470-CNP-f11-SNda.gro cnt.gro
cp ../../cnt-12-8-a470-CNP-f11-SNda.itp cnt.itp

insane -l POPC:1 -salt 0.15 -x $EDGE -y $EDGE -z $HEIGHT -center -pbc cubic -sol W:9 -sol WF:1 -f cnt.gro -p system.top -o system.gro

#printf '1|13|14|15|16|17|23|24|25|26|27 \n 18|19|20|21|28|29|30|31 \n name 32 Membrane \n name 33 Water \n q \n' | gmx make_ndx -f system.gro -o index.ndx


cd ..

