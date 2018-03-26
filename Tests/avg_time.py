# Calcule le temps moyen d'execution de l'executable passe en parametre dans le prompt
import os

print("Chemin de l'executable ?")
os.system("./avg_time.sh")

output = open(os.path.abspath("./results"), "r").read()

times = output.split('s\n')
avg_time = 0
for i in range(50):
    avg_time = avg_time + float(times[i])

avg_time = avg_time/50
print("temps moyen: ", avg_time, "s")

os.system("rm results *.rsp *.req")
