import streamlit as st
import requests
import time

# 1. Configuration (Garde bien ton URL exacte !)
URL_FB = "https://ton-projet.firebaseio.com/.json" # Vérifie bien ton lien ici

st.title("📱 ClassConnect Pro")

# 2. Zone pour publier (On utilise tes noms : pseudo et msg)
with st.container():
    c1, c2 = st.columns([1, 3])
    with c1:
        nom_utilisateur = st.text_input("Pseudo", value="didou")
    with c2:
        texte_message = st.text_input("Message", placeholder="Écris ici...")
    
    if st.button("Envoyer 🚀"):
        if texte_message:
            # On utilise exactement la structure que tu m'as montrée
            nouveau_data = {
                "pseudo": nom_utilisateur,
                "msg": texte_message,
                "date": time.time()
            }
            requests.post(URL_FB, json=nouveau_data)
            st.success("Envoyé !")
            st.rerun()

st.divider()

# 3. Affichage du fil (On lit tes noms : pseudo et msg)
st.subheader("Fil d'actualité 💬")

try:
    r = requests.get(URL_FB).json()
    if r:
        # On trie pour avoir les plus récents en haut
        for key in reversed(list(r.keys())):
            item = r[key]
            # On vérifie si c'est bien un message (pour éviter les erreurs)
            if isinstance(item, dict) and "msg" in item:
                with st.chat_message("user"):
                    st.write(f"**{item.get('pseudo', 'Anonyme')}**")
                    st.write(item.get('msg', ''))
    else:
        st.info("Aucun message trouvé.")
except Exception as e:
    st.error(f"Erreur d'affichage : {e}")
