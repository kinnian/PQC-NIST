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
