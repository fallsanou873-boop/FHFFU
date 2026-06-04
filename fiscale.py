import re
import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Optimiseur de Carte qgis2web",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Optimiseur de Carte Leaflet & Google Satellite")
st.write("Collez le code de votre fichier `index.html` généré par qgis2web pour corriger et optimiser automatiquement le fond de carte Google Satellite.")

# Zone de saisie du code HTML initial
code_initial = st.text_area(
    "Collez le code HTML de votre index.html ici :", 
    height=400, 
    placeholder="<!doctype html>..."
)

# Fonction de nettoyage et de correction du code
def optimiser_code_html(html_brut):
    if not html_brut:
        return ""
    
    # Bloc Google Satellite propre, sécurisé et configuré en HTTPS
    bloc_google_satellite_propre = """
        // --- BLOC GOOGLE SATELLITE CORRIGÉ ET OPTIMISÉ ---
        map.createPane('pane_GoogleSatellite_0');
        map.getPane('pane_GoogleSatellite_0').style.zIndex = 400;
        var layer_GoogleSatellite_0 = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            pane: 'pane_GoogleSatellite_0',
            opacity: 1.0,
            attribution: '<a href="https://www.google.com/permissions/geoguidelines/attr-guide.html">Map data © Google</a>',
            minZoom: 1,
            maxZoom: 28,
            maxNativeZoom: 20
        });
        map.addLayer(layer_GoogleSatellite_0);
        // -------------------------------------------------
"""
    
    # Expression régulière pour détecter et remplacer l'ancien bloc défectueux de qgis2web
    motif_recherche = r"map\.createPane\('pane_GoogleSatellite_0'\);.*?map\.addLayer\(layer_GoogleSatellite_0\);"
    
    # Application de la modification principale
    code_corrige, nb_remplacements = re.subn(motif_recherche, bloc_google_satellite_propre, html_brut, flags=re.DOTALL)
    
    # Si la structure classique n'est pas trouvée, on fait une insertion de sécurité avant setBounds()
    if nb_remplacements == 0:
        if "setBounds();" in code_corrige:
            code_corrige = code_corrige.replace("setBounds();", bloc_google_satellite_propre + "\n        setBounds();")
            
    return code_corrige

# Traitement du code si l'utilisateur a collé du contenu
if code_initial:
    code_final = optimiser_code_html(code_initial)
    
    st.success("✨ Votre code a été analysé et optimisé avec succès !")
    
    # Création de deux colonnes pour organiser l'interface
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Télécharger le résultat")
        # Bouton de téléchargement du fichier index.html corrigé
        st.download_button(
            label="Télécharger le fichier index.html corrigé",
            data=code_final,
            file_name="index.html",
            mime="text/html",
            type="primary"
        )
        
    with col2:
        st.subheader("💡 Améliorations appliquées")
        st.markdown("""
        - **Sécurisation HTTPS :** Passage forcé sur les serveurs sécurisés Google (`https://mt1.google.com`).
        - **Gestion des Panes :** Attribution d'un `zIndex` (400) strict pour éviter que le fond ne cache vos couches métiers.
        - **Zoom Max :** Configuration du `maxNativeZoom` à 20 pour éviter l'affichage de tuiles blanches ou manquantes lors des zooms profonds.
        """)
    
    # Aperçu du code généré
    with st.expander("👁️ Voir le code HTML corrigé"):
        st.code(code_final, language="html") 
