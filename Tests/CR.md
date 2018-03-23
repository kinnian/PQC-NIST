# Compte-rendu des tests effectués

### Remarque préliminaire
Les protocoles Kindi-{256-5,512-3}, uRound2-RLWR5 et {Mama,Papa}Bear n'ont pas pu être testées sur la première machine. Il s'agit la plupart du temps d'une erreur lors du `make`. En revanche, comme ces erreurs ne sont pas relevées par les tests de performances effectués par le NIST, il s'agit probablement d'un défaut de la machine utilisée (absence d'une librairie, ...).
Pour le moment, des tentatives de correction ont été apportées en ajoutant la bibliothèque [keccak](https://github.com/gvanas/KeccakCodePackage) `KeccakCodePackage`, dans sa version `Haswell`, ainsi que l'installation de [libkeccak](https://github.com/maandree/libkeccak). Cela a permis de compiler correctement les versions de références de MamaBear et PapaBear. Cependant, les versions optimisées, ainsi que uRound2-RLWR5 (qui utilise la même bibliothèque), font appel à des fonctions de cette bibliothèque que le compilateur ne semble pas trouver. 
Le même problème s'est présenté sur la deuxième machine sur laquelle j'ai testé ces codes, à quelques différences près :

* Cette fois-ci, le code fourni pour Kindi-{256-5,512-3} compile, et tourne correctement.
* En revanche, le code de LAC256 ne compile pas.


## Tailles

Les tailles trouvés en testant les implémentations correspondent effectivement aux tailles extraites de la documentation des différentes soumissions.

A noter cependant que les compressions parfois mentionnées dans la documentation ne sont pas implémentées, ni dans la version de référence, ni dans la version optimisée (voir par exemple Hila5).

## Temps d'exécution

Voici un tableau récapitulatif des temps moyen obtenus pour 100 instances (en secondes), sur deux ordinateurs différents, Ordi1 et Ordi2, pour les versions de références et optimisées :

| Protocoles  | Ordi1-ref | Ordi1-opt | Ordi2-ref  | Ordi2-opt |
|:---------   | ---------:| ---------:| ----------:| ---------:|
| Kyber1024   | 0.179     | 0.179     | 0.799      | 0.796     |
| Hila5       | 1.802     | 0.316     | 8.549      | 2.124     |
| LAC256      | 0.436     | 0.084     | *?*        | *?*       |
| NewHope1024 | 0.183     | 0.183     | 0.829      | 0.828     |
| FireSaber   | 0.325     | 0.196     | 1.608      | 0.934     |
| MamaBear    | 0.480     | *?*       | 2.187      | *?*       |
| PapaBear    | 0.781     | *?*       | 3.551      | *?*       |
| Kindi-256   | *?*       | *?*       | 0.571      | 0.571     |
| Kindi-512   | *?*       | *?*       | 0.590      | 0.590     |


* Pour les protocoles Kindi, il est précisé dans la documentation que la version de référence est aussi la version optimisée. Comme le NIST demandait que les codes de références ne contiennent aucune optimisation hardware, cela signifie que la version la plus optimisée de Kindi -- proposée dans la soumission -- ne prend pas en compte des éventuelles optimisations hardwares. 
* Pour Kyber1024 et NewHope1024, on ne voit aucune amélioration entre la version de référence et la version optimisée.
* Les temps mesurés ici, rapportés à une instance, sont 2 à 5 fois plus grands que ceux obtenus dans la documentation (voir [ici](../kem.md) ).
* Il y a une modification de l'ordre comparativement à l'étude précédente. On avait Hila5 < NewHope1024 < Kyber1024 < FireSaber < LAC256, on a maintenant LAC256 < Kyber1024 < NewHope1024 < FireSaber < Hila5. Ce deuxième ordre est plus proche de la "réalité", puisqu'il se base sur des mesures de performances effectuées sur la même machine. On retrouve à peu près le même ordre et les mêmes ordres de grandeurs de différences sur les tests de performances effectués par le NIST ; malheureusement, les temps d'exécutions y étant donnés en nombre de cycles (pour 100 instances), je ne peux pas comparer directement à mes valeurs. Pour information, on a :

| Protocoles  | Cycles    |
|:----------- | ---------:|
| LAC256      | 2,130,925 |
| Kindi-256-5 | 3,639,641 |
| Kindi-512-3 | 3,910,322 |
| NewHope1024 | 4,529,126 |
| Kyber1024   | 4,951,763 |
| FireSaber   | 6,040,376 |
| Hila5       | 13,869,431|
| uRound2-RLWR5 | 78,660,031 |

* Dans le test de performance du NIST, MamaBear et PapaBear se distingue par leur rapidité : respectivement 548,177 et 826,005 cycles pour 100 instances,
  soit presque 10 fois moins que les autres protocoles mentionnés dans le tableau précédent. Cependant, il s'agit le plus probablement des versions
  optimisées, et je n'arrive pas à exécuter ces versions, qui utilisent beaucoup de fonctions externes, et possiblement des optimisations hardware.
* A l'aide des exécutions sur une seconde machine, on peut voir que les codes Kindi se distinguent aussi par leur rapidité ; leur temps d'exécution est du même ordre de grandeur que Kyber1024. On peut en revanche supposer qu'ils restent plus lents que LAC256, qui est lui deux fois plus rapide que Kyber1024 (d'après les tests effectués sur la première machine et ceux du NIST).
