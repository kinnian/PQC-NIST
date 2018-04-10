# Compte-rendu des tests effectués

### Remarque préliminaire
Les protocoles Kindi-{256-5,512-3}, uRound2-RLWR5 et {Mama,Papa}Bear n'ont pas pu être testées sur la première machine. Il s'agit la plupart du temps d'une erreur lors du `make`. En revanche, comme ces erreurs ne sont pas relevées par les tests de performances effectués par le NIST, il s'agit probablement d'un défaut de la machine utilisée (absence d'une librairie, ...).

Pour le moment, des tentatives de correction ont été apportées en ajoutant la bibliothèque [keccak](https://github.com/gvanas/KeccakCodePackage) `KeccakCodePackage`, dans sa version `Haswell`, ainsi que l'installation de [libkeccak](https://github.com/maandree/libkeccak). Cela a permis de compiler correctement les versions de références de MamaBear et PapaBear. Cependant, les versions optimisées, ainsi que uRound2-RLWR5 (qui utilise la même bibliothèque), font appel à des fonctions de cette bibliothèque que le compilateur ne semble pas trouver. 
Le même problème s'est présenté sur les deuxième et troisième machines sur laquelle j'ai testé ces codes, à quelques différences près :

* Cette fois-ci, le code fourni pour Kindi-{256-5,512-3} compile, et tourne correctement.
* En revanche, le code de LAC256 ne compile pas.


## Tailles

Les tailles trouvés en testant les implémentations correspondent effectivement aux tailles extraites de la documentation des différentes soumissions.

A noter cependant que les compressions parfois mentionnées dans la documentation ne sont pas implémentées, ni dans la version de référence, ni dans la version optimisée (voir par exemple Hila5).

## Temps d'exécution

Voici un tableau récapitulatif des temps moyen obtenus pour 100 instances (en secondes), sur trois ordinateurs différents, Ordi1, Ordi2 et Ordi3, pour les versions de références et optimisées :

| Protocoles  | Ordi1-ref | Ordi1-opt | Ordi2-ref  | Ordi2-opt | Ordi3-ref | Ordi3-opt |
|:---------   | ---------:| ---------:| ----------:| ---------:| ---------:| ---------:|
| Kyber1024   | 0.179     | 0.179     | 0.799      | 0.796     | 0.362     | 0.363     |
| Hila5       | 1.802     | 0.316     | 8.549      | 2.124     | 3.646     | 0.872     |
| LAC256      | 0.436     | 0.084     | *?*        | *?*       | *?*       | *?*       |
| NewHope1024 | 0.183     | 0.183     | 0.829      | 0.828     | 0.389     | 0.381     |
| FireSaber   | 0.325     | 0.196     | 1.608      | 0.934     | 0.760     | 0.406     |
| MamaBear    | 0.480     | *?*       | 2.187      | *?*       | 0.908     | *?*       |
| PapaBear    | 0.781     | *?*       | 3.551      | *?*       | 1.476     | *?*       |
| Kindi-256   | *?*       | *?*       | 0.571      | 0.571     | 0.263     | 0.263     |
| Kindi-512   | *?*       | *?*       | 0.590      | 0.590     | 0.260     | 0.260     |


#### Remarques

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


## Version benchmarkée

Une version benchmarkée des soumissions au NIST a été proposée [ici](https://github.com/mjosaarinen/pqcbench). Elle permet notamment d'évaluer le temps d'exécution total des KEMs soumis. Pour avoir un meilleur aperçu de l'ordre de grandeur des temps d'exécution de ces protocoles, je donne ici la liste complète de tous les KEMs utilisant LWE ou une variante, avec neufs des dix retenus précédemment indiqués en gras, LAC256 n'apparaissant pas dans cette liste. Sans doute mjosaarinen n'a pas réussi à exéctuer ce code en particulier dans son benchmark. J'ai ajouté de plus l'information concernant le niveau de sécurité et la taille de (clé publique + chiffré).


| Protocole			| Temps total (ms)	| pk + ct (octets)	| Niveau de sécurité	|
|:-----------------------------	| ---------------------:| ---------------------:| ---------------------:|
| BabyBearEphem        		| 0.05			| 1 721			| 2			|	
| BabyBear             		| 0.08			| 1 721			| 2			|
| MamaBearEphem        		| 0.08			| 2 501			| 4			|
| NewHope512    		| 0.09			| 2 048			| 1			|
| **MamaBear**	       		| 0.13			| 2 501			| 5			|
| PapaBearEphem        		| 0.13			| 3 281			| 5			|
| LAC128      	       		| 0.15			| 1 568			| 2			|
| RLizard2048          		| 0.17			| 16 448		| 5			|
| uRound2-RLWR1 		| 0.18			| 917			| 1			|
| Kyber512	       		| 0.18			| 1 536			| 1			|
| **PapaBear**	       		| 0.20			| 3 281			| 5			|
| uRound2-RLWR2 		| 0.25			| 1 173			| 2			|
| Kyber768	       		| 0.26			| 2 240			| 3			|
| AKCN-MLWE	       		| 0.27			| 2 111			| 4			|
| OKCN-MLWE	       		| 0.27			| 2 111			| 4			|
| uRound2-RLWR3 		| 0.28			| 1 201			| 3			|
| Kindi-256-3	           	| 0.31			| 2 976			| 2			|
| **NewHope1024**       	| 0.32			| 4 032			| 5			|		
| Kindi-512-2	           	| 0.36			| 3 952			| 4			|
| **Kyber1024**               	| 0.37			| 2 944			| 5			|	
| LIMA-2p	               	| 0.38			| 8 451			| 3			|
| **uRound2-RLWR5**		| 0.38			| 1 565			| 5			|
| uRound2-RLWR4			| 0.41			| 1 589			| 4			|
| OKCN-RLWE                   	| 0.42			| 3 651			| 5			|
| AKCN-RLWE                 	| 0.42			| 3 779			| 5			|
| ntru-443	           	| 0.48			| 1 222			| 1			|
| LightSaber               	| 0.61			| 1 408			| 1			|
| **Kindi-256-5**              	| 0.72			| 4 672			| 5 			|
| **Kindi-512-3**              	| 0.72			| 5 696			| 5			|
| Saber                    	| 1.10			| 2 080			| 3			|
| ntru-743	           	| 1.11			| 2 046			| 4			|
| uRound2-LWR1			| 1.31			| 918			| 1			|
| Std128	         	| 1.61			| 19 904		| 1			|
| LIMA-2p	            	| 1.68			| 8 451			| 3			|
| **FireSaber**                	| 1.75			| 2 784			| 5			|
| Hi192		          	| 2.12			| 26 560		| 3			|
| uRound2-LWR2			| 2.51			| 12 841		| 2			|
| uRound2-LWR3			| 2.54			| 12 195		| 3			|
| **HILA5**                    	| 2.89			| 3 836			| 5			|
| Super256		       	| 3.00			| 35 264		| 5			|
| uRound2-LWR5			| 3.92			| 17 389		| 5			|
| lotus128              	| 4.78			| 81 511		| 1			|
| uRound2-LWR4			| 4.87			| 21 761		| 4			|
| NTRU-HRSS	          	| 6.06			| 2 416			|			|
| nRound2-1		     	| 6.78			| 881			| 1			|
| lotus192              	| 8.61			| 137 807		| 3			|
| nRound2-2		   	| 9.97			| 1 133			| 2			|
| nRound2-3		     	| 12.75			| 1 233			| 3			|
| lotus256              	| 15.23			| 199 071		| 5			|
| ntrulpr			| 16.75			| 2 204			| 5			|
| nRound2-4		     	| 17.79			| 1 605			| 4			|
| nRound2-5     		| 17.80			| 1 509			| 5			|
| sntrup		 	| 19.95			| 2 265			| 5			|
| Frodo-640             	| 39.10			| 19 352		| 1			|
| Frodo-976       		| 90.08			| 31 400		| 3			|
| ntru-1024			| 148.77		| 8 194			| 5			|


#### Remarque :

* Les temps sont donnés arrondi au centième. Le script de pqcbench donne des temps beaucoup plus précis, mais cela n'est pas utile pour une simple comparaison, au vu des ordres de grandeurs concernés.
