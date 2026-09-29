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

## B — Oxydation de l’alcool dans le sang

Une fois que l’alcool est passé dans le sang, il est progressivement éliminé, principalement au niveau du foie, par une réaction d’oxydation qui le transforme en éthanal. Cette réaction est catalysée par une enzyme appelée alcool-déshydrogénase. Pour déterminer la loi de vitesse de cette réaction, on injecte directement par voie veineuse une certaine quantité d’alcool dans le sang d’un homme, puis on mesure par des prélèvements successifs l’évolution de la concentration $c_2$ de l’alcool dans le sang. On suppose que l’injection est quasi-instantanée et que la concentration d’alcool est la même en tout point du corps.

| $t$ (min) | 0 | 120 | 240 | 360 | 480 | 600 | 720 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $c_2$ (mol·L$^{-1}$) | 0,0500 | 0,0413 | 0,0326 | 0,0239 | 0,0152 | 0,0065 | 0 |

**Question 3.** À l’aide de ces données, déterminer l’ordre de la réaction ainsi que sa constante de vitesse $k_2$.

> **Remarque :** on peut comparer l’évolution expérimentale de $c_2$ avec les lois intégrées correspondant aux différents ordres de réaction.

**Question 4.** Calculer, en minutes, le temps de demi-réaction $t_{1/2,2}$ de cette réaction et le comparer au temps de demi-réaction de l’absorption de l’alcool $t_{1/2,1}$.

> **Remarque :** le temps de demi-réaction est le temps nécessaire pour que la concentration atteigne la moitié de sa valeur initiale. Pour une réaction d’ordre 0, il dépend de la concentration initiale.

## C — Évolution de l’alcoolémie au cours du temps

Maintenant que l’on connaît les lois de vitesse de la réaction d’absorption et de la réaction d’élimination de l’alcool, on peut étudier l’évolution de l’alcoolémie au cours du temps à partir du moment où une personne boit de l’alcool. On note $c$ la concentration d’alcool dans le sang, en mol·L$^{-1}$, $v=\frac{dc}{dt}$ la vitesse de variation de cette concentration, $V_s$ le volume total du sang et des compartiments hydriques de l’organisme dans lesquels se dissout l’alcool, et $V_e$ le volume de boisson alcoolisée ingérée. On considère que la personne était à jeun avant de boire.

La concentration d’alcool dans le sang à l’instant $t$ est donnée par :

$$
c(t)=C_0\frac{V_e}{V_s}(1-e^{-k_1t})-k_2t
$$

où $C_0$ est la concentration en alcool dans la boisson.

Lors d’une soirée, Alice boit deux bières de volume $V_0=50\,\mathrm{cL}$ chacune et de degré alcoolique $d=6\%$. Le degré alcoolique correspond au pourcentage volumique d’éthanol dans la boisson :

$$
d=\frac{V_{\mathrm{éthanol}}}{V_{\mathrm{total}}}
$$

**Question 5.** Sachant que l’éthanol a une masse volumique $\rho_{\mathrm{eth}}=0,79\,\mathrm{kg\,L^{-1}}$, calculer la concentration $C_0$ d’éthanol dans la bière, en g·L$^{-1}$ puis en mol·L$^{-1}$. On donne $M_C=12\,\mathrm{g\,mol^{-1}}$, $M_H=1,0\,\mathrm{g\,mol^{-1}}$ et $M_O=16\,\mathrm{g\,mol^{-1}}$.

> **Remarque :** la formule de l’éthanol est $C_2H_6O$. Il faut d’abord calculer sa masse molaire, puis utiliser le degré alcoolique.

**Question 6.** Tracer la fonction

$$
c(t)=C_0\frac{V_e}{V_s}(1-e^{-k_1t})-k_2t
$$

représentant l’évolution de la concentration en éthanol dans le sang d’Alice, en mol·L$^{-1}$, à partir du moment où elle boit ses deux bières. On prendra $V_s=40\,\mathrm{L}$.

> **Remarque :** la courbe doit d’abord augmenter sous l’effet de l’absorption, atteindre un maximum, puis diminuer sous l’effet de l’élimination.

**Question 7.** Déterminer la valeur maximale $c_{\max}$ de la concentration en éthanol dans le sang d’Alice.

> **Remarque :** le maximum correspond au sommet de la courbe.

**Question 8.** Déterminer l’instant $t_{\max}$ auquel la concentration en éthanol est maximale dans le sang d’Alice.

> **Remarque :** au maximum, on a $\frac{dc}{dt}=0$.

**Question 9.** Alice a-t-elle le droit de conduire à cet instant ?

> **Remarque :** comparer l’alcoolémie maximale obtenue avec la limite légale donnée dans l’exercice, en veillant à utiliser les mêmes unités.

**Question 10.** Déterminer le temps au bout duquel Alice aura le droit de prendre le volant.

> **Remarque :** il faut déterminer l’instant où, après le maximum, l’alcoolémie redescend sous la limite légale en résolvant :

$$
c(t)=c_{\mathrm{limite}}
$$

