import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# =========================
# QUESTION 1
# Absorption de l'alcool
# =========================

# Données expérimentales
t1 = np.array([1.73, 2.8, 5.5, 18, 22])  # min
c1 = np.array([3.0, 2.5, 1.6, 0.2, 0.1])  # mol/L

# Concentration initiale :
# 1 mole dans 0.250 L
c10 = 1 / 0.250

print("c1,0 =", c10, "mol/L")

# Pour une cinétique d'ordre 1 :
# ln(c1/c10) = -k1*t
y1 = np.log(c1 / c10)

# Régression linéaire
resultat1 = linregress(t1, y1)

pente1 = resultat1.slope
ordonnee1 = resultat1.intercept
k1 = -pente1

print("Pente =", pente1)
print("Ordonnée à l'origine =", ordonnee1)
print("R² =", resultat1.rvalue**2)
print("k1 =", k1, "min^-1")

# Tracé
plt.scatter(t1, y1, label="Données expérimentales")
plt.plot(
    t1,
    pente1 * t1 + ordonnee1,
    color="red",
    label="Régression linéaire"
)

plt.xlabel("Temps t (min)")
plt.ylabel(r"$\ln(c_1/c_{1,0})$")
plt.title("Vérification d'une cinétique d'ordre 1")
plt.legend()
plt.grid()
plt.show()


# =========================
# QUESTION 2
# Temps de demi-réaction
# =========================

t12_1 = np.log(2) / k1

print("t1/2,1 =", t12_1, "min")


# =========================
# QUESTION 3
# Oxydation / élimination
# =========================

t2 = np.array([0, 120, 240, 360, 480, 600, 720])  # min
c2 = np.array([0.0500, 0.0413, 0.0326, 0.0239, 0.0152, 0.0065, 0])

# Pour une réaction d'ordre 0 :
# c2 = c20 - k2*t

resultat2 = linregress(t2, c2)

pente2 = resultat2.slope
ordonnee2 = resultat2.intercept
k2 = -pente2

print("\nQUESTION 3")
print("Pente =", pente2)
print("Ordonnée à l'origine =", ordonnee2)
print("R² =", resultat2.rvalue**2)
print("k2 =", k2, "mol.L^-1.min^-1")

# Tracé
plt.scatter(t2, c2, label="Données expérimentales")
plt.plot(
    t2,
    pente2 * t2 + ordonnee2,
    color="red",
    label="Régression linéaire"
)

plt.xlabel("Temps t (min)")
plt.ylabel(r"$c_2$ (mol/L)")
plt.title("Vérification d'une cinétique d'ordre 0")
plt.legend()
plt.grid()
plt.show()
