#!/usr/bin/python
#***************************************************************************
#    pmf.py- Python script for PMF runs with sander
#                             -------------------
#    begin                : Wed Nov 3 2004
#    copyright            : (C) 2004 by Nelson Fonseca
#    email                : nfonseca@dq.ua.pt
# ***************************************************************************/

#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/
#V0.1 03/11/2004



############################
#       import modules     #
############################

import os                       # import Miscellaneous operating system interfaces module
import string                   # import string module


###########################
#       input             #
###########################


# INPUT .crd na forma de xxxx_col_1.rst
# valor do indice para o primeiro elemento de uma lista igual a zero, neste caso somente os pontos
# 15.5, 15.0, 14.5, 14.0 irao ser calculados para E=0
# apos 14.0 nao existe na lista o ponto i+2!!


dist = [0.00,0.25,0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,3.75,4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00] # Lista com os valores de distancias pretendidos
# Note que somente os pontos no intervalo [(i+1),i=(n-3)] em que n
# e o numero de elementos da lista irao ser calculados

for i in range(len(dist)):

    DISANG = open("disang","w")

    MDIN   = open("mdin","w")


    print i , dist[i]


    r1 = dist[i]
    r2 = dist[i+1]
    r3 = dist[i+2]

    ##################################################
    # disang file for equilibration and collect      #
    ##################################################

    print("WRITING DISANG FILE FOR STEP:............."+str(i))

    DISANG.write("# distance restraint between  anion and the receptor \n\
&rst \n\
IRESID = 0, \n\
IAT(1)= -1, \n\
IAT(2)= -1, \n\
IAT(3)= 0, \n\
IAT(4)= 0, \n\
IR6=0, \n\
IGR1(1)= 4,IGR1(2)= 29,IGR1(3)= 8,IGR1(4)= 24,IGR1(5)= 20,IGR1(6)= 13\n\
IGR2(1)= 97,IGR2(2)= 96,IGR2(3)= 95,IGR2(4)= 94,IGR2(5)= 93,IGR2(6)= 98 \n\
r1= "+str(float(r1))+", r2= "+str(float(r2))+", r3= "+str(float(r2))+", r4= "+str(float(r3))+", \n\
rk2=5.0, rk3=5.0, \n\
&end")



    #################################
    # collection mdin file  #
    #################################

    print("WRITING MDIN FILE FOR COLLECTION STEP:."+str(i))

    MDIN.write("#\n\
# collect \n\
&cntrl \n       \
nmropt = 1,\n   \
imin = 0, irest = 1, ntx = 5, \n        \
ntb = 2, ntp=1, taup=2.0, \n            \
cut = 12, ntr = 0, \n   \
ntc = 2, ntf = 2, \n    \
tempi = 300.0, temp0 = 300.0, \n        \
ntt = 3, gamma_ln = 1.0, \n     \
nstlim = 1, dt = 0.002, \n      \
ntpr = 100, \n  \
ntwx = 100, ioutfm = 0, ntxo = 1,\n     \
ntwr = 100, \n  \
ntwv = 100, ntwe = 100, \n      \
nscm = 1000, \n \
/ \n\
&end \n\
&wt type= 'DUMPFREQ', istep1 = 1, / \n\
&wt type= 'END', / \n\
LISTOUT =list_col_"+str(i)+".log \n\
DISANG = disang \n\
DUMPAVE = results_col_"+str(i)+".log \n\
&end \n ")

    #########################
    # equilibration run     #
    #########################

    os.system("mpiexec -machinefile machine.file -n 4 /programs/amber8/exe/sander.mpich2 -O -i mdin \
                             -o macro_meta_equi_"+str(i)+".out  \
                             -p macro_meta_solv_RESP.top        \
                             -c macro_meta_equi_"+str(i)+".rst  \
                             -r macro_meta_col_"+str(i)+".crd   \
                             -x macro_meta_equi_"+str(i)+".mdcrd        \
                             -e macro_meta_equi_"+str(i)+".mden")


    #########################
    # equilibration mdin_file       #
    #########################

    MDIN   = open("mdin","w")

    print("WRITING MDIN FILE FOR COLLECT STEP:......."+str(i)+"\n")

    MDIN.write("#\n\
# equilibration \n\
&cntrl \n       \
nmropt = 1,\n   \
imin = 0, irest = 0, ntx = 5, \n        \
ntb = 2, ntp=1, taup=2.0, \n    \
cut = 12, ntr = 0, \n   \
ntc = 2, ntf = 2, \n    \
tempi = 300.0, temp0 = 300.0, \n        \
ntt = 3, gamma_ln = 1.0, \n     \
nstlim = 1, dt = 0.002, \n      \
ntpr = 100, \n  \
ntwx = 100, ioutfm = 0, ntxo = 1,\n     \
ntwr = 100, \n  \
ntwv = 100, ntwe = 100, \n      \
nscm = 1000, \n \
/ \n\
&end \n\
&wt type= 'DUMPFREQ', istep1 = 1, / \n\
&wt type= 'END', / \n\
LISTOUT = list_equi_"+str(i+1)+".log \n\
DISANG = disang \n\
DUMPAVE = results_equi_"+str(i+1)+".log \n\
&end \n ")





    #########################
    # production run        #
    #########################

    os.system("mpiexec -machinefile machine.file -n 4 /programs/amber8/exe/sander.mpich2 -O -i mdin \
                             -o macro_meta_col_"+str(i)+".out   \
                             -p macro_meta_solv_RESP.top        \
                             -c macro_meta_col_"+str(i)+".crd   \
                             -r macro_meta_equi_"+str(i+1)+".rst        \
                             -x macro_meta_col_"+str(i)+".mdcrd \
                             -e macro_meta_col_"+str(i)+".mden")