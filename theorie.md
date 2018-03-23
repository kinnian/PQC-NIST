# Quelques éléments théoriques sur les réseaux

## Intro


## Learning With Errors (LWE)


Pour n q in N, ksi une distribution d'erreurs sur Z, un vecteur s in Zq^n appelé secret, on appelle la distribution LWE l'ensemble des échantillons :

$$(a, b = <s,a> + e \, mod \, q)$$

Le problème computationnel associé est :
    Etant donnés m échantillons (ai,bi), trouver s.


## Ring-LWE


Pour un anneau R de degré n sur Z, un entier q, une distribution d'erreurs sur R et un secret s(x) dans $R_q[x]/\Phi(x)$, la distribution R-LWE est l'ensemble des
échantillons de la forme :
$$(a(x), b(x) = s(x).a(x) + e(x))$$

R-LWE peut être vu comme un cas spécial de LWE avec des échantillons correlés. Ici, ai n'est plus un vecteur de taille n, mais un élément de $R_q[x]/\Phi(x)$.


## Module-LWE



