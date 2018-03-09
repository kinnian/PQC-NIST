# Protocoles de chiffrement à clé publique (PKE)

*Julia Callebat, mars 2018*

Il y a de nombreux protocoles PKE qui ont été soumis :

* Compact-LWE
* EMBLEM et R.EMBLEM
* Kindi
* LAC
* LIMA
* LOTUS
* NewHope
* Lizard
* NTRU-HRSS
* NTRUEncrypt
* OKCN-AKCN
* Round2
* Saber
* Titanium

## Tableau récapitulatif des paramètres

Les tailles sont en octets, les temps en microsecondes.


| Protocole	| Sécurité	| N	| Clé privée	| Clé publique	| Chiffré	| 
|:-------------	|:-------------	| -----:| -------------:| -------------:| -------------:|
| Compact-LWE	| 3		| 8	| 232		| 2064		| 9288		| 
| EMBLEM	| 1		| 770	| 32		| 3041		| 74048		|
| R.EMBLEM	| 1		| 463	| 32		| 958		| 1470		|
 


#### Remarques

* La documentation de Compact-LWE donne des résultats pour différentes tailles de messages. J'ai choisi de ne garder que les données pour un message de 1024 octets.
