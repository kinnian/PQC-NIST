# Implémentation du protocole MamaBear en Python
## version CCA

Ce dossier rassemble le code python que j'ai construit pour implémenter le protocole d'encapsulation de clé MamaBear.


## WIP
#### commit 1
Pour l'instant, le fichiers test.py rassemble le "pseudo-code" python de toutes les fonctions nécessaires à l'implémentation de MamaBear ; les constantes sont celles de MamaBear, et les fonctions sont des retranscription (pour le momen) quasi littérale des pseudo-codes situés dans la documentation de la soumission ThreeBears et dans la documentation sur, entre autres, la fonction [cSHAKE256](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-185.pdf).

Cette implémentation, en plus des bibliothèques `math`, `numpy` et `os` -- cette dernière étant utilisée principalement pour la génération de chaînes d'octet de longueur determinée --, utilise la bibliothèque `_pysha3` disponible [ici](https://github.com/tiran/pysha3), un wrap-up python de la bibliothèque C `KeccakCodePackage`, qui implémente de manière optimisée les fonctions de hachage Keccak. A noter que c'est cette bibliothèque C qui est utilisée par l'implémentation en C fournie dans la soumission au NIST.


#### commit 2
Deux appels aux fonctions ont été ajoutées en fin de fichier pour pouvoir tester le code. Par conséquent, des corrections ont été apportées pour rendre le
"pseudo-code" plus "réel".

TODO: implémenter un typage pour pouvoir distinguer plus facilement ce qui est int, bytes, bytearray...
