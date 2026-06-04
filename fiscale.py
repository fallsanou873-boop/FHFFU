import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Fiscalité Pikine Nord",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Gestion de la Fiscalité dans la commune de Pikine Nord")
st.write("Cette application Streamlit permet de générer, corriger et télécharger l'interface cartographique de la commune.")

# Définition du code HTML mis à jour et centré (au cas où vous téléchargez le fichier index.html)
html_pikine_nord = """<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="initial-scale=1,user-scalable=no,maximum-scale=1,width=device-width">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <link rel="stylesheet" href="css/leaflet.css">
        <link rel="stylesheet" href="css/L.Control.Layers.Tree.css">
        <link rel="stylesheet" href="css/qgis2web.css">
        <link rel="stylesheet" href="css/fontawesome-all.min.css">
        <link rel="stylesheet" href="css/leaflet-search.css">
        <link rel="stylesheet" href="css/leaflet.photon.css">
        <style>
        html, body, #map {
            width: 100%;
            height: 100%;
            padding: 0;
            margin: 0;
        }
        </style>
        <title>Fiscalité (Gestion de la Fiscalité dans la commune de Pikine Nord)</title>
    </head>
    <body>
        <div id="map">
        </div>
        <script src="js/qgis2web_expressions.js"></script>
        <script src="js/leaflet.js"></script>
        <script src="js/L.Control.Layers.Tree.min.js"></script>
        <script src="js/multi-style-layer.js"></script>
        <script src="js/leaflet-svg-shape-markers.min.js"></script>
        <script src="js/leaflet.rotatedMarker.js"></script>
        <script src="js/leaflet.pattern.js"></script>
        <script src="js/leaflet-hash.js"></script>
        <script src="js/Autolinker.min.js"></script>
        <script src="js/rbush.min.js"></script>
        <script src="js/labelgun.min.js"></script>
        <script src="js/labels.js"></script>
        <script src="js/leaflet.photon.js"></script>
        <script src="js/proj4.js"></script>
        <script src="js/proj4leaflet.js"></script>
        <script src="js/leaflet-search.js"></script>
        
        <script src="data/PIKINENORD_1.js"></script>
        <script src="data/Secteur5_2.js"></script>
        <script src="data/Secteur3_3.js"></script>
        <script src="data/Secteur4_4.js"></script>
        <script src="data/Secteur2_5.js"></script>
        <script src="data/Secteur1_6.js"></script>
        <script src="data/March_7.js"></script>
        <script src="data/Equipecommercial_8.js"></script>
        <script src="data/Zonedestationnement_9.js"></script>
        <script src="data/OccupationDomain_10.js"></script>
        <script src="data/Supportpublicitaire_11.js"></script>
        <script src="data/Distributeurdecarburant_12.js"></script>
        <script src="data/Pharmacie_13.js"></script>
        <script src="data/differentesroutes_14.js"></script>
        
        <script>
        var highlightLayer;
        function highlightFeature(e) {
            highlightLayer = e.target;
            highlightLayer.openPopup();
        }
        
        var crs = new L.Proj.CRS('EPSG:32628', '+proj=utm +zone=28 +datum=WGS84 +units=m +no_defs', {
            resolutions: [2800, 1400, 700, 350, 175, 84, 42, 21, 11.2, 5.6, 2.8, 1.4, 0.7, 0.35, 0.14, 0.07],
        });
        
        var map = L.map('map', {
            crs: crs,
            continuousWorld: false,
            worldCopyJump: false, 
            zoomControl: false, 
            maxZoom: 28, 
            minZoom: 1
        });

        // Centrage ajusté sur la zone requise (14.761347, -17.395027)
        var pointTarget = proj4('EPSG:4326', 'EPSG:32628', [-17.395027, 14.761347]);
        var leafletPoint = L.point(pointTarget[0], pointTarget[1]);
        map.setView(crs.projection.unproject(leafletPoint), 16);

        var hash = new L.Hash(map);
        map.attributionControl.setPrefix('<a href="https://github.com/qgis2web/qgis2web" target="_blank">qgis2web</a> &middot; <a href="https://leafletjs.com">Leaflet</a> &middot; <a href="https://qgis.org">QGIS</a>');
        var autolinker = new Autolinker({truncate: {length: 30, location: 'smart'}});
        
        function removeEmptyRowsFromPopupContent(content, feature) {
             var tempDiv = document.createElement('div');
             tempDiv.innerHTML = content;
             var rows = tempDiv.querySelectorAll('tr');
             for (var i = 0; i < rows.length; i++) {
                 var td = rows[i].querySelector('td.visible-with-data');
                 var key = td ? td.id : '';
                 if (td && td.classList.contains('visible-with-data') && feature.properties[key] == null) {
                     rows[i].parentNode.removeChild(rows[i]);
                 }
             }
             return tempDiv.innerHTML;
        }

        var zoomControl = L.control.zoom({ position: 'topleft' }).addTo(map);
        var bounds_group = new L.featureGroup([]);
        function setBounds() {}

        map.createPane('pane_GoogleSatellite_0');
        map.getPane('pane_GoogleSatellite_0').style.zIndex = 400;
        var layer_GoogleSatellite_0 = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            pane: 'pane_GoogleSatellite_0',
            opacity: 1.0,
            attribution: '© Google',
            minZoom: 1,
            maxZoom: 28,
            maxNativeZoom: 20
        });
        map.addLayer(layer_GoogleSatellite_0);
        </script>
    </body>
</html>"""

# Interface de téléchargement de l'index.html
col_info, col_actions = st.columns([2, 1])

with col_info:
    st.subheader("📊 Paramètres d'exportation")
    st.markdown("""
    - **Projet :** Application de gestion de la fiscalité locale.
    - **Zone cible :** Commune de Pikine Nord.
    - **Coordonnées du centre :** 14.761347, -17.395027.
    """)

with col_actions:
    st.subheader("📥 Téléchargement")
    st.download_button(
        label="Télécharger index.html pour maintenance",
        data=html_pikine_nord,
        file_name="index.html",
        mime="text/html",
        type="primary"
    )

# --- AJOUT DE LA PAGE INTÉGRÉE (NETLIFY) ---
st.divider()
st.subheader("🗺️ Aperçu en temps réel de la Carte Interactive")
st.write("Retrouvez ci-dessous la cartographie dynamique hébergée sur Netlify :")

# Intégration de la page Netlify avec les coordonnées spécifiées
url_netlify = "https://gestion-fiscalite-local-pikine-nord.netlify.app/#16/14.761347/-17.395027"
st.components.v1.iframe(url_netlify, height=600, scrolling=True)

# --- ZONE DES LIENS DE L'APPLICATION ---
st.divider()
st.markdown("""
🔗 **Lien de l'application en ligne :** [https://getiondelafiscalite.streamlit.app/](https://getiondelafiscalite.streamlit.app/)  
🌐 **Serveur de données Cartographiques (Netlify) :** [Visiter la page plein écran]({})
""".format(url_netlify))
