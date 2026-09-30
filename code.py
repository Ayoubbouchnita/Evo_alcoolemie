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

# =========================
# QUESTION 4
# Temps de demi-réaction (ordre 0)
# =========================

# Ordre 0 : t1/2 = c20 / (2*k2)
c20 = c2[0]
t12_2 = c20 / (2 * k2)

print("\nQUESTION 4")
print("t1/2,2 =", t12_2, "min")
print("t1/2,2 / t1/2,1 =", t12_2 / t12_1)


# =========================
# QUESTION 5
# Concentration d'éthanol dans la bière
# =========================

M_C, M_H, M_O = 12, 1.0, 16  # g/mol
M_eth = 2 * M_C + 6 * M_H + M_O  # C2H6O
rho_eth = 790  # g/L
d = 0.06

# 1 L de bière contient d litres d'éthanol
C0_g = d * rho_eth  # g/L
C0 = C0_g / M_eth  # mol/L

print("\nQUESTION 5")
print("M(éthanol) =", M_eth, "g/mol")
print("C0 =", C0_g, "g/L")
print("C0 =", C0, "mol/L")


# =========================
# QUESTION 6
# Alcoolémie d'Alice au cours du temps
# =========================

Ve = 2 * 0.50  # L (deux bières de 50 cL)
Vs = 40  # L


def c(t):
    return C0 * Ve / Vs * (1 - np.exp(-k1 * t)) - k2 * t


# On s'arrête quand l'alcoolémie revient à 0
t_fin = C0 * Ve / Vs / k2
t = np.linspace(0, t_fin, 1000)

print("\nQUESTION 6")
print("Alcoolémie nulle à t =", t_fin, "min")

plt.plot(t, c(t))
plt.xlabel("Temps t (min)")
plt.ylabel(r"$c$ (mol/L)")
plt.title("Alcoolémie d'Alice")
plt.grid()
plt.show()


# =========================
# QUESTION 7 et 8
# Maximum de l'alcoolémie
# =========================

# dc/dt = C0*Ve/Vs*k1*exp(-k1*t) - k2 = 0
# => t_max = ln(C0*Ve*k1 / (Vs*k2)) / k1
t_max = np.log(C0 * Ve * k1 / (Vs * k2)) / k1
c_max = c(t_max)

print("\nQUESTION 8")
print("t_max =", t_max, "min")

print("\nQUESTION 7")
print("c_max =", c_max, "mol/L")
print("c_max =", c_max * M_eth, "g/L")
=======



from scipy.optimize import brentq



# QUESTION 9
# Droit de conduire à t_max ?

limite_g = 0.5                 # g/L 
c_lim = limite_g / M_eth        # mol/L

print("\nQUESTION 9")
print("c_max =", c_max, "mol/L =", c_max * M_eth, "g/L")
print("Limite =", limite_g, "g/L")
print("Alice peut conduire ?", c_max < c_lim)


# QUESTION 10
# Instant où l'alcoolémie repasse sous la limite

t_lim = brentq(lambda x: c(x) - c_lim, t_max, t_fin)

print("\nQUESTION 10")
print("t_lim =", t_lim, "min =", t_lim / 60, "h")

# Tracé
plt.plot(t, c(t), label="Alcoolémie d'Alice")
plt.axhline(c_lim, color="red", linestyle="--", label=f"Limite légale ({limite_g} g/L)")
plt.plot(t_max, c_max, "go", label=f"Maximum ({t_max:.1f} min)")
plt.plot(t_lim, c_lim, "ro", label=f"Retour sous la limite ({t_lim:.0f} min)")
plt.xlabel("Temps t (min)")
plt.ylabel(r"$c$ (mol/L)")
plt.title("Alcoolémie d'Alice et limite légale")
plt.legend()
plt.grid()
plt.show()
