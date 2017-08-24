#!/usr/bin/python
# ***************************************************************************
#    amber.py- Python script for the transformation of mden to a XY file for
#                 graphic display
#                             -------------------
#    begin                : Wed Jun 3 2004
#    copyright            : (C) 2004 by Nelson Fonseca
#    email                : nfonseca@dq.ua.pt
# ***************************************************************************/

# /***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/
# V0.1 03/06/2004
# V0.2 30/08/2004


############################
#       import modules     #
############################

import string  # import string module
import re  # import regular expression module
from array import *  # import everything from array module

###########################
#       input             #
###########################



mden = raw_input("Enter Input File Name: ")

file_input = open(mden)

lines = file_input.read()  # loads the entire file in one list of strings

lines_split = lines.split()  # splits the list in multiple strings with space delimiter by default

del lines_split[0:51]  # remove headers lines

####################################
# FILES FROM OUTPUT RESULTS        #
####################################

Nsteps_file = open("Nsteps.txt", "w")
Nsteps_file.write("\t""Nsteps""\t\t""time (ps)""\n")

Etot_file = open("Etot.txt", "w")
Etot_file.write("\t""time (ps)""\t""Etot (kcal/mol""\t\t""<Etot>""\n")

EKinetic_file = open("EKinetic.txt", "w")
EKinetic_file.write("\t""time (ps)""\t""EKinetic (kcal/mmol)""\t\t""<EKinetic>""\n")

Temp_file = open("Temp.txt", "w")
Temp_file.write("\t""time (ps)""\t""Temp (K)""\t\t\t""<Temp>""\n")

T_solute_file = open("T_solute.txt", "w")
T_solute_file.write("\t""time (ps)""\t""T_solute (K)""\t\t""<T_solute>""\n")

T_solv_file = open("T_solv.txt", "w")
T_solv_file.write("\t""time (ps)""\t""T_solv (K)""\t\t\t""<T_solv>""\n")

Pres_scal_solu_file = open("Pres_scal_solu.txt", "w")
Pres_scal_solu_file.write("\t""time (ps)""\t""Pres_scal_solu""\t\t""<Pres_scal_solu>""\n")

Pres_scal_solv_file = open("Pres_scal_solv.txt", "w")
Pres_scal_solv_file.write("\t""time (ps)""\t""Pres_scal_solv""\t\t""<Pres_scal_solv>""\n")

BoxX_file = open("BoxX.txt", "w")
BoxX_file.write("\t""time (ps)""\t""BoxX""\t\t\t""<BoxX>""\n")

BoxY_file = open("BoxY.txt", "w")
BoxY_file.write("\t""time (ps)""\t""BoxY""\t\t\t""<BoxY>""\n")

BoxZ_file = open("BoxZ.txt", "w")
BoxZ_file.write("\t""time (ps)""\t""BoxZ""\t\t\t""<BoxZ>""\n")

volume_file = open("volume.txt", "w")
volume_file.write("\t""time (ps)""\t""volume (A^3)""\t\t""<volume>""\n")

pres_X_file = open("pres_X.txt", "w")
pres_X_file.write("\t""time (ps)""\t""pres_X""\t\t\t""<pres_X>""\n")

pres_Y_file = open("pres_Y.txt", "w")
pres_Y_file.write("\t""time (ps)""\t""pres_Y""\t\t\t""<pres_Y>""\n")

pres_Z_file = open("pres_Z.txt", "w")
pres_Z_file.write("\t""time (ps)""\t""pres_Z""\t\t\t""<pres_Z>""\n")

Pressure_file = open("Pressure.txt", "w")
Pressure_file.write("\t""time (ps)""\t""Pressure""\t\t""<Pressure>""\n")

EKCoM_x_file = open("EKCoM_x.txt", "w")
EKCoM_x_file.write("\t""time (ps)""\t""EKCoM_x""\t\t\t""<EKCoM_x>""\n")

