import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Sentiment Architect", page_icon="🤖")
st.title("Bilingual Sentiment Analyzer")
st.markdown("---")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
analyzer = load_model()
# Interface utilisateur
text_input = st.text_area("Entrez un texte (Français ou Anglais) :", 
                         placeholder="Ex: I'm worried about AI replacing jobs...")
if st.button("Analyser le sentiment"):
    if text_input:
        with st.spinner('L\'IA réfléchit...'):
            result = analyzer(text_input)[0]
            label = result['label'] # Ex: '1 star' ou '5 stars'

            # Transformation du label en score numérique pour l'affichage
            stars = int(label.split()[0])

            st.subheader(f"Résultat : {stars} / 5 ⭐")

            # Barre de progression visuelle
            st.progress(stars * 20)

            if stars <= 2:
                st.error("Sentiment Négatif")
            elif stars == 3:
                st.warning("Sentiment Neutre")
            else:
                st.success("Sentiment Positif")
    else:
        st.info("Veuillez entrer du texte pour lancer l'analyse.")