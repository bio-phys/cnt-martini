#!/usr/bin/python

import sys
import math
from math import *
import argparse


# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument( "-nr", "--numrings",   type=int,   default=12,     help='Number of rings (~height)'                           )
parser.add_argument( "-rs", "--ringsize",   type=int,   default=8,      help='Number of beads per ring (~circumference)'           )
parser.add_argument( "-bl", "--bondlength", type=float, default=0.47,   help='Length of one bond'                                  )
parser.add_argument( "-bt", "--beadtype",   type=str,   default='CNP',  help='Type of the regular beads'                           )
parser.add_argument( "-ft", "--functype",   type=str,   default='SNda', help='Type of the functionalization beads'                 )
parser.add_argument( "-fb", "--numfuncb",   type=int,   default=1,      help='Number of funct. bead rings at the beginning'        )
parser.add_argument( "-fe", "--numfunce",   type=int,   default=1,      help='Number of funct. bead rings at the end'              )
parser.add_argument( "-fn", "--filename",   type=str,   default=None,   help='Name of the output, default: generate automatically' )
args = parser.parse_args()


numrings = args.numrings
ringsize = args.ringsize
a 	 = args.bondlength
beadtype = args.beadtype
functype = args.functype
numfuncb = args.numfuncb
numfunce = args.numfunce

if args.filename == None:
	filename = "cnt-"+str(numrings)+"-"+str(ringsize)+"-a"+"%3i"%(1000*a)+"-"+beadtype+"-f"+str(numfuncb)+str(numfunce)+"-"+functype
else:
        filename = args.filename
	
numatoms = numrings*ringsize
alpha 	 = 2*math.pi/ringsize
R 	 = a/(2*sin(alpha/2))


print( "------------------------------------------------------------------------------" )
print( "Generating a Martini model for an open CNT using "+str(numrings)+" rings with "+str(ringsize)+" each." )
print( "------------------------------------------------------------------------------" )


print( "The "+str(numfuncb)+" first and the "+str(numfunce)+" last rings will be of type "+functype+"." )


#----------------#
# Structure File #
#----------------#


# Open the file for writing

structure_file = open(filename+".gro", 'w')


# Header

if numfuncb > 0 or numfunce > 0:
	structure_file.write( "cnt-%s-%s-f%s%s-%s\n" % (numrings, ringsize, numfuncb, numfunce, functype) )
else:
	structure_file.write( "cnt-%s-%s-f%s%s\n" % (numrings, ringsize, numfuncb, numfunce) )
structure_file.write( "  %3d\n" % (numatoms) )


# Atoms

for i in range(0, numrings):
	for j in range(0, ringsize):
		n = i*ringsize + j + 1
		p = j*alpha + i%2*alpha/2
		x = R*sin(p)
		y = R*cos(p)
		z = i*a*sqrt(3)/2
		if ( i < numfuncb or i >= numrings-numfunce):
			structure_file.write(  "%5d%-5s F%03d%5d%8.3f%8.3f%8.3f%8.4f%8.4f%8.4f\n" % (1, "  CNT", n%1000, n%100000, x, y, z, 0, 0, 0) )
		else:
			structure_file.write(  "%5d%-5s C%03d%5d%8.3f%8.3f%8.3f%8.4f%8.4f%8.4f\n" % (1, "  CNT", n%1000, n%100000, x, y, z, 0, 0, 0) )


# Box Dimensions

bx = ringsize*a
by = ringsize*a
bz = numrings*a+1

structure_file.write(  "   %u  %u  %u\n" % (bx, by, bz) )

structure_file.close()



#---------------#
# Topology File #
#---------------#


# Open the file for writing

topology_file = open(filename+".itp", 'w')

# Variables

numatoms = numrings*ringsize
alpha 	 = 180*(ringsize-2)/ringsize
beta 	 = (180/math.pi)*2*acos(tan(math.pi/(2*ringsize))/sqrt(3))

# Header

topology_file.write( "; \n; Carbon nanotube topology\n; for the Martini force field\n;\n; created by martini-tube-topology.py\n;\n" )
topology_file.write( "; Martin Voegele\n; Max Planck Institute of Biophysics\n;\n\n" )

topology_file.write( "[ moleculetype ]\n" )
topology_file.write( "; Name	 nrexcl\n" )
if numfuncb > 0 or numfunce > 0:
	topology_file.write( "cnt-%s-%s-f%s%s-%s  1\n" % (numrings, ringsize, numfuncb, numfunce, functype) )
