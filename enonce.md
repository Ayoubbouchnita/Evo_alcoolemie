Enoncé exo 8:
Partie A:
## A — Absorption de l’alcool à travers la paroi stomacale

On cherche à étudier la loi cinétique modélisant le processus d’absorption de l’alcool, c’est-à-dire à déterminer son ordre ainsi que sa constante de vitesse $k_1$.

Pour cela, on réalise l’expérience suivante : on fait boire à un homme initialement à jeun, c’est-à-dire l’estomac vide, une boisson alcoolisée de volume $V=250\,\mathrm{mL}$ contenant $1$ mole d’éthanol. On mesure ensuite la concentration $c_1$ de l’éthanol dans l’estomac en fonction du temps.

Les résultats obtenus sont regroupés dans le tableau suivant :

| $t$ (min) | 0 | 1,73 | 2,8 | 5,5 | 18 | 22 |
|---|---:|---:|---:|---:|---:|---:|
| $c_1$ (mol·L$^{-1}$) | à déterminer | 3,0 | 2,5 | 1,6 | 0,2 | 0,1 |

**Question 1.** Utiliser ces données pour prouver graphiquement que la réaction d’absorption de l’alcool dans le sang suit une loi cinétique d’ordre $1$, et déterminer sa constante de vitesse $k_1$, en précisant son unité.

> **Remarque :** pour vérifier graphiquement une cinétique d’ordre 1, on peut représenter $\ln\left(\frac{c_1(t)}{c_{1,0}}\right)$ en fonction du temps $t$. Si les points sont alignés sur une droite, la réaction suit une loi d’ordre 1. La pente de cette droite vaut $-k_1$. On utilisera la fonction `linregress` du sous-module `stats` de SciPy pour effectuer la régression linéaire.

### Rappel

On note $c_1(t)$ la concentration de l’alcool dans l’estomac au cours du temps et :

$$
v_1=-\frac{dc_1}{dt}
$$

la vitesse d’absorption de l’alcool au niveau de la paroi de l’estomac.

Si la réaction est d’ordre 1, on a :

$$
v_1=k_1c_1(t)
$$

et $c_1(t)$ est solution de l’équation différentielle :

$$
\frac{dc_1(t)}{dt}+k_1c_1(t)=0
$$

qui se résout en :

$$
c_1(t)=c_{1,0}e^{-k_1t}
$$

où $c_{1,0}$ est la concentration initiale.

Ainsi, si la réaction est bien d’ordre 1 :

$$
\ln\left(\frac{c_1(t)}{c_{1,0}}\right)=-k_1t
$$

**Question 2.** Calculer, en minutes, le temps de demi-réaction $t_{1/2,1}$ de la réaction d’absorption de l’alcool dans le sang.

> **Remarque :** pour une réaction d’ordre 1, le temps de demi-réaction est donné par :

$$
t_{1/2,1}=\frac{\ln 2}{k_1}
$$

> Il suffit donc d’utiliser la valeur de $k_1$ obtenue à la question 1.
