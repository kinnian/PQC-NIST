# Protocoles d'encapsulation de clé (KEM)

*Julia Callebat, mars 2018*

Tous les PKE listés précédemment sont dérivés en un KEM dans les soumissions elles-mêmes, et ont donc les mêmes paramètres de base. D'autres soumission
proposent uniquement un KEM :

* CRYSTALS.Kyber, dont la sécurité repose sur la difficulté du MLWE ;
* Ding Key Exchange, basé sur RLWE ;
* EMBLEM et R.EMBLEM, basés respectivement sur LWE et RLWE ; 
* Frodo, basé sur LWE ;
* Hila5, basé sur RLWE ;
* NTRU-HRSS, une variation de NTRUEncrypt avec des paramètres différents ;
* NTRU prime, avec sntrup pour "streamlined NTRU Prime", et ntrulpr pour "NTRU LPRime" ;
* ThreeBears (BabyBear, MamaBear et PapaBear), basé sur LWE.

## Tableau récapitulatif des paramètres

| Protocole     | Sécurité  | N     | Clé privée    | Clé publique  | Chiffré   | Temps total   |
|:------------- |:--------- | -----:| -------------:| -------------:| ---------:| -------------:|
| Kyber512      | 1         | 512   | 1 632         | 736           | 800       | 169           |
| Kyber768      | 3         | 768   | 2 400         | 1 088         | 1 152     | 277           |
| Kyber1024     | 5         | 1024  | 3 168         | 1 440         | 1 504     | 402           |
| Ding512       | 1         | 512   | 1 536         | 1 040         | 1 088     | 4 700         | 
| Ding1024      | 3/5       | 1024  | 3 072         | 2 064         | 2 176     | 9 380         |
| EMBLEM-770    | 1         | 770   | 32            | 12 068        | 18 608    | 27 853        |
| EMBLEM-611    | 1         | 611   | 32            | 10 016        | 14 792    | 20 239        |
| R.EMBLEM-16   | 1         | 512   | 32            | 1 056         | 1 568     | 2 480         |
| R.EMBLEM-14   | 1         | 512   | 32            | 928           | 1 376     | 2 083         |
| Frodo-640     | 1         | 640   | 19 872        | 9 616         | 9 736     | 1 100         |
| Frodo-976     | 3         | 976   | 31 272        | 15 632        | 15 768    | 2 100         |
| Hila5         | 5         | 1024  | 640           | 1 824         | 2 012     | 175           |
| Kindi-256-3   | 2         | 768   | 1 472         | 1 184         | 1 792     | 342           |
| Kindi-512-2   | 4         | 1024  | 1 712         | 1 456         | 2 496     | 399           |
| Kindi-256-5   | 5         | 1280  | 2 304         | 1 984         | 2 688     | 811           |
| Kindi-512-3   | 5         | 1536  | 2 752         | 2 368         | 3 328     | 735           |
| LAC128        | 1, 2      | 512   | 1 056         | 544           | 1 024     | 151           |
| LAC192        | 3, 4      | 1024  | 2 080         | 1 056         | 1 536     | 153           |
| LAC256        | 5         | 1024  | 2 080         | 1 056         | 2 048     | 543           |
| LIMA-2p       | 3         | 1024  | 6 912         | 4 608         | 3 843     | 550           |
| LIMA-2p       | 4         | 2048  | 13 824        | 9 216         | 6 915     | 1 120         |
| LIMA-sp       | 1         | 1018  | 9 162         | 6 108         | 3 825     | 1 350         |
| LIMA-sp       | 2         | 1306  | 12 734        | 8 489         | 6 251     | 2 560         |
| LIMA-sp       | 3         | 1822  | 17 765        | 11 843        | 8 315     | 2 750         |
| LIMA-sp       | 4         | 2062  | 19 332        | 12 888        | 9 275     | 5 120         |
| lotus128      | 1, 2      | 128   | 87 552        | 82 368        | 143       | 6 552         |
| lotus192      | 3, 4      | 192   | 128 125       | 137 625       | 182       | 11 228        |
| lotus256      | 5         | 256   | 183 875       | 198 850       | 221       | 17 452        |
| NewHope512    | 1         | 512   | 1 888         | 928           | 1 120     | 144           |
| NewHope1024   | 5         | 1024  | 3 680         | 1 824         | 2 208     | 303           |
| Lizard-536    | 1         | 536   | 8 608         | 1 130 496     | 17 696    | 76 570        |
| Lizard-816    | 3         | 816   | 19 632        | 1 720 320     | 26 928    | 120 984       |
| Lizard-1088   | 5         | 1088  | 34 880        | 4 587 520     | 35 904    | 308 119       |
| RLizard-1024  | 3         | 1024  | 641           | 4 096         | 4 144     | 684           |
| RLizard-2048  | 5         | 2048  | 769           | 8 192         | 8 256     | 1 231         |
| NTRU-HRSS     | *?*       | 701   | 1 418         | 1 138         | 1 278     | 6 554         |
| ntru-443      | 1         | 443   | 701           | 611           | 611       | 631           |
| ntru-743      | 4         | 743   | 1 173         | 1 023         | 1 023     | 1 367         |
| ntru-1024     | 5         | 1024  | 8 194         | 4 097         | 4 097     | 225           |
| sntrup        | 5         | 761   | 1 600         | 1 218         | 1 047     | > 1 760       |
| ntrulpr       | 5         | 761   | 1 238         | 1 047         | 1 157     | > 1 760       |
| OKCN-MLWE     | 4         | 768   | 288           | 992           | 1 120     | 382           |
| AKCN-MLWE     | 4         | 768   | 288           | 991           | 1 120     | 371           |
| OCKN-RLWE     | 5         | 768   | 1 664         | 1 696         | 1 955     | 594           |
| ACKN-RLWE     | 5         | 768   | 1 664         | 1 696         | 2 083     | 610           |
| uRound2-LWR1  | 1         | 500   | *?*           | 3 455         | 4 837     | 3 000         |
| uRound2-LWR2  | 2         | 580   | *?*           | 6 413         | 6 428     | 5 700         |
| uRound2-LWR3  | 3         | 630   | *?*           | 5 223         | 6 972     | 5 800         |
| uRound2-LWR4  | 4         | 786   | *?*           | 10 857        | 10 904    | 8 900         |
| uRound2-LWR5  | 5         | 786   | *?*           | 8 679         | 8 710     | 7 600         |
| uRound2-RLWR1 | 1         | 418   | *?*           | 435           | 482       | 300           |
| uRound2-RLWR2 | 2         | 522   | *?*           | 555           | 618       | 400           |
| uRound2-RLWR3 | 3         | 540   | *?*           | 565           | 636       | 400           |
| uRound2-RLWR4 | 4         | 700   | *?*           | 749           | 940       | 600           |
| uRound2-RLWR5 | 5         | 676   | *?*           | 709           | 858       | 600           |
| nRound2-1     | 1         | 400   | *?*           | 417           | 464       | 8 200         |
| nRound2-2     | 2         | 486   | *?*           | 519           | 614       | 12 100        |
| nRound2-3     | 3         | 556   | *?*           | 581           | 652       | 15 700        |
| nRound2-4     | 4         | 658   | *?*           | 707           | 898       | 21 800        |
| nRound2-5     | 5         | 658   | *?*           | 691           | 818       | 21 800        |
| LightSaber    | 1         | 512   | 992           | 672           | 736       | 191           |
| Saber         | 3         | 768   | 1 344         | 992           | 1 088     | 309           |
| FireSaber     | 5         | 1024  | 1 760         | 1 312         | 1 472     | 475           |
| BabyBear      | 2         | 624   | 40            | 804           | 917       | 88            |
| MamaBear      | 4, 5      | 938   | 40            | 1 194         | 1 307     | 143           |
| PapaBear      | 5         | 1248  | 40            | 1 584         | 1 697     | 207           |
| Std128        | 1         | 1024  | 16 384        | 16 352        | 3 552     | 1 362         |
| Hi192         | 3         | 1536  | 20 544        | 20 512        | 6 048     | 1 813         |
| Super256      | 5         | 2048  | 26 944        | 26 912        | 8 352     | 2 540         |




#### Remarques

* Pour EMBLEM et R.EMBLEM, de nombreux autres ensembles de paramètres sont donnés ; j'ai choisi de garder uniquement ceux qui minimise la taille combiné de la
  clé publique et du chiffré.

* La taille de la clé privée de Hila5 est donnée après compression.

* De même que pour le PKE, la documentation de LOTUS n'est pas très précise sur les unités ; je ne garanti pas l'exactitude des résultats reportés ici.

* Pour Lizard, j'ai choisi un seul des deux instances proposées par niveau de sécurité - celle avec les plus petits paramètres.

* La documentation de NTRU prime donne des ordres de grandeurs pour certaines mesures de temps ; il s'agit donc d'approximations.
* Pour ThreeBears, j'ai choisi le temps d'exécution de la version CCA-secure ; ceux de la version CPA-secure sont plus petits.
