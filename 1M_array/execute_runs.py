'''
This script will run through the slurm script "job.mpi," which is found in each of the set directories. When executed, this script will run each of the models
found within the set. Note that you will have to manually move each of the directories to the appropriate sets using the console before running this or any future
scripts. The simplest way to do this is either organizing by mass (as I have) or by Z.
'''

import os

models = [f for f in os.listdir('.') if os.path.isdir(f)]

#cd to each model within the set
for model in models:
	os.chdir(model)
	os.chdir("controls")

#run the model and cd back to the set directory
	os.system("./rn")
	os.chdir("../..")
		
