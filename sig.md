# Protocoles de signature utilisant 

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
| Dilithium-2	| 1		 	| 768	| 1184          | 2044      	| 529.2             	|
| Dilithium-3   | 2			| 1024  | 1472          | 2701      	| 741.9             	|
| Dilithium-4   | 3			| 1280  | 1760          | 3366      	| 782.4             	|
| Falcon-512    | 1			| 512   | 897           | 617.38    	| 6980              	|
| Falcon-768    | 2, 3			| 768   | 1441          | 993.91    	| 12690			|
| Falcon-1024   | 4, 5			| 1024  | 1793          | 1233.29   	| 19640			|
| Gaussian-1024 | 5 			| 1024	| 2065		| 2065		| 168760		|
| Uniform-1024	| 5			| 1024	| 2065		| 2065		| 121870		|
| qTesla-128    | 1			| 1024  | 4128          | 2112		| 2.67              	| 
| qTesla-192    | 3			| 2048  | 8224          | 6176		| 6.9               	|
| qTesla-256    | 5			| 2048  | 8224          | 6175		| 21.2              	|


#### Remarques

* Falcon donne des signatures approximées car il s'agit d'une moyenne, les variations étant dûe à la compression variable de la signature.
* Apparemment les demandes du NIST excluait l'utilisation d'optimisations liées à AVX2 ; certains papiers ont malgré tout fait cette optimisation, mais je
  ne l'ai pas prise en compte.
* qTesla donne dans sa documentation des valeurs théoriques et les valeurs qu'ils ont eu en pratique lors de l'implémentation. J'ai décidé de garder les
  valeurs expérimentales, qui reflètent à mon sens mieux l'efficacité réelle de ce protocole.
