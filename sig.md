# Protocoles de signature 

*Julia Callebat, mars 2018*



J'ai trouvé plusieurs soumissions de protocoles de signature qui utilise des algorithmes à base de réseaux, et plus précisemment des variantes de NTRU ou LWE :

* CRYSTALS-Dilithium, qui se base sur la sécurité de MLWE ;
* Falcon, basé sur NTRU ;
* pqNTRUSign (Gaussian-1024, Uniform-1024), basé sur NTRU ;
* qTesla, basé sur Ring-LWE.

## Tableau récapitulatif des paramètres 

Les tailles sont en octets, et les temps en microsecondes.

| Protocole     | Niveau de sécurité	| N 	| Clé publique	| Signature	| Temps de calcul	|
|:-----------   |:------------------	| ---:	| ------------: | ---------:    | ---------------:  	|
| Dilithium-2	| 1		 	| 768	| 1 184         | 2 044      	| 529.2             	|
| Dilithium-3   | 2			| 1024  | 1 472         | 2 701      	| 741.9             	|
| Dilithium-4   | 3			| 1280  | 1 760         | 3 366      	| 782.4             	|
| Falcon-512    | 1			| 512   | 897           | 617.38    	| 6 980              	|
| Falcon-768    | 2, 3			| 768   | 1 441         | 993.91    	| 12 690		|
| Falcon-1024   | 4, 5			| 1024  | 1 793         | 1 233.29   	| 19 640		|
| Gaussian-1024 | 5 			| 1024	| 2 065		| 2 065		| 16 8760		|
| Uniform-1024	| 5			| 1024	| 2 065		| 2 065		| 12 1870		|
| qTesla-128    | 1			| 1024  | 4 128         | 2 112		| 2.67              	| 
| qTesla-192    | 3			| 2048  | 8 224         | 6 176		| 6.9               	|
| qTesla-256    | 5			| 2048  | 8 224         | 6 175		| 21.2              	|


#### Remarques

* Falcon donne des signatures approximées car il s'agit d'une moyenne, les variations étant dûe à la compression variable de la signature.

* Apparemment les demandes du NIST excluait l'utilisation d'optimisations liées à AVX2 ; certains papiers ont malgré tout fait cette optimisation, mais je
  ne l'ai pas prise en compte.

* qTesla donne dans sa documentation des valeurs théoriques et les valeurs qu'ils ont eu en pratique lors de l'implémentation. J'ai décidé de garder les
  valeurs expérimentales, qui reflètent à mon sens mieux l'efficacité réelle de ce protocole.
