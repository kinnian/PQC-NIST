#!/bin/bash

#Calcule le temps moyen d'exécution du programme donné

read

for i in `seq 1 50`
do
  { time $REPLY ; } 2>&1 | awk -F "m" '/real/ {print $2}' >> results
done
