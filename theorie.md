# Eléments théoriques des réseaux pour la cryptographie

## Introduction
### Définition des réseaux

Un réseau L est l'ensemble généré par toutes les combinaisons linéaires d'un ensemble de n vecteurs de taille m. On considère en général des réseaux de rang
plein, c'est-à-dire tels que le rang n est égal à la dimension m. Un réseau est en général caractérisé par une matrice de base, matrice mxn dont les lignes sont les
vecteurs générateurs du réseau. 

En cryptographie, on travaille généralement avec des vecteurs d'entiers.

### Problèmes sur les réseaux

Il existe plusieurs problèmes décisionnels sur réseaux. Le plus couramment utilisé est le *Closest Vector Problem*, CVP, défini comme suit :

	Etant donnés une matrice de base B d'un résea L et un vecteur w à coefficients rationnels, trouver un vecteur v de L qui minimise la distance ||w - v||.

Il s'agit d'un problème NP-difficile. En revanche, en possession d'une "bonne" base du réseau, c'est-à-dire d'une base de vecteurs assez courts et
quasiment orthogonaux, ce problème devient plus facile. Il existe plusieurs algorithmes de réduction de réseau qui, étant donnés une matrice de base
quelconque, donnent une "bonne" matrice de base ; le plus connu est l'algorithme de Lenstra–Lenstra–Lovász (LLL). Il est possible de se protéger de tels
algorithmes en choisissant un réseau de dimension assez grande. En effet, avec les notations précédentes, LLL est de complexité O(n.m^5).

Il est donc possible d'utiliser la difficulté de ce problème en utilisant une "bonne" base comme clé secrète, et un vecteur à coefficiants rationnels
comme chiffré, construit tel que retrouvé le message revienne à résoudre le CVP. L'un des premiers cryptosystèmes utilisant ce principe est celui de
Goldreich-Goldwasser-Halevi (GGH).

Il existe une variante du CVP, aussi utilisée en cryptographie, appelée *Bounded Distance Decoding* (BDD). Il s'agit de même de trouver un vecteur v d'un
réseau L le plus proche d'un autre vecteur quelconque w, mais cette fois-ci avec la condition que le vecteur w soit proche à un facteur d'approximation
près du réseau.


## Cryptosystèmes sur réseaux
### NTRU

Il s'agit d'une variante de GGH, qui utilise des anneaux polynomiaux de la forme R = Z[X]/(X^N - 1). R peut alors être vu comme un réseau algébraiquement
structurés. Les autres paramètres sont les suivants :

* un entier impair q, qui défini Rq = R/q.R, qui peut être vu comme une "mauvaise" base du réseau ;
* une clé secrète s de R, inversible modulo p et q, et avec des coefficients "petits" (en général dans {-1, 0, 1}) ;
* une clé publique h = pg.s^(-1) dans Rq, avec g un polynôme de R de coefficients "petits" ;
* un facteur "aveuglant" r de R, qui doit être gardé secret ;
* un terme d'erreur e de R court, qui encode les bits de message sur ses coefficients modulo p.

Le mot-code est alors c = h.r + e, un élément de Rq. 

Pour récupérer le message, on le multiplie par le secret s, et on obtient pg.r + e.s dans Rq, que l'on interprète comme un élément court de R ; modulo p,
on retrouve e.s, d'où il est facile de retrouver e et donc l'information.

Pour N, q et p choisis convenablement, ainsi que les polynômes s et g choisis avec un grand nombre de coefficients non-nuls, ce système résiste à la
plupart des attaques connues. De plus, les clés sont compactes et les calculs efficaces, ce qui en fait un bon protocole de chiffrement.


### Learning With Errors (LWE)


Pour n q in N, X une distribution d'erreurs sur Z, un vecteur s in (Zq)^n appelé secret, on appelle la distribution LWE l'ensemble des échantillons :

	(a, b = \<s,a\> + e mod q)

Les a sont choisis de manière uniformément aléatoire sur (Zq)^n.

Le problème computationnel associé est :

	Etant donnés m échantillons (ai,bi), trouver s.

