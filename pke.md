# Protocoles de chiffrement à clé publique (PKE)

*Julia Callebat, mars 2018*

Il y a de nombreux protocoles PKE qui ont été soumis :

* Compact-LWE, basé sur LWE ;
* Kindi, basé sur RLWE ;
* LAC, basé sur RLWE ;
* LIMA, basé sur RLWE, avec deux contraintes différentes pour p : power-of-two (2p) ou safe-prime (sp) ;
* LOTUS, basé sur LWE ;
* NewHope, basé sur RLWE ;
* Lizard, basé sur LWE, et RLizard, sur RLWE ;
* NTRUEncrypt, basé sur NTRU ;
* OKCN-AKCN, basé sur LWE ;
* Round2, avec uRound2 (u pour "unified set of parameters") basé sur LWR et RLWR, et nRound2 (n pour "NTT friendly"), basé sur LWR ;
* Saber, basé sur LWR ;
* Titanium (Std128, Hi192, Super256), basé sur LWE.

## Tableau récapitulatif des paramètres

Les tailles sont en octets, les temps en microsecondes.


| Protocole     | Sécurité  | N	    | Clé privée	| Clé publique	| Chiffré	    | Temps total   | 
|:-------------	|:----------| -----:| -------------:| -------------:| -------------:| -------------:|
| Compact-LWE	| 3		    | 8	    | 232		    | 2 064		    | 9 288		    | 3 225         | 
| Kindi-256-3   | 2         | 768   | 1 472         | 1 184         | 1 792         | 331           |
| Kindi-512-2   | 4         | 1024  | 1 712         | 1 184         | 1 792         | 379           |
| Kindi-256-5   | 5         | 1280  | 2 304         | 1 728         | 2 688         | 789           |
| Kindi-512-3   | 5         | 1536  | 2 752         | 2 368         | 3 328         | 709           |
| LAC128        | 1,2       | 512   | 1 056         | 544           | 1 024         | 100           |
| LAC192        | 3,4       | 1024  | 2 080         | 1 056         | 1 636         | 309           |
| LAC256        | 5         | 1024  | 2 080         | 1 056         | 2 048         | 361           |
| LIMA-2p-1024  | 3         | 1024  | 6 912         | 4 608         | 4 611         | 550           |
| LIMA-2p-2048  | 4         | 2048  | 13 824        | 9 216         | 7 683         | 1 120         |
| LIMA-sp-1018  | 1         | 1018  | 9 162         | 6 108         | 4 593         | 1 350         |
| LIMA-sp-1306  | 2         | 1306  | 12 734        | 8 489         | 7 275         | 2 570         |
| LIMA-sp-1822  | 3         | 1822  | 17 765        | 11 843        | 9 339         | 2 750         |
| LIMA-sp-2062  | 4         | 2062  | 19 332        | 12 888        | 10 299        | 5 120         |
| lotus128      | 1,2       | 576   | 700 420       | 658 950       | c + 1 144     | 6 552         |
| lotus192      | 3,4       | 704   | 1 101 000     | 1 025 000     | c + 1 768     | 11 354        |
| lotus256      | 5         | 832   | 1 590 800     | 1 471 000     | c + 1 768     | 17 556        |
| Lizard-536    | 1         | 536   | 137 216       | 1 622 016     | 1 648         | 156 385       |
| Lizard-816    | 3         | 816   | 313 344       | 2 457 600     | 2 496         | 250 671       |
| Lizard-1088   | 5         | 1088  | 557 056       | 6 553 600     | 3 328         | 664 027       |
| RLizard-1024  | 3         | 1024  | 513           | 4 096         | 4 272         | 645           |
| RLizard       | 5         | *?*   | 513           | 8 192         | 8 512         | 1 163         |
| ntru-443      | 1         | 443   | 701           | 611           | 611           | 663           |
| ntru-743      | 4         | 743   | 1 173         | 1 023         | 1 023         | 1 306         |
| ntru-1024     | 5         | 1024  | 8 194         | 4 097         | 4 097         | 225           |
| okcn-akcn     | 4         | 768   | 1 312         | 992           | (msg) + 1 168 | 1 374         |
| uRound2-LWR-1 | 1         | 500   | *?*           | 3 455         | (msg) + 4 881 | 6 600         |
| uRound2-LWR-2 | 2         | 585   | *?*           | 6 468         | (msg) + 6 567 | 8 700         |
| uRound2-LWR-3 | 3         | 643   | *?*           | 5 330         | (msg) + 7 185 | 9 000         |
| uRound2-LWR-4 | 4		    | 835	| *?*		    | 12 574	    | (msg) + 12 673| 14 600	    |
| uRound2-LWR-5	| 5		    | 835	| *?*		    | 10 053	    | (msg) + 10 128| 12 600	    |
| uRound2-RLWR-1| 1		    | 420	| *?*		    | 437		    | (msg) + 560	| 400		    |
| uRound2-RLWR-2| 2		    | 540	| *?*		    | 641		    | (msg) + 764	| 700		    |
| uRound2-RLWR-3| 3		    | 586	| *?*		    | 685		    | (msg) + 784	| 700		    |
| uRound2-RLWR-4| 4		    | 708	| *?*		    | 846		    | (msg) + 1 017	| 1 000		    |
| uRound2-RLWR-5| 5		    | 708	| *?*		    | 830		    | (msg) + 953	| 1 000		    |
| nRound2-1	    | 1		    | 442	| *?*		    | 515		    | (msg) + 622	| 15 000	    |
| nRound2-2	    | 2		    | 556	| *?*		    | 659		    | (msg) + 846	| 23 400	    |
| nRound2-3	    | 3		    | 576	| *?*		    | 673		    | (msg) + 820	| 25 100	    |
| nRound2-4	    | 4		    | 708	| *?*		    | 846		    | (msg) + 1 113 | 36 000	    |
| nRound2-5	    | 5		    | 708	| *?*		    | 830		    | (msg) + 1 017	| 35 800	    |
| LightSaber    | 1         | 512   | 256           | 672           | 736           | *?*           |
| Saber         | 3         | 768   | 288           | 992           | 1 088         | *?*           |
| FireSaber     | 5         | 1024  | 384           | 1 312         | 1 472         | *?*           |
| Std128        | 1         | 1024  | 16 384        | 16 352        | 3 552         | 948           |
| Hi192         | 3         | 1536  | 20 544        | 20 512        | 6 048         | 1 812         |
| Super256      | 5         | 2048  | 26 944        | 26 912        | 8 352         | 2 540         |

