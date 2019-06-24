for NUMRINGS in 08 10 12 14 16 18 20 24 28 ; do
	for RINGSIZE in 08 10 12 14 16 20 30 40 ; do
		for NUMFUNC in 0 1 2 ; do
			python martini-cnt-generator.py -nr $NUMRINGS -rs $RINGSIZE -ft SNda -nb $NUMFUNC -ne $NUMFUNC
		done
	done
done