EKCoM_y_file = open("EKCoM_y.txt", "w")
EKCoM_y_file.write("\t""time (ps)""\t""EKCoM_y""\t\t\t""<EKCoM_y>""\n")

EKCoM_z_file = open("EKCoM_z.txt", "w")
EKCoM_z_file.write("\t""time (ps)""\t""EKCoM_z""\t\t\t""<EKCoM_z>""\n")

EKComTot_file = open("EKComTot.txt", "w")
EKComTot_file.write("\t""time (ps)""\t""EKComTot""\t\t""<EKComTot>""\n")

VIRIAL_x_file = open("VIRIAL_x.txt", "w")
VIRIAL_x_file.write("\t""time (ps)""\t""VIRIAL_x""\t\t""<VIRIAL_x>""\n")

VIRIAL_y_file = open("VIRIAL_y.txt", "w")
VIRIAL_y_file.write("\t""time (ps)""\t""VIRIAL_y""\t\t""<VIRIAL_y>""\n")

VIRIAL_z_file = open("VIRIAL_z.txt", "w")
VIRIAL_z_file.write("\t""time (ps)""\t""VIRIAL_z""\t\t""<VIRIAL_z>""\n")

VIRIAL_tot_file = open("VIRIAL_tot.txt", "w")
VIRIAL_tot_file.write("\t""time (ps)""\t""VIRIAL_tot""\t\t""<VIRIAL_tot>""\n")

E_pot_file = open("E_pot.txt", "w")
E_pot_file.write("\t""time (ps)""\t""E_pot (kcal/mol)""\t\t""<E_pot>""\n")

E_vdw_file = open("E_vdw.txt", "w")
E_vdw_file.write("\t""time (ps)""\t""E_vdw (kcal/mol)""\t\t""<E_vdw>""\n")

E_el_file = open("E_el.txt", "w")
E_el_file.write("\t""time (ps)""\t""E_el (kcal/mol)""\t\t\t""<E_el>""\n")

E_hbon_file = open("E_hbon.txt", "w")
E_hbon_file.write("\t""time (ps)""\t""E_hbon (kcal/mol)""\t\t""<E_hbon>""\n")

E_bon_file = open("E_bon.txt", "w")
E_bon_file.write("\t""time (ps)""\t""E_bon (kcal/mol)""\t\t""<E_bon>""\n")

E_angle_file = open("E_angle.txt", "w")
E_angle_file.write("\t""time (ps)""\t""E_angle (kcal/mol)""\t\t""<E_angle>""\n")

E_dih_file = open("E_dih.txt", "w")
E_dih_file.write("\t""time (ps)""\t""E_dih (kcal/mol)""\t\t""<E_dih>""\n")

E_14vdw_file = open("E_14vdw.txt", "w")
E_14vdw_file.write("\t""time (ps)""\t""E_14vdw (kcal/mol)""\t\t""<E_14vdw>""\n")

E_14el_file = open("E_14el.txt", "w")
E_14el_file.write("\t""time (ps)""\t""E_14el (kcal/mol)""\t\t""<E_14el>""\n")

E_const_file = open("E_const.txt", "w")
E_const_file.write("\t""time (ps)""\t""E_const (kcal/mol)""\t\t""<E_const>""\n")

E_pol_file = open("E_pol.txt", "w")
E_pol_file.write("\t""time (ps)""\t""E_pol (kcal/mol)""\t\t""<E_pol>""\n")

AV_permMoment_file = open("AV_permMoment.txt", "w")
AV_permMoment_file.write("\t""time (ps)""\t""AV_permMoment""\t\t""<AV_permMoment>""\n")

AV_indMoment_file = open("AV_indMoment.txt", "w")
AV_indMoment_file.write("\t""time (ps)""\t""AV_indMoment""\t\t""<AV_indMoment>""\n")

AV_totMoment_file = open("AV_totMoment.txt", "w")
AV_totMoment_file.write("\t""time (ps)""\t""AV_totMoment""\t\t""<AV_totMoment>""\n")

