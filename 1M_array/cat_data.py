'''
This script is to be run manually from each of the set directories after receiving results from each of the models. When executed, this script will concatenate
the history.data files from each of the three segments of every model and create a new file, "full_history.data," within the model directories themselves. This may
be used to graph HR diagrams or Kippenhahn diagrams as needed.
'''

import os

models = [f for f in os.listdir('.') if os.path.isdir(f)]

for model in models:
	#cd to each of the model directories
	os.chdir(model)

	#concatenate the results from each controls directory to the model directory
	os.system("cat controls/LOGS_start/history.data controls/LOGS_to_end_agb/history.data controls/LOGS_to_wd/history.data >> full_history.data")

	#cd back to the set directory to continue the loop
	os.chdir("..")
