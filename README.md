# PQC-NIST
Etat de l'art des soumissions PQC du NIST utilisant LWE, NTRU ou des variantes

## Résumé des soumissions

Les différentes soumissions PQC du NIST qui utilisent comme primitive LWE, NTRU ou des variantes, ont été triées en fonction de leur but.

* Le fichier `sig.md` propose un aperçu des soumissions de protocoles de signature (SIG), et de leurs paramètres.

* Le fichier `pke.md` propose un aperçu des soumissions de protocoles d'échange à clé publique (PKE), et de leurs paramètres.

* Le fichier `kem.md` propose un aperçu des soumissions de protocoles d'échange de clé (KEM), et de leurs paramètres.

Pour chacune des soumissions, un ou plusieurs protocoles ont été choisis, en fonction de leur pertinence ; certaines soumission proposant une dizaine de protocoles semblables, mais aux paramètres et caractéristiques différentes, il était nécessaire de faire un choix.
Les paramètres les plus importants sont les différentes tailles de clés, chiffrés ou signatures instanciés par ces protocoles, ainsi que le temps d'exécution du protocole entier (génération, échanges, vérifications éventuelles), et le niveau de sécurité tel que défini par le NIST (voir [Call for proposals](https://csrc.nist.gov/CSRC/media/Projects/Post-Quantum-Cryptography/documents/call-for-proposals-final-dec-2016.pdf) ).
A noter que, chaque soumission ayant été construite est testée sur des machines différentes -- dont on peut retrouver les caractéristiques précises dans les dossiers de soumission au NIST [ici](https://csrc.nist.gov/projects/post-quantum-cryptography/round-1-submissions "Round 1 soumissions") -- les temps notés sont ceux de la machine de l'équipe qui a soumis le protocole. Cependant, comme les différentes machines ont des caractéristiques similaires, et que NIST a demandé explicitement que soient donnés des implémentations qui ne contiennent pas d'optimisation dépendant de la machine, on peut considérer la comparaison des temps d'exécution entre deux protocoles -- et donc entre deux machines -- comme raisonnable.


## Tests des implémentations soumises

A la suite de cet état de l'art, 12 protocoles de KEM ont été sélectionnés selon les critères suivants -- par ordre d'importance :
1. Niveau de sécurité 5 (le plus élevé)
2. Tailles des clés et du chiffré relativement petites
3. Temps d'exécution relativement faible

Les protocoles choisis sont les suivants :
* Kyber1024
* Hila5
* Kindi-{256-5, 512-3}
* LAC256
* NewHope1024
* {A,O}KCN-RLWE
* uRound2-RLWR5
* FireSaber
* {Mama,Papa}Bear

Dans le dossier de [tests](./Tests/) se trouvent :
* Les versions standards (`std`) et optimisées (`opt`) de chaque protocole choisi ;
* Des fonctions python permettant d'effectuer des tests de tailles de clés, chiffrés et secrets communs, et de vitesse d'exécution sur la machine courante ;
* Un deuxième [README](./Tests/README.md) expliquant comment utiliser ces fonctions.
* Un [compte-rendu](.Tests/CR.md) des tests effectués.