else:
	topology_file.write( "cnt-%s-%s-f%s%s  1\n" % (numrings, ringsize, numfuncb, numfunce) )


# Atoms

topology_file.write( "\n[ atoms ]\n" )
topology_file.write( "; nr	 type	 resnr	 residue	 atom	 cgnr	 charge	 mass\n" )

#for i in range(1, numatoms+1):
for m in range(0, numrings):
	for n in range(1, ringsize+1):
		i = m*ringsize + n
		if ( m < numfuncb or m >= numrings-numfunce):
			topology_file.write( "%3d    %4s   1   CNT    F%03d     %3d       0      48\n" % (i, functype, i, i) )
		else:
			topology_file.write( "%3d    %4s   1   CNT    C%03d     %3d       0      48\n" % (i, beadtype, i, i) )


# Bonds

topology_file.write( "\n[ bonds ]\n" )
topology_file.write( "; i	 j	  funct	 length	 force\n" )

topology_file.write( "; rings\n" )

for m in range(1, numrings+1):
	for n in range(1, ringsize+1):
		i = (m-1)*ringsize + n
		j = (m-1)*ringsize + n%ringsize + 1
		topology_file.write( "     %3d     %3d       1   %4.3f    5000\n" % (i, j, a) )


topology_file.write( "; between rings, short\n" )

for m in range(1, numrings):
	for n in range(1, ringsize+1):
		# odd-numbered rings
		if m%2 == 1: 	
			i = (m-1)*ringsize + n
			j = m*ringsize + n
			topology_file.write( "     %3d     %3d       1   %4.3f    5000\n" % (i, j, a) )
			if i%ringsize == 1: 
				k = (m+1)*ringsize
			else:
				k = m*ringsize + n-1
			topology_file.write( "     %3d     %3d       1   %4.3f    5000\n" % (i, k, a) )
		# even-numbered rings
		else: 		
			i = (m-1)*ringsize + n
			j = m*ringsize + n
			topology_file.write( "     %3d     %3d       1   %4.3f    5000\n" % (i, j, a) )
			if i%ringsize == 0: 
				k = i+1
			else:
				k = j+1
			topology_file.write( "     %3d     %3d       1   %4.3f    5000\n" % (i, k, a) )


# Angles

topology_file.write( "\n[ angles ]\n" )
topology_file.write( "; i	 j	 k	 funct	 angle	 force\n" )

topology_file.write( "; in rings\n" )

for m in range(1, numrings+1):
	for n in range(1, ringsize+1):
		i = (m-1)*ringsize + n
		j = (m-1)*ringsize + n%ringsize + 1
		k = (m-1)*ringsize + (n+1)%ringsize + 1
		topology_file.write( "     %3d     %3d     %3d       2     %3.3f     350\n" % (i, j, k, alpha) )


# Improper Dihedrals

topology_file.write( "\n[ dihedrals ]\n" )
topology_file.write( "; i	 j	 k	 l     func	 q0     cq\n" )


for m in range(1, numrings-1):
	for n in range(1, ringsize+1):
		i = (m-1)*ringsize + n
		j = m*ringsize + n
		l = (m+1)*ringsize + n
		# odd-numbered rings
		if m%2 == 1:
			if i%ringsize == 1: 
				k = (m+1)*ringsize
			else:
				k = m*ringsize + (n-1)
			topology_file.write( "     %3d     %3d     %3d     %3d       2        %3.3f      350\n" % (i,k,j,l,beta) )
		# even-numbered rings
		else:
			if i%ringsize == 0: 
				k = i+1
			else:
				k = j+1
			topology_file.write( "     %3d     %3d     %3d     %3d       2        %3.3f      350\n" % (i,j,k,l,beta) )


# Restraints

topology_file.write( "\n; Include Position restraint file\n" )
topology_file.write( "#ifdef POSRES\n" )
topology_file.write( "#include \"cnt-%d-%d-f%d%d-%s-posres.itp\"\n" % (numrings, ringsize, numfuncb, numfunce, functype) )
topology_file.write( "#endif\n" )

topology_file.close()



#--------------------------#
# Position Restraints File #
#--------------------------#


# Open the file for writing

posres_file = open(filename+"-posres.itp", 'w')


# Header

posres_file.write( "[ position_restraints ]\n" )
posres_file.write( "; ai  funct  fcx    fcy    fcz\n" )

for i in range(1, numatoms+1):
	posres_file.write( " %3d    1    1000   1000   1000\n" % (i) )
	
posres_file.close()

