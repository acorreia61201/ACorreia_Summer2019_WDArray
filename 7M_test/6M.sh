#!/bin/bash

#SBATCH -J 6M
#SBATCH -o 6M.%j.out
#SBATCH -e 6M.%j.error
#SBATCH --nodes=1 --sockets-per-node=1 --cores-per-socket=1 --threads-per-core=2
#SBATCH -t 2:30:00
#SBATCH --mail-user acorreia7@umassd.edu
#SBATCH --gres=gpu:M2050:0

export NUM_OMP_THREADS=2
cd 6M_prems_to_agb
./rn
