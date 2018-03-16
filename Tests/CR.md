# Compte-rendu des tests effectués

### Remarque préliminaire
Les protocoles Kindi-{256-5,512-3}, {A,O}KCN-RLWE, uRound2-RLWR5 et {Mama,Papa}Bear n'ont pas pu être testées sur ma machine. Il s'agit la plupart du temps d'une erreur lors du `make`. En revanche, comme ces erreurs ne sont pas relevées par les tests de performances effectués par le NIST, il s'agit probablement d'un défaut de la machine utilisée (absence d'une librairie, ...) qui pourra potentiellement être corrigé par la suite.


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
