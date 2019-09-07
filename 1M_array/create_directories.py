'''
This script is run manually from a directory containing a master 1M directory containing the necessary variables and modifications for duplication. When executed, 
this script will make directories for every desired model and copy the master 1M directory into each, with modifications made by use of string.Template. Every 
array directory you create should have a copy of the parent simulation, with each of the inlist files modified such that every prompt for mass and Z is replaced
with the appropriate variable $mass or $z.
'''

import os
import numpy as np
from string import Template

#./mk master 1M
os.chdir("master_1M")
os.system("./mk")
os.chdir("..")

mass_list = np.arange(0.25, 8, 0.25)
Z_list = [0.014, 0.017, 0.020, 0.023, 0.026]

for mass in mass_list:
	for Z in Z_list:
		#make a directory titled by mass and Z
		os.mkdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")

		#copy master 1M to each new directory
		os.system("cp -rf master_1M WD_" + str(mass) + "_M_" + str(Z) + "_Z/controls")

		#cd to each directory
		os.chdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")
		os.chdir("controls")

		#substitute the variables $mass and $z with the mass and Z values from the string
                d = {'mass':mass, 'z':Z}

                #inlist_start
                filein_start = open("/home/acorreia7/star_projects/1M_array/master_1M/inlist_start")
                src_start = Template(filein_start.read())
                result_start = src_start.substitute(d)
                out_inlist_start = open("inlist_start", "w")
                out_inlist_start.write(result_start)
                out_inlist_start.close()

                #inlist_to_end_agb
                filein_agb = open("/home/acorreia7/star_projects/1M_array/master_1M/inlist_to_end_agb")
                src_agb = Template(filein_agb.read())
                result_agb = src_agb.substitute(d)
                out_inlist_agb = open("inlist_to_end_agb", "w")
                out_inlist_agb.write(result_agb)
                out_inlist_agb.close()

		#inlist_to_wd
                filein_wd = open("/home/acorreia7/star_projects/1M_array/master_1M/inlist_to_wd")
                src_wd = Template(filein_wd.read())
                result_wd = src_wd.substitute(d)
                out_inlist_wd = open("inlist_to_wd", "w")
                out_inlist_wd.write(result_wd)
                out_inlist_wd.close()

		#cd back to the initial directory to continue the loop
		os.chdir("../..")