Density_file = open("Density.txt", "w")
Density_file.write("\t""time (ps)""\t""Density (g/cm^3)""\t\t""<Density>""\n")

dV_dlambda_file = open("dV_dlambda.txt", "w")
dV_dlambda_file.write("\t""time (ps)""\t""dV/dlambda""\t\t""<dV/dlambda>""\n")

###########################
#                         #
#       Loops over file   #
###########################

j = 2  # time counter
i = 1  # Nstep counter

while i < len(lines_split) or j < len(lines_split):
    Nsteps = lines_split[i]
    time = lines_split[j]

    i = i + 51
    j = j + 51

    Nsteps_file.write("\t" + Nsteps + "\t" + time + "\n")

print
"\nOutputing..."

j = 2  # reinitialize time counter
k = 3  # set Etot counter
sum = 0.0  # initial sum counter for averages

matrix_Etot = array("f")
while j < len(lines_split) or k < len(lines_split):
    time = float(lines_split[j])
    Etot = float(lines_split[k])
    matrix_Etot.append(Etot)
    sum = sum + Etot
    average = sum / len(matrix_Etot)

    Etot_file.write("\t" + str(time) + "\t\t" + str(Etot) + "\t\t" + str(average) + "\n")

    j = j + 51
    k = k + 51

print
"Outputing..."

j = 2  # reinitialize time counter
l = 4  # EKinetic counter
sum = 0.0  # initial sum counter for averages

