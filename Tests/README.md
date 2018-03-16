# Comment tester les soumissions choisies

Il y a deux programmes python, `size.py` et `avg_time.py`, qui permettent de calculer respectivement la taille (moyenne sur 100 instances) des clés privée et
publique, du chiffré et du secret commun du protocole choisi, et le temps moyen de l'exécution de l'implémentation donnée par la soumission de la création
de ces données.



## Calcul des tailles moyennes


Tout d'abord, avant de lancer la méthode python, il faut avoir produit le fichier contenant les 100 instances de (sk, pk, ct, ss). Pour se faire, il faut
se rendre dans le dossier du protocole choisi, dans sa version standard ou optimisé, lancer la commande `make` puis exécuter l'exécutable qui a été
produit.


La syntaxe d'utilisation de `size.py` est la suivante :
```
python size.py <Chemin du fichier>
```

La variable `<Chemin du fichier>` dépend du protocole choisi et se présente sous la forme `<Protocole>/<Protocole>-{ref,opt}/PQCkemKAT_<chiffre>.rsp`. Les
versions `ref` et `opt` correspondent respectivement aux versions standard et optimisée du protocole donné. La variable `<chiffre>` dépend du protocole, elle se trouve dans le dossier `<Protocole>/<Protocol>-{ref,opt}`.

*Exemple :*
```
python size.py Hila5/Hila5-opt/PQCkemKAT_1824.rsp
(sk, pk, ct, ss)
(1824, 1824, 2012, 32)
```
#### Remarque :
La taille est donnée en octets.

## Calcul du temps moyen

Pour calculer le temps moyen de l'exécutable fourni par la soumission, il faut lancer `avg_time.py` Pour ce faire, il faut commencer par déplacer
`avg_time.sh` dans `/bin/` afin que ce script bash puisse être correctement appelé par `avg_time.py` :
```
sudo mv avg_time.sh /bin/avg_time.sh
```

Lors de l'exécution de `avg_time.py`, il faudra donner le chemin (relatif) de l'exécutable choisi, que l'on trouve comme précédemment dans le dossier
`<Protocole>/<Protocole>-{ref,opt}`.

*Exemple :*
```
python avg_time.py
Chemin de l'executable ?
Hila5/Hila5-opt/genkat_opt
temps moyen: 0.3168s
```

#### Remarque
Le temps moyen donné correspond à la création de 100 instances de (clé privée, clé publique, chiffré, secret commun).