On considère en général les m échantillons comme un matrice A de taille nxm dans Zq, de colonnes les ai, et un vecteur b de taille m de coefficients bi. Le
problème computationnel peut alors être vu comme un CVP : le vecteur b est proche de exactement un vecteur du réseau L(A) := {A's : s dans (Zq)^n} + q.Z^m,
avec A' la matrice transposée de A. Il s'agit donc aussi d'un problème difficile à résoudre sans avoir accès au secret s.


### Ring-LWE


Il s'agit d'une variante du problème précédent où Zq est remplacé par un anneau Rq (généralement de la forme Zq[x]/f(x), avec f(x) un polynôme). On a alors
une distribution d'échantillons de la forme :

	(a(x), b(x) = s(x).a(x) + e(x))

où a(x), s(x) et e(x) sont des polynômes de Rq, s étant le secret et e des "erreurs" choisies selon une distribution de probabilité R. Ici encore, a est
choisi de manière uniformément aléatoire sur Rq.

R-LWE peut être vu comme un cas spécial de LWE avec des échantillons correlés. Ici, ai n'est plus un vecteur de taille n, mais un élément de Rq.


### Module-LWE


RLWE est préférable au LWE standard sur bien des aspects : les tailles de clés et de chiffrés sont significativement plus petites, et les temps d'exécution
plus petit, notamment grâce à des méthodes optimisées de multiplication de polynôme (NTT, ...). En revanche, un inconvéniant de RLWE est qu'il introduit
plus de structure dans les réseaux générés par le problème, ce qui pourrait être utilisé pour attaquer plus efficacement ce chiffrement. Un compromis a été
trouvé dans le Module-LWE, qui se base sur des modules d'un anneau cyclotomique. 

On se place dans un module de taille k de Rq, anneau tel que défini pour RLWE, et on construit de même que précédemment des échantillons générés
aléatoirement, avec s le secret, e des erreurs générés selon une distribution de probabilité, et a choisi de manière uniformément aléatoire, des vecteurs de taille k dans Rq :

	(a, b = \<s,a\> + e)


### Learning With Roundings (LWR)


Le problème LWR est très similaire à LWE ; le problème décisionnel revient ici encore à retrouver un secret s de (Zq)^n à partir d'un ensemble d'échantillons
aléatoires construits en utilisant s. La différence est que ici, au lieu d'ajouter des erreurs aléatoires pour rendre les attaques plus difficiles, les
échantillons sont arrondis de manière déterministe. On a donc :

	(a, b = round(\<s,a\>))

avec a dans (Zq)^n et round() une fonction d'arrondissement à un entier modulo q déterministe. 

## Construction d'un protocole d'échange de clé "à la Diffie-Helmman"
### Chiffrement classique

Que ce soit en LWE classique, RLWE ou MLWE, le principe de chiffrement est généralement similaire. Considérons le cas LWE, qui s'adapte facilement aux autre paramétrisations.

La clé publique est composée d'une matrice A de taille n sur n, dont chaque ligne est un vecteur a échantilloné selon la distribution considérée, et du vecteur B de taille n tel que B = A.S + E, avec E un vecteur d'erreur. Chaque ligne de B contient effectivement un échantillon du type \<a,s\> + e. La clé privée est alors constituée uniquement du vecteur secret S.

Pour chiffrer un bit d'information m, on calcule le vecteur U = S'.A + E' et l'entier v = S'.B + e + m.[q/2], avec [q/2] l'entier arrondi au supérieur de q/2. Les vecteurs S' et E' et l'entier e sont choisis selon la distribution considérée.

Pour déchiffrer (U,v) à l'aide de la clé secrète S, il faut calculer l'entier v -U.S et déterminer s'il est plus proche de 0 ou de q/2 - et donc si le bit chiffré était égal à respectivement 0 ou 1. En effet, comme B = A.S + E, l'entier calculé précédemment est égal à :

	v - U.S = S'.A.S + S'.E + e + m.[q/2] - S'.A.S - S'.E' ~ m.[q/2]


La distribution des erreurs E, E' et e et des secrets S et S' étant choisie spécifiquement de manière à ce que ces vecteurs et leurs produits restent courts, le déchiffrement est le plus souvent correct. En pratique, le cas d'échec, qui correspond au cas où la valeur (S'.E + e - S'.E') est supérieur à q/4, est très rare. Dans toutes les soumissions de type LWE proposées au NIST, le taux d'erreurs est toujours plus petit que 10^(-50), et est en général de l'ordre de 10^(-100) voire encore plus petit.


### Variations

Les variations les plus courantes, que ce soit dans la version LWE "de base" décrite précédemment ou des versions modulaire ou sur anneaux qui en découlent, consistent simplement en une légère modification de la méthode d'encodage de l'information m. Certaines soumissions, notamment celles sur anneaux, encodent plus d'un seul bit à la fois, et effectuent donc des opérations proche d'une multiplication de chaque coefficient du polynôme par [q/2] ; certaines soumissions effectuent en plus de cette multiplication une troncature des bits les moins significatifs ; certaines, qui placent leurs mots codes dans un espace particulier - notamment, encore une fois en RLWE, pour pouvoir effectuer des *NTT* -, encodent donc aussi le message dans cet espace.

Une variante un peu plus intéressante est présente dans la soumission **Kindi**. Comme ils utilisent une clé publique munie d'une fonction gadget qui permet de récupérer aussi les erreurs E' et e, l'information est encodée directement dans ces erreurs. En pratique, ils effectuent un XOR de l'erreur obtenue aléatoirement et du message à chiffré. 


**Compact-LWE** en revanche varie beaucoup du chiffrement "classique", dont il s'inspire. Cette soumission propose des échantillons "doubles" de LWE, de la forme suivante :

	(ai, \<ai,s\> + k.(ri + p.ei) mod q, \<ai,s'\> + k'.(ri' + p* ei') mod q)

Ceci leur permet d'obtenir une méthode de chiffrement plus compacte (comme l'indique le nom), avec des tailles de clés et d'espace plus petites, au prix de calculs plus compliqués.

### Méthode de réconciliation de clé de Peikert

Dans le contexte proposé par le NIST d'un KEM, key exchange mechanism, il est possible d'adapter cette méthode de chiffrement pour un déduire une méthode d'échange de clé par réconciliation, décrit pour la première fois par Peikert. Ce KEM repose sur le fait que les quantités définies précédemment v et U.S sont très proches. Il suffit donc à Alice et Bob d'effectuer un chiffrement classique, avec m = 0, pour que chacun se retrouve en possession d'une clé qui est, à des termes d'erreurs très faibles près, identique.