matrix_EKinetic = array("f")
while j < len(lines_split) or l < len(lines_split):
    time = float(lines_split[j])
    EKinetic = float(lines_split[l])
    matrix_EKinetic.append(EKinetic)
    sum = sum + EKinetic
    average = sum / len(matrix_EKinetic)

    EKinetic_file.write("\t" + str(time) + "\t\t" + str(EKinetic) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    l = l + 51

print
"Outputing..."

j = 2  # reinitialize time counter
m = 6  # Temp counter
sum = 0.0  # initial sum counter for averages

matrix_Temp = array("f")
while j < len(lines_split) or m < len(lines_split):
    time = float(lines_split[j])
    Temp = float(lines_split[m])
    matrix_Temp.append(Temp)
    sum = sum + Temp
    average = sum / len(matrix_Temp)

    Temp_file.write("\t" + str(time) + "\t\t" + str(Temp) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    m = m + 51

print
"Outputing..."

j = 2  # reinitialize time counter
n = 7  # T_solute counter
sum = 0.0  # initial sum counter for averages

matrix_T_solute = array("f")
while j < len(lines_split) or n < len(lines_split):
    time = float(lines_split[j])
    T_solute = float(lines_split[n])
    matrix_T_solute.append(T_solute)
    sum = sum + T_solute
    average = sum / len(matrix_T_solute)

    T_solute_file.write("\t" + str(time) + "\t\t" + str(T_solute) + "\t\t" + str(average) + "\n")

    j = j + 51
    n = n + 51

print
"Outputing..."

j = 2  # reinitialize time counter
o = 8  # T_solv counter
sum = 0.0  # initial sum counter for averages

matrix_T_solv = array("f")
while j < len(lines_split) or o < len(lines_split):
    time = float(lines_split[j])
    T_solv = float(lines_split[o])
    matrix_T_solv.append(T_solv)
    sum = sum + T_solv
    average = sum / len(matrix_T_solv)

    T_solv_file.write("\t" + str(time) + "\t\t" + str(T_solv) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    o = o + 51

print
"Outputing..."

j = 2  # reinitialize time counter
p = 9  # Pres_scal_solu counter
sum = 0.0  # initial sum counter for averages

matrix_Pres_scal_solu = array("f")
while j < len(lines_split) or p < len(lines_split):
    time = float(lines_split[j])
    Pres_scal_solu = float(lines_split[p])
    matrix_Pres_scal_solu.append(Pres_scal_solu)
    sum = sum + Pres_scal_solu
    average = sum / len(matrix_Pres_scal_solu)

    Pres_scal_solu_file.write("\t" + str(time) + "\t\t" + str(Pres_scal_solu) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    p = p + 51

print
"Outputing..."

j = 2  # reinitialize time counter
q = 11  # Pres_scal_solv counter
sum = 0.0  # initial sum counter for averages

matrix_Pres_scal_solv = array("f")
while j < len(lines_split) or q < len(lines_split):
    time = float(lines_split[j])
    Pres_scal_solv = float(lines_split[q])
    matrix_Pres_scal_solv.append(Pres_scal_solv)
    sum = sum + Pres_scal_solv
    average = sum / len(matrix_Pres_scal_solv)

    Pres_scal_solv_file.write("\t" + str(time) + "\t\t" + str(Pres_scal_solv) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    q = q + 51

print
"Outputing..."

j = 2  # reinitialize time counter
r = 12  # BoxX counter
sum = 0.0  # initial sum counter for averages

matrix_BoxX = array("f")
while j < len(lines_split) or r < len(lines_split):
    time = float(lines_split[j])
    BoxX = float(lines_split[r])
    matrix_BoxX.append(BoxX)
    sum = sum + BoxX
    average = sum / len(matrix_BoxX)

    BoxX_file.write("\t" + str(time) + "\t\t" + str(BoxX) + "\t\t" + str(average) + "\n")

    j = j + 51
    r = r + 51

print
"Outputing..."

j = 2  # reinitialize time counter
s = 13  # BoxY counter
sum = 0.0  # initial sum counter for averages

matrix_BoxY = array("f")
while j < len(lines_split) or s < len(lines_split):
    time = float(lines_split[j])
    BoxY = float(lines_split[s])
    matrix_BoxY.append(BoxY)
    sum = sum + BoxY
    average = sum / len(matrix_BoxY)

    BoxY_file.write("\t" + str(time) + "\t\t" + str(BoxY) + "\t\t" + str(average) + "\n")

    j = j + 51
    s = s + 51

print
"Outputing..."

j = 2  # reinitialize time counter
t = 14  # BoxZ counter
sum = 0.0  # initial sum counter for averages

matrix_BoxZ = array("f")
while j < len(lines_split) or t < len(lines_split):
    time = float(lines_split[j])
    BoxZ = float(lines_split[t])
    matrix_BoxZ.append(BoxZ)
    sum = sum + BoxZ
    average = sum / len(matrix_BoxZ)

    BoxZ_file.write("\t" + str(time) + "\t\t" + str(BoxZ) + "\t\t" + str(average) + "\n")

    j = j + 51
    t = t + 51

print
"Outputing..."

j = 2  # reinitialize time counter
u = 16  # volume counter
sum = 0.0  # initial sum counter for averages

matrix_volume = array("f")
while j < len(lines_split) or u < len(lines_split):
    time = float(lines_split[j])
    volume = float(lines_split[u])
    matrix_volume.append(volume)
    sum = sum + volume
    average = sum / len(matrix_volume)

    volume_file.write("\t" + str(time) + "\t\t" + str(volume) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    u = u + 51

print
"Outputing..."

j = 2  # reinitialize time counter
v = 17  # pres_X counter
sum = 0.0  # initial sum counter for averages

matrix_pres_X = array("f")
while j < len(lines_split) or v < len(lines_split):
    time = float(lines_split[j])
    pres_X = float(lines_split[v])
    matrix_pres_X.append(pres_X)
    sum = sum + pres_X
    average = sum / len(matrix_pres_X)

    pres_X_file.write("\t" + str(time) + "\t\t" + str(pres_X) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    v = v + 51

print
"Outputing..."

j = 2  # reinitialize time counter
w = 18  # pres_Y counter
sum = 0.0  # initial sum counter for averages

matrix_pres_Y = array("f")
while j < len(lines_split) or w < len(lines_split):
    time = float(lines_split[j])
    pres_Y = float(lines_split[w])
    matrix_pres_Y.append(pres_Y)
    sum = sum + pres_Y
    average = sum / len(matrix_pres_Y)

    pres_Y_file.write("\t" + str(time) + "\t\t" + str(pres_Y) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    w = w + 51

print
"Outputing..."

j = 2  # reinitialize time counter
y = 19  # pres_Z counter
sum = 0.0  # initial sum counter for averages

matrix_pres_Z = array("f")
while j < len(lines_split) or y < len(lines_split):
    time = float(lines_split[j])
    pres_Z = float(lines_split[y])
    matrix_pres_Z.append(pres_Z)
    sum = sum + pres_Z
    average = sum / len(matrix_pres_Z)

    pres_Z_file.write("\t" + str(time) + "\t\t" + str(pres_Z) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    y = y + 51

print
"Outputing..."

j = 2  # reinitialize time counter
z = 21  # Pressure counter
sum = 0.0  # initial sum counter for averages

matrix_Pressure = array("f")
while j < len(lines_split) or z < len(lines_split):
    time = float(lines_split[j])
    Pressure = float(lines_split[z])
    matrix_Pressure.append(Pressure)
    sum = sum + Pressure
    average = sum / len(matrix_Pressure)

    Pressure_file.write("\t" + str(time) + "\t\t" + str(Pressure) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    z = z + 51

print
"Outputing..."

j = 2  # reinitialize time counter
kk = 22  # EKCoM_x counter
sum = 0.0  # initial sum counter for averages

matrix_EKCoM_x = array("f")
while j < len(lines_split) or kk < len(lines_split):
    time = float(lines_split[j])
    EKCoM_x = float(lines_split[kk])
    matrix_EKCoM_x.append(EKCoM_x)
    sum = sum + EKCoM_x
    average = sum / len(matrix_EKCoM_x)

    EKCoM_x_file.write("\t" + str(time) + "\t\t" + str(EKCoM_x) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    kk = kk + 51

print
"Outputing..."

j = 2  # reinitialize time counter
ll = 23  # EKCoM_y counter
sum = 0.0  # initial sum counter for averages

matrix_EKCoM_y = array("f")
while j < len(lines_split) or ll < len(lines_split):
    time = float(lines_split[j])
    EKCoM_y = float(lines_split[ll])
    matrix_EKCoM_y.append(EKCoM_y)
    sum = sum + EKCoM_y
    average = sum / len(matrix_EKCoM_y)

    EKCoM_y_file.write("\t" + str(time) + "\t\t" + str(EKCoM_y) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    ll = ll + 51

print
"Outputing..."

j = 2  # reinitialize time counter
mm = 24  # EKCoM_Z counter
sum = 0.0  # initial sum counter for averages

matrix_EKCoM_z = array("f")
while j < len(lines_split) or mm < len(lines_split):
    time = float(lines_split[j])
    EKCoM_z = float(lines_split[mm])
    matrix_EKCoM_z.append(EKCoM_z)
    sum = sum + EKCoM_z
    average = sum / len(matrix_EKCoM_z)

    EKCoM_z_file.write("\t" + str(time) + "\t\t" + str(EKCoM_z) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    mm = mm + 51

print
"Outputing..."

j = 2  # reinitialize time counter
nn = 26  # EKComTot counter
sum = 0.0  # initial sum counter for averages

matrix_EKComTot = array("f")
while j < len(lines_split) or nn < len(lines_split):
    time = float(lines_split[j])
    EKComTot = float(lines_split[nn])
    matrix_EKComTot.append(EKComTot)
    sum = sum + EKComTot
    average = sum / len(matrix_EKComTot)

    EKComTot_file.write("\t" + str(time) + "\t\t" + str(EKComTot) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    nn = nn + 51

print
"Outputing..."

j = 2  # reinitialize time counter
oo = 27  # VIRIAL_x counter
sum = 0.0  # initial sum counter for averages

matrix_VIRIAL_x = array("f")
while j < len(lines_split) or oo < len(lines_split):
    time = float(lines_split[j])
    VIRIAL_x = float(lines_split[oo])
    matrix_VIRIAL_x.append(VIRIAL_x)
    sum = sum + VIRIAL_x
    average = sum / len(matrix_VIRIAL_x)

    VIRIAL_x_file.write("\t" + str(time) + "\t\t" + str(VIRIAL_x) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    oo = oo + 51

print
"Outputing..."

j = 2  # reinitialize time counter
pp = 28  # VIRIAL_y counter
sum = 0.0  # initial sum counter for averages

matrix_VIRIAL_y = array("f")
while j < len(lines_split) or pp < len(lines_split):
    time = float(lines_split[j])
    VIRIAL_y = float(lines_split[pp])
    matrix_VIRIAL_y.append(VIRIAL_y)
    sum = sum + VIRIAL_y
    average = sum / len(matrix_VIRIAL_y)

    VIRIAL_y_file.write("\t" + str(time) + "\t\t" + str(VIRIAL_y) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    pp = pp + 51

print
"Outputing..."

j = 2  # reinitialize time counter
qq = 29  # VIRIAL_z counter
sum = 0.0  # initial sum counter for averages

matrix_VIRIAL_z = array("f")
while j < len(lines_split) or qq < len(lines_split):
    time = float(lines_split[j])
    VIRIAL_z = float(lines_split[qq])
    matrix_VIRIAL_z.append(VIRIAL_z)
    sum = sum + VIRIAL_z
    average = sum / len(matrix_VIRIAL_z)

    VIRIAL_z_file.write("\t" + str(time) + "\t\t" + str(VIRIAL_z) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    qq = qq + 51

print
"Outputing..."

j = 2  # reinitialize time counter
rr = 31  # VIRIAL_tot counter
sum = 0.0  # initial sum counter for averages

matrix_VIRIAL_tot = array("f")
while j < len(lines_split) or rr < len(lines_split):
    time = float(lines_split[j])
    VIRIAL_tot = float(lines_split[rr])
    matrix_VIRIAL_tot.append(VIRIAL_tot)
    sum = sum + VIRIAL_tot
    average = sum / len(matrix_VIRIAL_tot)

    VIRIAL_tot_file.write("\t" + str(time) + "\t\t" + str(VIRIAL_tot) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    rr = rr + 51

print
"Outputing..."

j = 2  # reinitialize time counter
ss = 32  # E_pot counter
sum = 0.0  # initial sum counter for averages

matrix_E_pot = array("f")
while j < len(lines_split) or ss < len(lines_split):
    time = float(lines_split[j])
    E_pot = float(lines_split[ss])
    matrix_E_pot.append(E_pot)
    sum = sum + E_pot
    average = sum / len(matrix_E_pot)

    E_pot_file.write("\t" + str(time) + "\t\t" + str(E_pot) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    ss = ss + 51

print
"Outputing..."

j = 2  # reinitialize time counter
tt = 33  # E_vdw counterE_bon
sum = 0.0  # initial sum counter for averages

matrix_E_vdw = array("f")
while j < len(lines_split) or tt < len(lines_split):
    time = float(lines_split[j])
    E_vdw = float(lines_split[tt])
    matrix_E_vdw.append(E_vdw)
    sum = sum + E_vdw
    average = sum / len(matrix_E_vdw)

    E_vdw_file.write("\t" + str(time) + "\t\t" + str(E_vdw) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    tt = tt + 51

print
"Outputing..."

j = 2  # reinitialize time counter
uu = 34  # E_el counter
sum = 0.0  # initial sum counter for averages

matrix_E_el = array("f")
while j < len(lines_split) or uu < len(lines_split):
    time = float(lines_split[j])
    E_el = float(lines_split[uu])
    matrix_E_el.append(E_el)
    sum = sum + E_el
    average = sum / len(matrix_E_el)

    E_el_file.write("\t" + str(time) + "\t\t" + str(E_el) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    uu = uu + 51

print
"Outputing..."

j = 2  # reinitialize time counter
vv = 36  # E_hbon counter
sum = 0.0  # initial sum counter for averages

matrix_E_hbon = array("f")
while j < len(lines_split) or vv < len(lines_split):
    time = float(lines_split[j])
    E_hbon = float(lines_split[vv])
    matrix_E_hbon.append(E_hbon)
    sum = sum + E_hbon
    average = sum / len(matrix_E_hbon)

    E_hbon_file.write("\t" + str(time) + "\t\t" + str(E_hbon) + "\t\t\t\t" + str(average) + "\n")

    j = j + 51
    vv = vv + 51

print
"Outputing..."

j = 2  # reinitialize time counter
ww = 37  # E_bon counter
sum = 0.0  # initial sum counter for averages

matrix_E_bon = array("f")
while j < len(lines_split) or ww < len(lines_split):
    time = float(lines_split[j])
    E_bon = float(lines_split[ww])
    matrix_E_bon.append(E_bon)
    sum = sum + E_bon
    average = sum / len(matrix_E_bon)

    E_bon_file.write("\t" + str(time) + "\t\t" + str(E_bon) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    ww = ww + 51

print
"Outputing..."

j = 2  # reinitialize time counter
yy = 38  # E_angle counter
sum = 0.0  # initial sum counter for averages

matrix_E_angle = array("f")
while j < len(lines_split) or yy < len(lines_split):
    time = float(lines_split[j])
    E_angle = float(lines_split[yy])
    matrix_E_angle.append(E_angle)
    sum = sum + E_angle
    average = sum / len(matrix_E_angle)

    E_angle_file.write("\t" + str(time) + "\t\t" + str(E_angle) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    yy = yy + 51

print
"Outputing..."

j = 2  # reinitialize time counter
zz = 39  # E_dih counter
sum = 0.0  # initial sum counter for averages

matrix_E_dih = array("f")
while j < len(lines_split) or zz < len(lines_split):
    time = float(lines_split[j])
    E_dih = float(lines_split[zz])
    matrix_E_dih.append(E_dih)
    sum = sum + E_dih
    average = sum / len(matrix_E_dih)

    E_dih_file.write("\t" + str(time) + "\t\t" + str(E_dih) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    zz = zz + 51

print
"Outputing..."

j = 2  # reinitialize time counter
kkk = 41  # E_14vdw counter
sum = 0.0  # initial sum counter for averages

matrix_E_14vdw = array("f")
while j < len(lines_split) or kkk < len(lines_split):
    time = float(lines_split[j])
    E_14vdw = float(lines_split[kkk])
    matrix_E_14vdw.append(E_14vdw)
    sum = sum + E_14vdw
    average = sum / len(matrix_E_14vdw)

    E_14vdw_file.write("\t" + str(time) + "\t\t" + str(E_14vdw) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    kkk = kkk + 51

print
"Outputing..."

j = 2  # reinitialize time counter
lll = 42  # E_14el counter
sum = 0.0  # initial sum counter for averages

matrix_E_14el = array("f")
while j < len(lines_split) or lll < len(lines_split):
    time = float(lines_split[j])
    E_14el = float(lines_split[lll])
    matrix_E_14el.append(E_14el)
    sum = sum + E_14el
    average = sum / len(matrix_E_14el)

    E_14el_file.write("\t" + str(time) + "\t\t" + str(E_14el) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    lll = lll + 51

print
"Outputing..."

j = 2  # reinitialize time counter
mmm = 43  # E_const counter
sum = 0.0  # initial sum counter for averages

matrix_E_const = array("f")
while j < len(lines_split) or mmm < len(lines_split):
    time = float(lines_split[j])
    E_const = float(lines_split[mmm])
    matrix_E_const.append(E_const)
    sum = sum + E_const
    average = sum / len(matrix_E_const)

    E_const_file.write("\t" + str(time) + "\t\t" + str(E_const) + "\t\t\t\t" + str(average) + "\n")

    j = j + 51
    mmm = mmm + 51

print
"Outputing..."

j = 2  # reinitialize time counter
nnn = 44  # E_pol counter
sum = 0.0  # initial sum counter for averages

matrix_E_pol = array("f")
while j < len(lines_split) or nnn < len(lines_split):
    time = float(lines_split[j])
    E_pol = float(lines_split[nnn])
    matrix_E_pol.append(E_pol)
    sum = sum + E_pol
    average = sum / len(matrix_E_pol)

    E_pol_file.write("\t" + str(time) + "\t\t" + str(E_pol) + "\t\t\t\t" + str(average) + "\n")

    j = j + 51
    nnn = nnn + 51

print
"Outputing..."

j = 2  # reinitialize time counter
ooo = 46  # AV_permMoment counter
sum = 0.0  # initial sum counter for averages

matrix_AV_permMoment = array("f")
while j < len(lines_split) or ooo < len(lines_split):
    time = float(lines_split[j])
    AV_permMoment = float(lines_split[ooo])
    matrix_AV_permMoment.append(AV_permMoment)
    sum = sum + AV_permMoment
    average = sum / len(matrix_AV_permMoment)

    AV_permMoment_file.write("\t" + str(time) + "\t\t" + str(AV_permMoment) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    ooo = ooo + 51

print
"Outputing..."

j = 2  # reinitialize time counter
ppp = 47  # AV_indMoment counter
sum = 0.0  # initial sum counter for averages

matrix_AV_indMoment = array("f")
while j < len(lines_split) or ppp < len(lines_split):
    time = float(lines_split[j])
    AV_indMoment = float(lines_split[ppp])
    matrix_AV_indMoment.append(AV_indMoment)
    sum = sum + AV_indMoment
    average = sum / len(matrix_AV_indMoment)

    AV_indMoment_file.write("\t" + str(time) + "\t\t" + str(AV_indMoment) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    ppp = ppp + 51

print
"Outputing..."

j = 2  # reinitialize time counter
qqq = 48  # AV_totMoment counter
sum = 0.0  # initial sum counter for averages

matrix_AV_totMoment = array("f")
while j < len(lines_split) or qqq < len(lines_split):
    time = float(lines_split[j])
    AV_totMoment = float(lines_split[qqq])
    matrix_AV_totMoment.append(AV_totMoment)
    sum = sum + AV_totMoment
    average = sum / len(matrix_AV_totMoment)

    AV_totMoment_file.write("\t" + str(time) + "\t\t" + str(AV_totMoment) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    qqq = qqq + 51

print
"Outputing..."

j = 2  # reinitialize time counter
rrr = 49  # Density counter
sum = 0.0  # initial sum counter for averages

matrix_Density = array("f")
while j < len(lines_split) or rrr < len(lines_split):
    time = float(lines_split[j])
    Density = float(lines_split[rrr])
    matrix_Density.append(Density)
    sum = sum + Density
    average = sum / len(matrix_Density)

    Density_file.write("\t" + str(time) + "\t\t" + str(Density) + "\t\t\t\t" + str(average) + "\n")

    j = j + 51
    rrr = rrr + 51

print
"Outputing..."

j = 2  # reinitialize time counter
sss = 50  # dV/dlambda counter
sum = 0.0  # initial sum counter for averages

matrix_dV_dlambda = array("f")
while j < len(lines_split) or sss < len(lines_split):
    time = float(lines_split[j])
    dV_dlambda = float(lines_split[sss])
    matrix_dV_dlambda.append(dV_dlambda)
    sum = sum + dV_dlambda
    average = sum / len(matrix_dV_dlambda)

    dV_dlambda_file.write("\t" + str(time) + "\t\t" + str(dV_dlambda) + "\t\t\t" + str(average) + "\n")

    j = j + 51
    sss = sss + 51

print
"Outputing..."

print
"\nFINISH! Now you can plot the data files."
