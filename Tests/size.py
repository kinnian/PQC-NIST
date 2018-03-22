# Evalue la taille moyenne des cles privee, publique, du chiffre et du secret commun des protocoles KEM dont le produit de l'execution est passe en parametre

# Recupere la variable path_name directement du bash
from docopt import docopt
import os

help = """ Calcul des tailles moyennes

Usage:
    size.py <arg>

Options:
    -h --help

"""

path = docopt(help).get('<arg>')

def size(path_name):
    output = open(os.path.abspath(path_name), "r")
    results = output.read();
    data = results.split('\n\n')    # on separe les differentes instances
    data = data[1:]     # on supprime le '# <Nom du protocoles>' du debut du fichier

    sk_bytes = 0
    pk_bytes = 0
    ct_bytes = 0
    ss_bytes = 0

    for i in range(100):
        keys = data[i].split('\n')
        pk = keys[2].split(' ')[2]
        sk = keys[3].split(' ')[2]
        ct = keys[4].split(' ')[2]
        ss = keys[5].split(' ')[2]
        
        # Taille en octets
        pk_curr = len(pk)/2
        sk_curr = len(sk)/2
        ct_curr = len(ct)/2
        ss_curr = len(ss)/2
    
        sk_bytes = sk_bytes + sk_curr
        pk_bytes = pk_bytes + pk_curr
        ct_bytes = ct_bytes + ct_curr
        ss_bytes = ss_bytes + ss_curr

    # Moyenne sur les 100 instances
    sk_bytes = sk_bytes/100
    pk_bytes = pk_bytes/100
    ct_bytes = ct_bytes/100
    ss_bytes = ss_bytes/100

    print("sk, pk, ct, ss :")
    print(sk_bytes, pk_bytes, ct_bytes, ss_bytes)
    return 0

size(path)

