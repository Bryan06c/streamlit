import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titre de l'application avec du markdown
st.title("🖥️ Outil d'analyse de données interactif avec Streamlit")

# Description de l'application
st.markdown("""
Bienvenue dans cet outil interactif d'analyse de données !  
Vous pouvez charger un fichier CSV, explorer vos données, visualiser des graphiques interactifs et exporter les résultats.

### Fonctionnalités disponibles :
- **Chargement des données** : Importez votre fichier CSV.
- **Exploration des données** : Affichez les premières lignes et des statistiques descriptives.
- **Visualisation des données** : Créez des nuages de points ou des histogrammes interactifs.
- **Filtrage des données** : Filtrez selon une colonne et une valeur spécifique.
- **Exportation des données** : Téléchargez les données filtrées et exportez les graphiques.
""")

# Chargement des données avec une barre latérale
st.sidebar.header("📂 Chargement des données")
uploaded_file = st.sidebar.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lire le fichier CSV
    data = pd.read_csv(uploaded_file)

    # Aperçu des données
    st.subheader("📊 Aperçu des données")
    st.write(data.head())

    # Statistiques descriptives
    st.subheader("📈 Statistiques descriptives")
    st.write(data.describe())

    # Exploration des colonnes avec st.multiselect
    st.subheader("🔎 Sélectionner des colonnes à afficher")
    columns = st.multiselect("Choisissez des colonnes", data.columns.tolist())
    if columns:
        st.write(data[columns])

    # Choix du type de graphique
    st.subheader("📊 Visualisation des données")
    chart_type = st.selectbox("Choisissez le type de graphique", ["Nuage de points", "Histogramme"])

    if chart_type == "Nuage de points":
        # Visualisation : nuage de points interactif
        st.subheader("🔵 Nuage de points interactif")
        x_axis = st.selectbox("Sélectionner une colonne pour l'axe X", data.columns)
        y_axis = st.selectbox("Sélectionner une colonne pour l'axe Y", data.columns)

        # Créer le graphique avec seaborn et Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=data[x_axis], y=data[y_axis], ax=ax)
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)

        # Afficher le graphique avec st.pyplot()
        st.pyplot(fig)

    elif chart_type == "Histogramme":
        # Affichage de l'histogramme
        st.subheader("🔶 Histogramme interactif")
        hist_column = st.selectbox("Choisissez une colonne numérique pour l'histogramme", data.select_dtypes(include=['number']).columns)
        bins = st.slider("Nombre de bacs de l'histogramme", min_value=5, max_value=100, value=20)

        # Créer l'histogramme avec Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(data[hist_column], bins=bins, color="skyblue", edgecolor="black")
        ax.set_xlabel(hist_column)
        ax.set_ylabel("Fréquence")

        # Afficher le graphique de l'histogramme
        st.pyplot(fig)

    # Filtrage des données
    st.subheader("🔎 Filtrage des données")
    filter_column = st.selectbox("Choisissez une colonne pour filtrer", data.columns)
    filter_value = st.text_input(f"Entrez une valeur pour filtrer {filter_column}")

    if filter_value:
        filtered_data = data[data[filter_column].astype(str).str.contains(filter_value, case=False, na=False)]
        st.write("📄 Données filtrées", filtered_data)

        # Exporter les données filtrées
        st.download_button(
            label="📥 Télécharger les données filtrées",
            data=filtered_data.to_csv(index=False),
            file_name="filtered_data.csv",
            mime="text/csv"
        )

    # Résumé des types de données et valeurs manquantes
    st.subheader("📊 Résumé des données")
    st.write(data.info())

    # Exporter le graphique actuel
    st.subheader("📤 Exporter le graphique")
    export_graph = st.checkbox("Exporter le graphique actuel en PNG")
    
    if export_graph:
        fig.savefig("graph.png", dpi=300)
        st.success("Graphique exporté sous le nom 'graph.png'")

else:
    st.warning("⚠️ Veuillez télécharger un fichier CSV pour commencer.")
