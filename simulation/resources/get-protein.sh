PFOLDER="1okc-cg"

cp $PFOLDER/protein-cg.itp protein.itp
printf "1\n\n" | gmx trjconv -f $PFOLDER/coarsegrained-system.pdb -n $PFOLDER/coarsegrained-system.ndx -s $PFOLDER/coarsegrained-system.pdb -o protein.pdb
