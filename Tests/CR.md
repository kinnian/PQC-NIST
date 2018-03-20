# Compte-rendu des tests effectués

### Remarque préliminaire
Les protocoles Kindi-{256-5,512-3}, {A,O}KCN-RLWE, uRound2-RLWR5 et {Mama,Papa}Bear n'ont pas pu être testées sur ma machine. Il s'agit la plupart du temps d'une erreur lors du `make`. En revanche, comme ces erreurs ne sont pas relevées par les tests de performances effectués par le NIST, il s'agit probablement d'un défaut de la machine utilisée (absence d'une librairie, ...) qui pourra potentiellement être corrigé par la suite.
Pour le moment, des tentatives de correction ont été apportées en ajoutant la bibliothèque [keccak](https://github.com/gvanas/KeccakCodePackage) `KeccakCodePackage`. Cela a permis de compiler correctement les versions de références de MamaBear et PapaBear. Cependant, les versions optimisées, ainsi que uRound2-RLWR5 (qui utilise la même bibliothèque), font appel à des fonctions de cette bibliothèque que le compilateur ne semble pas trouver. 


## Tailles

Les tailles trouvés en testant les implémentations correspondent effectivement aux tailles extraites de la documentation des différentes soumissions.

A noter cependant que les compressions parfois mentionnées dans la documentation ne sont pas implémentées, ni dans la version de référence, ni dans la version optimisée (voir par exemple Hila5).

## Temps d'exécution

Voici un tableau récapitulatif des temps moyen obtenus pour 100 instances (en secondes) :

| Protocoles  | Référence | Optimisé  |
|:---------   | ---------:| ---------:|
| Kyber1024   | 0.179     | 0.179     |
| Hila5       | 1.802     | 0.316     |
| LAC256      | 0.436     | 0.084     |
| NewHope1024 | 0.183     | 0.183     |
| FireSaber   | 0.325     | 0.196     |
| MamaBear    | 0.480     | *?*       |
| PapaBear    | 0.781     | *?*       |

* Pour Kyber1024 et NewHope1024, on ne voit aucune amélioration entre la version de référence et la version optimisée.
* Les temps mesurés ici, rapportés à une instance, sont 2 à 5 fois plus grands que ceux obtenus dans la documentation (voir [ici](../kem.md) ).
* Il y a une modification de l'ordre comparativement à l'étude précédente. On avait Hila5 < NewHope1024 < Kyber1024 < FireSaber < LAC256, on a maintenant LAC256 < Kyber1024 < NewHope1024 < FireSaber < Hila5. Ce deuxième ordre est plus proche de la "réalité", puisqu'il se base sur des mesures de performances effectuées sur la même machine. On retrouve à peu près le même ordre et les mêmes ordres de grandeurs de différences sur les tests de performances effectués par le NIST ; malheureusement, les temps d'exécutions y étant donnés en nombre de cycles (pour 100 instances), je ne peux pas comparer directement à mes valeurs. Pour information, on a :

| Protocoles  | Cycles    |
|:----------- | ---------:|
| LAC256      | 2,130,925 |
| NewHope1024 | 4,529,126 |
| Kyber1024   | 4,951,763 |
| FireSaber   | 6,040,376 |
| Hila5       | 13,869,431|

* Dans le test de performance du NIST, MamaBear et PapaBear se distingue par leur rapidité : respectivement 548,177 et 826,005 cycles pour 100 instances,
  soit presque 10 fois moins que les autres protocoles mentionnés dans le tableau précédent. Cependant, il s'agit le plus probablement des versions
  optimisées, et je n'arrive pas à exécuter ces versions, qui utilisent beaucoup de fonctions externes. Cela signifie que non seulement je n'arrive pas à
  exécuter le code fourni dans la soumission au NIST, mais aussi que implémenter moi-même ces protocoles optimisés serait plus délicat que pour d'autres
  protocoles.