#### Remarques

* La documentation de Compact-LWE donne des résultats pour différentes tailles de messages. J'ai choisi de ne garder que les données pour un message de 1024 octets.

* Pour la soumission Lima, les tailles de clés publique et privées sont données avec et sans compression, et avec un encodage de Huffman ; c'est les
  valeurs de ce dernier cas que j'ai gardé. De même pour le chiffré, les valeurs sont données selon que la sécurité garantie est CCA ou CPA, avec des
  tailles non compressées et compressées. J'ai décidé de garder les valeurs du cas CCA compresssé. De même pour les temps d'exécutions, plusieurs valeurs
  sont données. J'ai gardé celles du cas CCA sur le processeur le plus performant des 4 donnés.

* La documentation pour LOTUS n'est pas très claire sur les unités utilisées, et ne précisent pas la valeur de c, la taille de la "clé symmétrique". Il y a
  donc potentiellement des erreurs d'ordre de grandeur pour les paramètres dans le tableau pour lotus128, lotus192 et lotus256.

* La soumission NewHope n'utilise son protocole PKE uniquement comme partie d'un KEM, et déconseille l'utilisation du PKE seul, en partie car il n'accepte pas de message de taille arbitraire. Il n'est donc pas présent dans ce tableau des paramètres des PKE.

* Pour Lizard et RLizard, certaines configurations de paramètres sont omises ; elles ont les mêmes ordres de grandeur de performance.  A noter aussi que la
  taille des messages chiffrés n'est pas exactement la même entre plusieurs niveaux de sécurité (32 octets pour sécurité 1, 48 pour 3 et 64 pour 5).

* NTRUEncrypt donne deux fichiers de résultats différents, avec des valeurs un peu différentes entre les deux, mais les ordres de grandeur reste
  sensiblement les mêmes.

* La soumission OKCN-AKCN donne les temps d'exécutions pour différentes tailles de messages (de 32 à 20000 octets) ; j'ai conservé celle pour 20000 octets.

* La soumission Saber donne la taille de la clé secrète non compressée et compressée ; j'ai gardé la valeur compressée.

* Titanium donne les valeurs pour une sécurité CPA et CCA ; j'ai gardé celles de CCA.
