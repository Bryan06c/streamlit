import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt

# Titre de l'application avec du markdown
st.title("📊 Visualisation interactive d'une fonction affine avec Streamlit")

# Introduction à l'application
st.markdown("""
Dans cette application, vous pouvez visualiser une fonction affine interactive en ajustant la pente **a** et l'ordonnée à l'origine **b**.  
Vous pouvez également personnaliser l'intervalle des valeurs **x**, la couleur de la courbe et voir l'équation de la droite en temps réel.

### Fonctionnalités :
- **Choix de la pente (a)** : Modifiez la pente de la droite.
- **Choix de l'ordonnée à l'origine (b)** : Modifiez l'intersection de la droite avec l'axe y.
- **Plage des valeurs x** : Personnalisez l'intervalle des valeurs pour x.
- **Couleur de la courbe** : Choisissez la couleur de la droite pour la personnaliser.
""")

# Sliders pour les paramètres a (pente) et b (ordonnée à l'origine)
a = st.slider("Choisissez la pente (a)", min_value=-10, max_value=10, value=1)
b = st.slider("Choisissez l'ordonnée à l'origine (b)", min_value=-10, max_value=10, value=0)

# Personnalisation de l'intervalle des valeurs x
st.markdown("### Personnaliser l'intervalle des valeurs de x")
x_min = st.slider("Plage minimale de x", min_value=-20, max_value=0, value=-10)
x_max = st.slider("Plage maximale de x", min_value=0, max_value=20, value=10)

# Génération des valeurs x sur l'intervalle choisi
x_values = np.linspace(x_min, x_max, 100)

# Calcul des valeurs y
y_values = a * x_values + b

# Affichage de l'équation de la droite
st.markdown(f"### Équation de la droite : y = {a}x + {b}")

# Options de personnalisation de la couleur de la courbe
st.markdown("### Personnalisez la couleur de la courbe")
line_color = st.color_picker("Choisissez la couleur de la courbe", "#00f900")

# Création du graphique avec Matplotlib
plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label=f"y = {a}x + {b}", color=line_color)
plt.title("Fonction affine y = ax + b")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Lignes de l'axe
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Légende
plt.legend()

# Affichage du graphique dans Streamlit
st.pyplot(plt)
