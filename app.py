import streamlit as st
st.set_page_config(
    page_title="Mohamed Dyn",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# ETAPE 2 : LE CSS (POUR FORCER SI LA CONFIG ECHOUE)
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Force le conteneur principal à prendre toute la largeur */
    .main .block-container {
        padding-top: 2rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)
import content as data
import time
import os
import base64
from streamlit_option_menu import option_menu
from PIL import Image
import requests

# ==============================================================================
# 1. CONFIGURATION & GESTION DE L'ÉTAT (URL & SESSION)
# ==============================================================================

# Récupération des paramètres URL
query_params = st.query_params
url_lang = query_params.get("lang", None)
project_id = query_params.get("project_id")
exp_id = query_params.get("exp_id")
active_tab = query_params.get("tab")
url_demo_id = query_params.get("demo_id")

# Initialisation de la langue (Priorité : URL > Session > Défaut 'fr')
if 'language' not in st.session_state:
    st.session_state.language = url_lang if url_lang in ['fr', 'en'] else 'fr'
elif url_lang and url_lang != st.session_state.language:
    # Si l'URL change manuellement, on met à jour la session
    st.session_state.language = url_lang

# Synchronisation inverse : Si la session change, on force l'URL
if st.session_state.language != st.query_params.get("lang"):
    st.query_params["lang"] = st.session_state.language

# Initialisation de la démo courante
if 'current_demo' not in st.session_state:
    st.session_state.current_demo = None

# Variable raccourci pour la langue actuelle
lang = st.session_state.language

# ==============================================================================
# 2. DICTIONNAIRES DE TRADUCTION (UI TEXTS)
# ==============================================================================
T = {
    "fr": {
        "prompto" : """
                                Tu es un assistant médical virtuel expert, bienveillant et professionnel.
                                TES OBJECTIFS :
                                1. Analyser les symptômes décrits par l'utilisateur avec empathie.
                                2. Proposer des hypothèses simples et des conseils d'hygiène de vie (repos, hydratation, etc.).
                                3. Structurer ta réponse avec des sauts de ligne et du gras pour être lisible.
                                
                                RÈGLES DE SÉCURITÉ ABSOLUES (CRITIQUE) :
                                - NE JAMAIS poser de diagnostic médical définitif.
                                - Si les symptômes semblent graves (douleur poitrine, difficultés respiratoires, paralysie), ORDONNE d'appeler les urgences immédiatement.
                                - Termine TOUJOURS par une phrase rappelant que tu es une IA et qu'il faut consulter un médecin réel.
                                
                                Contexte de la conversation :
                                """,
        "bng" : "Bonjour. Je suis votre assistant médical virtuel. Décrivez-moi vos symptômes, je ferai de mon mieux pour vous orienter et vous conseiller.",
        "greeting": "Bonjour, je suis",
        "menu_items": ["Projets", "Expériences", "Compétences", "✨ DÉMOS LIVE", "Contact"],
        "back_projects": "⬅ Retour aux projets",
        "back_exp": "⬅ Retour aux expériences",
        "back_demos": "⬅ Retour aux démos",
        "desc_title": "📝 Description",
        "impact_title": "🎯 Impact",
        "challenges_title": "🧗 Challenges & Solutions",
        "stack_title": "🛠 Stack",
        "github_btn": "Voir sur GitHub 🐙",
        "demo_btn": "Tester la démo 🎮",
        "download_report": "Télécharger le Rapport",
        "missions_title": "💼 Missions",
        "results_title": "🏆 Réalisations",
        "env_title": "🛠 Environnement",
        "more_btn": "En savoir plus ➜",
        "cv_title": "###### 📄 Consulter mon CV",
        "cv_not_found": "Fichier introuvable",
        "nudge_text": """
        <div style="background-color: #FFF7ED; border-left: 5px solid #FF9F1C; padding: 15px; border-radius: 5px; margin-bottom: 40px; line-height: 1.6;">
            <p style="margin:0; font-weight: 500; color: #9A3412;">
                💡 <strong>Preuve par l'exemple :</strong> 
                Plutôt que de longs discours, j'ai rendu mes projets interactifs. 
                Rendez-vous dans l'onglet <span style="background-color:#FF9F1C; color:white; padding:2px 8px; border-radius:4px; font-size:0.85em; font-weight:700; white-space: nowrap;">✨ DÉMOS LIVE</span> 
                ci-dessus pour tester mes modèles en temps réel.
            </p>
        </div>""",
        "bio_html": f"""
<div style='margin-bottom: 30px; font-size: 1.15rem; line-height: 1.6; color: #374151;'>
<p>
Élève-ingénieur en dernière année à l'<strong>{data.INFO['school']}</strong>, je cultive une double compétence rare : 
<strong>Data Engineering & Data Science</strong>.
</p>
<p>
Je ne me contente pas d'entraîner des modèles : je construis les architectures qui les rendent opérationnels. 
De l'ingénierie des données (ETL, Pipelines) à l'IA Générative (RAG, LLMs), mon objectif est simple : 
<strong>transformer la donnée brute en solution stratégique.</strong>
</p>
<p>
🎯 <strong>À la recherche d'un stage PFE</strong> pour relever des défis techniques concrets et créer de la valeur au sein de votre équipe.
</p>
</div>
        """,
        "section_projects": "### Mes Projets",
        "section_exp": "### 🚀 Parcours Professionnel",
        "section_skills": "### Arsenal Technique",
        "section_demos": "### 🎮 Zone de Test Interactive",
        "section_contact": "### 📬 Me Contacter",
        "demo_info": "💡 Cliquez sur un projet ci-dessous pour le tester en direct.",
        "contact_intro": """
            <div style="text-align: center; margin-bottom: 40px; font-size: 1.1rem; color: #4B5563;">
                Je suis actuellement à la recherche d'un <b>Stage de Fin d'Études (PFE)</b> en Data Science / IA, Data Engineering. 
                <br>Disponible immédiatement pour échanger sur vos projets et opportunités.
            </div>""",
        "coord_title": "#### 📍 Mes Coordonnées",
        "linkedin_btn": "Voir mon profil LinkedIn",
        "msg_title": "#### 💬 M'envoyer un message",
        "msg_subtitle": "Une question sur un projet ? Une proposition d'entretien ? Remplissez ce formulaire, je vous réponds sous 24h. 🚀",
        "form_name": "Nom complet",
        "form_email": "Votre Email",
        "form_msg": "Votre Message",
        "form_btn": "Envoyer le message 📨",
        "form_success": "✅ Merci ! Votre message a bien été envoyé.",
        "form_error": "⚠️ Veuillez remplir tous les champs.",
        "input_pipeline": "📥 <b>Input Pipeline :</b> Sélectionnez une source de données ci-dessous.",
        "input_corpus": "📝 <b>Input Corpus :</b> Saisissez une phrase ci-dessous.",
        "input_meta": "📝 <b>Transaction Metadata :</b> Configurez les paramètres de la transaction.",
        "launch_inf": "🚀 Lancer l'Inférence",
        "launch_ana": "🚀 Lancer l'Analyse",
        "launch_risk": "🚀 Exécuter l'Analyse de Risque"
    },
    "en": {
        "prompto" : """You are an expert, empathetic, and professional virtual medical assistant.

                        YOUR OBJECTIVES:

                        Analyze the symptoms described by the user with empathy.

                        Offer simple hypotheses and lifestyle advice (rest, hydration, etc.).

                        Structure your response using line breaks and bold text for readability.

                        ABSOLUTE SAFETY RULES (CRITICAL):

                        NEVER provide a definitive medical diagnosis.

                        If symptoms appear severe (chest pain, difficulty breathing, paralysis), INSTRUCT the user to call emergency services immediately.

                        ALWAYS conclude with a statement reminding the user that you are an AI and advising them to consult a real doctor.

                        Conversation context:
                        """,
        "bng" : "Hello. I am your virtual medical assistant. Please describe your symptoms, and I will do my best to guide and advise you.",
        "greeting": "Hello, I am",
        "menu_items": ["Projects", "Experiences", "Skills", "✨ LIVE DEMOS", "Contact"],
        "back_projects": "⬅ Back to projects",
        "back_exp": "⬅ Back to experiences",
        "back_demos": "⬅ Back to demos",
        "desc_title": "📝 Description",
        "impact_title": "🎯 Impact",
        "challenges_title": "🧗 Challenges & Solutions",
        "stack_title": "🛠 Stack",
        "github_btn": "View on GitHub 🐙",
        "demo_btn": "Try Demo 🎮",
        "download_report": "Download Report",
        "missions_title": "💼 Missions",
        "results_title": "🏆 Achievements",
        "env_title": "🛠 Environment",
        "more_btn": "Learn more ➜",
        "cv_title": "###### 📄 Download my CV",
        "cv_not_found": "File not found",
        "nudge_text": """
        <div style="background-color: #FFF7ED; border-left: 5px solid #FF9F1C; padding: 15px; border-radius: 5px; margin-bottom: 40px;">
            <p style="margin:0; font-weight: 500; color: #9A3412;">
                💡 <strong>Proof by example:</strong> 
                Instead of long speeches, I made my projects interactive. 
                Go to the <span style="background-color:#FF9F1C; color:white; padding:2px 6px; border-radius:4px; font-size:0.9em;">✨ LIVE DEMOS</span> 
                tab above to test my models (Vision, NLP, Fraud) in real-time.
            </p>
        </div>""",
        "bio_html": f"""
        <div style='margin-bottom: 30px; font-size: 1.15rem; line-height: 1.6; color: #374151;'>
            <p>
                Final-year engineering student at <strong>{data.INFO['school']}</strong>, I cultivate a rare dual skill set: 
                <strong>Data Engineering & Data Science</strong>.
            </p>
            <p>
                I don't just train models: I build the architectures that make them operational. 
                From data engineering (ETL, Pipelines) to Generative AI (RAG, LLMs), my goal is simple: 
                <strong>transform raw data into strategic solutions.</strong>
            </p>
            <p>
                🎯 <strong>Looking for an End-of-Studies Internship (PFE)</strong> to tackle concrete technical challenges and create value within your team.
            </p>
        </div>
        """,
        "section_projects": "### My Projects",
        "section_exp": "### 🚀 Professional Experience",
        "section_skills": "### Technical Arsenal",
        "section_demos": "### 🎮 Interactive Test Zone",
        "section_contact": "### 📬 Contact Me",
        "demo_info": "💡 Click on a project below to test it live.",
        "contact_intro": """
            <div style="text-align: center; margin-bottom: 40px; font-size: 1.1rem; color: #4B5563;">
                I am currently looking for an <b>End-of-Studies Internship (PFE)</b> in Data Science / AI, Data Engineering. 
                <br>Available immediately to discuss your projects and opportunities.
            </div>""",
        "coord_title": "#### 📍 My Details",
        "linkedin_btn": "View LinkedIn Profile",
        "msg_title": "#### 💬 Send me a message",
        "msg_subtitle": "A question about a project? An interview proposal? Fill out this form, I'll reply within 24h. 🚀",
        "form_name": "Full Name",
        "form_email": "Your Email",
        "form_msg": "Your Message",
        "form_btn": "Send Message 📨",
        "form_success": "✅ Thank you! Your message has been sent.",
        "form_error": "⚠️ Please fill in all fields.",
        "input_pipeline": "📥 <b>Input Pipeline:</b> Select a data source below.",
        "input_corpus": "📝 <b>Input Corpus:</b> Enter a sentence below.",
        "input_meta": "📝 <b>Transaction Metadata:</b> Configure transaction parameters.",
        "launch_inf": "🚀 Launch Inference",
        "launch_ana": "🚀 Launch Analysis",
        "launch_risk": "🚀 Run Risk Analysis"
    }
}
UI = T[lang]

# Sélection des données pour la vue principale
if lang == 'en':
    current_info = data.INFO_EN if hasattr(data, 'INFO_EN') else data.INFO
    current_projects_list = data.PROJECTS_EN if hasattr(data, 'PROJECTS_EN') else data.PROJECTS
    current_experiences_list = data.EXPERIENCES_EN if hasattr(data, 'EXPERIENCES_EN') else data.EXPERIENCES
    current_demos_list = data.DEMOS_EN if hasattr(data, 'DEMOS_EN') else data.DEMOS
else:
    current_info = data.INFO
    current_projects_list = data.PROJECTS
    current_experiences_list = data.EXPERIENCES
    current_demos_list = data.DEMOS

current_skills = data.DATA["SKILLS"]

# CSS Local
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")

# ==============================================================================
# --- LOGIQUE DE NAVIGATION ---
# ==============================================================================

# Règle de priorité : Si un demo_id existe, l'onglet doit être 'demos'
if url_demo_id and active_tab != "demos":
    st.query_params["tab"] = "demos"
    st.query_params["lang"] = lang
    st.rerun()

# Synchronisation démo
if url_demo_id != st.session_state.current_demo:
    st.session_state.current_demo = url_demo_id
    # On ne rerun pas ici pour éviter une boucle infinie, sauf si nécessaire

def on_menu_change(key):
    selected = st.session_state["nav_menu"]
    # Mise à jour des params URL en conservant la langue
    base_params = {"lang": st.session_state.language}
    
    if selected == UI["menu_items"][0]: # Projets
        base_params["tab"] = "projets"
    elif selected == UI["menu_items"][1]: # Expériences
        base_params["tab"] = "experiences"
    elif selected == UI["menu_items"][2]: # Compétences
        base_params["tab"] = "competences"
    elif selected == UI["menu_items"][3]: # Démos
        base_params["tab"] = "demos"
    elif selected == UI["menu_items"][4]: # Contact
        base_params["tab"] = "contact"
    
    # Application des changements
    for k, v in base_params.items():
        st.query_params[k] = v
    
    # Nettoyage des ID si on change de menu
    if "demo_id" in st.query_params and selected != UI["menu_items"][3]:
        del st.query_params["demo_id"]

def set_demo(demo_key):
    st.query_params["tab"] = "demos"
    st.query_params["demo_id"] = demo_key
    st.query_params["lang"] = lang

def reset_demo():
    st.query_params["tab"] = "demos"
    st.query_params["lang"] = lang
    if "demo_id" in st.query_params:
        del st.query_params["demo_id"]
    if 'fraud_result' in st.session_state: 
        del st.session_state.fraud_result

# ==============================================================================
# --- VUES : DÉTAIL PROJET (FR & EN) ---
# ==============================================================================

def show_project_detail(p_id):
    """Affiche le détail d'un projet en Français"""
    try:
        project = data.PROJECTS[int(p_id)]
    except:
        st.error("Projet introuvable.")
        return

    # Lien de retour avec maintien de la langue
    st.markdown(f'<a href="/?tab=projets&lang=fr" target="_self" class="back-btn">{T["fr"]["back_projects"]}</a>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="padding-bottom:20px; border-bottom:1px solid #e5e7eb; margin-bottom:30px;">
        <h1 style="font-size:3rem; margin-bottom:10px; color:#111827;">{project['title']}</h1>
        <p style="font-size:1.2rem; color:#6B7280;">{project['type']} | {project['period']}</p>
    </div>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"### {T['fr']['desc_title']}")
        desc_content = project.get('details', project['desc'])
        st.markdown(f"""
        <div style="background-color: #EFF6FF; padding: 20px; border-radius: 8px; border-left: 5px solid #3B82F6; color: #1E3A8A; font-size: 1rem; line-height: 1.6;">
            {desc_content}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {T['fr']['impact_title']}")
        impact_content = project['impact']
        st.markdown(f"""
        <div style="background-color: #ECFDF5; padding: 20px; border-radius: 8px; border-left: 5px solid #10B981; color: #064E3B; font-size: 1rem; line-height: 1.6;">
            {impact_content}
        </div>
        """, unsafe_allow_html=True)
        
        if "challenges" in project:
            st.markdown(f"### {T['fr']['challenges_title']}")
            challenges_list = "".join([f"<li style='margin-bottom:5px;'>{c}</li>" for c in project['challenges']])
            st.markdown(f"""
            <div style="background-color: #FFF7ED; padding: 20px; border-radius: 8px; border-left: 5px solid #F97316; color: #9A3412; font-size: 1rem; line-height: 1.6;">
                <ul style="margin:0; padding-left:20px;">
                    {challenges_list}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"### {T['fr']['stack_title']}")
        tags = "".join([f'<span class="skill-tag">{t}</span>' for t in project["tech"]])
        st.markdown(f'<div style="margin-bottom:20px;">{tags}</div>', unsafe_allow_html=True)
        
        if "link" in project:
             st.markdown(f"""<a href="{project['link']}" target="_blank" style="display:block; text-align:center; background:#111827; color:white; padding:12px; border-radius:8px; text-decoration:none; font-weight:600; margin-bottom:10px;">{T['fr']['github_btn']}</a>""", unsafe_allow_html=True)
        if "demo_key" in project:
            link = f"/?tab=demos&demo_id={project['demo_key']}&lang=fr"
            st.markdown(f"""<a href="{link}" target="_self" style="display:block; text-align:center; background:#FF9F1C; color:white; padding:12px; border-radius:8px; text-decoration:none; font-weight:600;">{T['fr']['demo_btn']}</a>""", unsafe_allow_html=True)


def show_project_detail_en(p_id):
    """Display project details in English"""
    try:
        # Utilisation explicite de PROJECTS_EN
        project = data.PROJECTS_EN[int(p_id)]
    except:
        st.error("Project not found.")
        return

    # Lien de retour avec paramètre lang=en
    st.markdown(f'<a href="/?tab=projets&lang=en" target="_self" class="back-btn">{T["en"]["back_projects"]}</a>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="padding-bottom:20px; border-bottom:1px solid #e5e7eb; margin-bottom:30px;">
        <h1 style="font-size:3rem; margin-bottom:10px; color:#111827;">{project['title']}</h1>
        <p style="font-size:1.2rem; color:#6B7280;">{project['type']} | {project['period']}</p>
    </div>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"### {T['en']['desc_title']}")
        desc_content = project.get('details', project['desc'])
        st.markdown(f"""
        <div style="background-color: #EFF6FF; padding: 20px; border-radius: 8px; border-left: 5px solid #3B82F6; color: #1E3A8A; font-size: 1rem; line-height: 1.6;">
            {desc_content}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {T['en']['impact_title']}")
        impact_content = project['impact']
        st.markdown(f"""
        <div style="background-color: #ECFDF5; padding: 20px; border-radius: 8px; border-left: 5px solid #10B981; color: #064E3B; font-size: 1rem; line-height: 1.6;">
            {impact_content}
        </div>
        """, unsafe_allow_html=True)
        
        if "challenges" in project:
            st.markdown(f"### {T['en']['challenges_title']}")
            challenges_list = "".join([f"<li style='margin-bottom:5px;'>{c}</li>" for c in project['challenges']])
            st.markdown(f"""
            <div style="background-color: #FFF7ED; padding: 20px; border-radius: 8px; border-left: 5px solid #F97316; color: #9A3412; font-size: 1rem; line-height: 1.6;">
                <ul style="margin:0; padding-left:20px;">
                    {challenges_list}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"### {T['en']['stack_title']}")
        tags = "".join([f'<span class="skill-tag">{t}</span>' for t in project["tech"]])
        st.markdown(f'<div style="margin-bottom:20px;">{tags}</div>', unsafe_allow_html=True)
        
        if "link" in project:
             st.markdown(f"""<a href="{project['link']}" target="_blank" style="display:block; text-align:center; background:#111827; color:white; padding:12px; border-radius:8px; text-decoration:none; font-weight:600; margin-bottom:10px;">{T['en']['github_btn']}</a>""", unsafe_allow_html=True)
        if "demo_key" in project:
            link = f"/?tab=demos&demo_id={project['demo_key']}&lang=en"
            st.markdown(f"""<a href="{link}" target="_self" style="display:block; text-align:center; background:#FF9F1C; color:white; padding:12px; border-radius:8px; text-decoration:none; font-weight:600;">{T['en']['demo_btn']}</a>""", unsafe_allow_html=True)


# --- FONCTION UTILITAIRE (PDF) ---
def get_pdf_button(file_path, label, custom_style=None):
    if not os.path.exists(file_path):
        return f"""<span style="color:red; font-size:0.8em; margin-left:10px;">⚠️ {UI['cv_not_found']} : {os.path.basename(file_path)}</span>"""
    
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    if custom_style is None:
        custom_style = "text-decoration:none; background-color:#FF9F1C; color:white; padding:6px 12px; border-radius:6px; font-weight:600; font-size:0.85rem; display:inline-flex; align-items:center; gap:5px;"
        
    return f"""<a href="data:application/pdf;base64,{base64_pdf}" download="{os.path.basename(file_path)}" style="{custom_style}">{label} 📥</a>"""


# ==============================================================================
# --- VUES : DÉTAIL EXPÉRIENCE (FR & EN) ---
# ==============================================================================

def show_experience_detail(e_id):
    """Affiche le détail d'une expérience en Français"""
    try: exp = data.EXPERIENCES[int(e_id)]
    except: st.error("Expérience introuvable."); return

    # Lien de retour avec lang=fr
    st.markdown(f'<a href="/?tab=experiences&lang=fr" target="_self" class="back-btn">{T["fr"]["back_exp"]}</a>', unsafe_allow_html=True)

    st.markdown(f"""
    <div style="padding-bottom:20px; border-bottom:1px solid #e5e7eb; margin-bottom:30px;">
        <h1 style="font-size:2.5rem; margin-bottom:10px; color:#111827;">{exp['role']}</h1>
        <h2 style="font-size:1.5rem; color:#4F46E5; margin-bottom:10px;">chez {exp['company']}</h2>
        <span style="background:#EEF2FF; color:#4F46E5; padding:5px 15px; border-radius:20px; font-weight:600;">🗓 {exp['period']}</span>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"### {T['fr']['missions_title']}")
        st.markdown(exp['description'], unsafe_allow_html=True)
        st.markdown(f"### {T['fr']['results_title']}")
        for res in exp['results']:
            st.markdown(f"""<div style="background:white; padding:15px; border-radius:10px; border:1px solid #e5e7eb; margin-bottom:10px; display:flex; align-items:start;"><span style="margin-right:10px; font-size:1.2em;">👉</span><div>{res}</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"### {T['fr']['env_title']}")
        st.markdown(f"<div>{''.join([f'<span class=skill-tag style=margin:5px; display:inline-block;>{t}</span>' for t in exp.get('tags',[])])}</div>", unsafe_allow_html=True)

        st.markdown('<div style="margin-top: 35px;"></div>', unsafe_allow_html=True)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        btns_detail = ""
        block_btn_style = "text-decoration:none; color:white; padding:12px 24px; border-radius:8px; font-weight:700; font-size:1.1rem; display:flex; justify-content:center; align-items:center; width:100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"

        if "github" in exp and exp['github']:
            btns_detail += f"""<a href="{exp['github']}" target="_blank" style="{block_btn_style} background-color:#111827; margin-bottom:12px;">GitHub 🐙</a>"""

        if "report" in exp and exp['report']:
            full_path = os.path.join(current_dir, exp['report'])
            style_pdf_block = f"{block_btn_style} background-color:#FF9F1C;"
            btns_detail += get_pdf_button(full_path, T["fr"]["download_report"], custom_style=style_pdf_block)

        if btns_detail:
             st.markdown(f'<div style="display:flex; flex-direction:column; align-items:stretch;">{btns_detail}</div>', unsafe_allow_html=True)

def show_experience_detail_en(e_id):
    """Display experience details in English"""
    try: 
        # Utilisation explicite de EXPERIENCES_EN
        exp = data.EXPERIENCES_EN[int(e_id)]
    except: st.error("Experience not found."); return

    # Lien de retour avec lang=en
    st.markdown(f'<a href="/?tab=experiences&lang=en" target="_self" class="back-btn">{T["en"]["back_exp"]}</a>', unsafe_allow_html=True)

    st.markdown(f"""
    <div style="padding-bottom:20px; border-bottom:1px solid #e5e7eb; margin-bottom:30px;">
        <h1 style="font-size:2.5rem; margin-bottom:10px; color:#111827;">{exp['role']}</h1>
        <h2 style="font-size:1.5rem; color:#4F46E5; margin-bottom:10px;">at {exp['company']}</h2>
        <span style="background:#EEF2FF; color:#4F46E5; padding:5px 15px; border-radius:20px; font-weight:600;">🗓 {exp['period']}</span>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"### {T['en']['missions_title']}")
        st.markdown(exp['description'], unsafe_allow_html=True)
        st.markdown(f"### {T['en']['results_title']}")
        for res in exp['results']:
            st.markdown(f"""<div style="background:white; padding:15px; border-radius:10px; border:1px solid #e5e7eb; margin-bottom:10px; display:flex; align-items:start;"><span style="margin-right:10px; font-size:1.2em;">👉</span><div>{res}</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"### {T['en']['env_title']}")
        st.markdown(f"<div>{''.join([f'<span class=skill-tag style=margin:5px; display:inline-block;>{t}</span>' for t in exp.get('tags',[])])}</div>", unsafe_allow_html=True)

        st.markdown('<div style="margin-top: 35px;"></div>', unsafe_allow_html=True)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        btns_detail = ""
        block_btn_style = "text-decoration:none; color:white; padding:12px 24px; border-radius:8px; font-weight:700; font-size:1.1rem; display:flex; justify-content:center; align-items:center; width:100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"

        if "github" in exp and exp['github']:
            btns_detail += f"""<a href="{exp['github']}" target="_blank" style="{block_btn_style} background-color:#111827; margin-bottom:12px;">GitHub 🐙</a>"""

        if "report" in exp and exp['report']:
            full_path = os.path.join(current_dir, exp['report'])
            style_pdf_block = f"{block_btn_style} background-color:#FF9F1C;"
            btns_detail += get_pdf_button(full_path, T["en"]["download_report"], custom_style=style_pdf_block)

        if btns_detail:
             st.markdown(f'<div style="display:flex; flex-direction:column; align-items:stretch;">{btns_detail}</div>', unsafe_allow_html=True)


# ==============================================================================
# --- VUE : HOME / PORTFOLIO ---
# ==============================================================================
def show_home_view():
    
    # 1. SIDEBAR (PROFILE)
    with st.sidebar:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "assets", "profile.jpg")
        
        if os.path.exists(file_path):
            st.markdown("""
            <style>
                [data-testid="stSidebar"] img {
                    border-radius: 50%;
                    width: 170px;
                    height: 170px;
                    object-fit: cover;
                    display: block;
                    margin: 0 0 20px 50px; 
                    border: 3px solid #FF9F1C;
                }
            </style>
            """, unsafe_allow_html=True)
            st.image(file_path) 
        else:
            st.warning(f"Image introuvable : {file_path}")

        st.title(current_info["name"])
        st.markdown(f"**{current_info['role']}**")
        st.markdown("---")
        st.markdown(f"📍 {current_info['location']}")
        st.markdown(f"📧 {data.INFO['email']}") 
        st.markdown(f"📱 {data.INFO['phone']}")
        
        st.markdown(f"🐙 <a href='https://github.com/dynmohamed' target='_blank'>GitHub</a>", unsafe_allow_html=True)
        st.markdown(f"🔗 <a href='https://www.linkedin.com/in/mohamed-dyn-301ba6268/' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
    
    # -------------------------------------------------------------
    # CONDITION MAGIQUE : SI UNE DÉMO EST ACTIVE -> MODE IMMERSIF
    # -------------------------------------------------------------
    if st.session_state.current_demo is not None:
        
        st.button(UI["back_demos"], on_click=reset_demo)
        st.divider()

        # LOGIQUE D'AFFICHAGE DES DÉMOS
        demo_key = st.session_state.current_demo
        
        if demo_key == "yolo":
            st.markdown("#### 👁️ Détection d'Objets (YOLOv8)")
            
            st.markdown(f"""
            <div style="margin-bottom: 20px; font-size: 16px; color: #374151; background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #6366F1;">
                {UI['input_pipeline']}
            </div>
            """, unsafe_allow_html=True)

            source_option = st.radio("Source :", ["Upload", "Test Image"], horizontal=True)
            image_file = None
            
            if source_option == "Upload":
                image_file = st.file_uploader("Image (JPG/PNG)...", type=['jpg', 'png', 'jpeg'])
            else:
                sample_options = {
                    "Car": "assets/car.jpg",
                    "Cat": "assets/cat.jpg",
                    "Dog": "assets/dog.jpg",
                    "Person": "assets/humain.jpg",
                    "Train": "assets/train.jpg"
                }
                selected_sample_name = st.selectbox("Sample :", list(sample_options.keys()))
                selected_path = sample_options[selected_sample_name]
                if os.path.exists(selected_path):
                    image_file = selected_path
                else:
                    st.warning(f"⚠️ {selected_path} not found.")

            if image_file:
                from PIL import Image
                from ultralytics import YOLO
                c1, c2 = st.columns(2)
                img = Image.open(image_file)
                with c1:
                    st.image(img, caption="Input", use_column_width=True)

                if st.button(UI["launch_inf"]):
                    with st.spinner("Processing..."):
                        try:
                            model = YOLO('yolov8n.pt') 
                            res = model(img)
                            st.markdown("""
                            <div style="margin-top: 20px; margin-bottom: 15px; font-size: 16px; color: #065F46; background-color: #D1FAE5; padding: 15px; border-radius: 8px; border-left: 5px solid #10B981;">
                                ✅ <b>Done.</b>
                            </div>
                            """, unsafe_allow_html=True)
                            result_img = res[0].plot()
                            with c2:
                                st.image(result_img, caption="Output", use_column_width=True)
                        except Exception as e:
                            st.error(f"Error : {e}")

        elif demo_key == "nlp":
            st.markdown("#### 🧠 Sentiment Analysis (NLP)")
            st.markdown(f"""
            <div style="margin-bottom: 20px; font-size: 16px; color: #374151; background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #8B5CF6;">
                {UI['input_corpus']}
            </div>
            """, unsafe_allow_html=True)
            txt = st.text_area("Text...", height=100, placeholder="Ex: The service was excellent but the wait time was too long.")

            if st.button(UI["launch_ana"]) and txt:
                with st.spinner("Analysing..."):
                    from textblob import TextBlob
                    blob = TextBlob(txt)
                    pol = blob.sentiment.polarity
                    st.divider()
                    if pol > 0.1:
                        st.success(f"POSITIVE (Score: {pol:.2f})")
                        st.balloons()
                    elif pol < -0.1:
                        st.error(f"NEGATIVE (Score: {pol:.2f})")
                    else:
                        st.warning(f"NEUTRAL (Score: {pol:.2f})")

        elif demo_key == "chatbot":
            st.markdown("#### 🩺 Assistant Médical (IA Générative)")
            try:
                api_key = st.secrets["GEMINI_API_KEY"]
            except:
                st.error("🚨 Clé API manquante dans st.secrets.")
                st.stop()
            import google.generativeai as genai
            model = None
            try:
                genai.configure(api_key=api_key)
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                target_model = next((m for m in available_models if 'flash' in m), available_models[0]) if available_models else None
                if target_model: model = genai.GenerativeModel(target_model)
            except Exception as e: st.error(f"Error: {e}")

            if "messages" not in st.session_state:
                st.session_state.messages = [{"role": "assistant", "content": f"{UI['bng']}"}]

            for message in st.session_state.messages:
                avatar = "🩺" if message["role"] == "assistant" else "👤"
                with st.chat_message(message["role"], avatar=avatar):
                    st.markdown(message["content"])

            if prompt := st.chat_input("Symptoms..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user", avatar="👤"):
                    st.markdown(prompt)

                if model:
                    with st.chat_message("assistant", avatar="🩺"):
                        with st.spinner("thinking..."):
                            try:
                                conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
                                system_instruction = f"{UI['prompto']}"
                                full_prompt = f"{system_instruction}\n{conversation_history}\nassistant:"
                                response = model.generate_content(full_prompt)
                                bot_reply = response.text
                                st.markdown(bot_reply)
                                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                            except Exception as e: st.error(f"Error: {e}")

        elif demo_key == "fraude":
            import pandas as pd
            import numpy as np
            import time

            st.markdown("#### 🛡️ Fraud Detection & Risk Scoring")
            
            # Message d'explication plus clair
            st.markdown(f"""
            <div style="margin-bottom: 20px; font-size: 0.95rem; color: #374151; background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #4F46E5;">
                {UI['input_meta']}
                <br><i>💡 Essayez des combinaisons risquées (ex: <b>Crypto</b> + <b>Nigeria</b> + <b>Montant élevé</b> + <b>3h du matin</b>) pour déclencher l'IA.</i>
            </div>
            """, unsafe_allow_html=True)

            col_input, col_viz = st.columns([1, 1.2], gap="large")
            
            with col_input:
                st.subheader("Paramètres de la Transaction")
                montant = st.number_input("Montant ($)", 0, 20000, 1000, step=100)
                heure = st.slider("Heure de la transaction (0h-23h)", 0, 23, 14)
                type_trans = st.selectbox("Type de paiement", ["Carte Bancaire", "Virement", "Crypto-monnaie"], index=0)
                pays = st.selectbox("Pays IP", ["France", "USA", "Allemagne", "Maroc", "Russie", "Nigeria"], index=3)
                categorie = st.selectbox("Catégorie", ["Alimentation", "Transport", "Santé", "Luxe", "Jeux d'argent", "Électronique"], index=0)
                
                st.write("") # Spacer
                btn_predict = st.button(UI["launch_risk"], use_container_width=True)

            with col_viz:
                st.subheader("Analyse de Risque IA")
                if btn_predict:
                    with st.spinner("Analyse des vecteurs de fraude en cours..."):
                        time.sleep(0.8) # Petit délai pour l'effet "calcul"

                        # --- LOGIQUE DE SCORING (SIMULATION RÉALISTE) ---
                        # On calcule un score de probabilité basé sur des poids (Features Importance)
                        risk_score = 0
                        
                        # 1. Analyse du Montant (Plus c'est haut, plus c'est risqué)
                        if montant > 10000: risk_score += 40
                        elif montant > 5000: risk_score += 25
                        elif montant > 1000: risk_score += 10

                        # 2. Analyse Géographique
                        if pays in ["Russie", "Nigeria"]: risk_score += 30
                        elif pays == "USA": risk_score += 10
                        
                        # 3. Analyse Temporelle (La nuit c'est louche)
                        if 1 <= heure <= 5: risk_score += 20
                        
                        # 4. Type & Catégorie
                        if type_trans == "Crypto-monnaie": risk_score += 25
                        if categorie == "Paris en ligne (Gambling)": risk_score += 20
                        elif categorie == "Luxe / Bijoux": risk_score += 15

                        # Normalisation (Max 99%)
                        final_risk = min(risk_score, 99)
                        # On ajoute un tout petit peu d'aléatoire pour faire "vivant"
                        if final_risk > 0:
                            final_risk += np.random.randint(-2, 3)
                        final_risk = max(0, min(final_risk, 99))

                        # --- AFFICHAGE DU RÉSULTAT ---
                        
                        # Création de la jauge de couleur
                        bar_color = "green"
                        if final_risk > 75: bar_color = "red"
                        elif final_risk > 40: bar_color = "orange"

                        # Affichage conditionnel
                        if final_risk > 75:
                            st.error(f"🚨 **ALERTE FRAUDE DÉTECTÉE**")
                            st.markdown("La transaction a été **bloquée** par le modèle de sécurité.")
                        elif final_risk > 40:
                            st.warning(f"⚠️ **TRANSACTION SUSPECTE**")
                            st.markdown("La transaction nécessite une **vérification manuelle** (2FA).")
                        else:
                            st.success(f"✅ **TRANSACTION LÉGITIME**")
                            st.markdown("Aucune anomalie détectée.")

                        # Jauge de probabilité
                        st.write(f"**Probabilité de fraude : {final_risk}%**")
                        st.progress(final_risk / 100, text=None)

                        # Détails techniques (pour faire "Data Science")
                        with st.expander("Voir les facteurs de décision (Explainability)"):
                            st.write("Facteurs principaux ayant influencé le score :")
                            factors = {}
                            if montant > 5000: factors["Montant Élevé"] = "+High"
                            if pays in ["Russie", "Nigeria"]: factors["Pays à Risque"] = "+Critical"
                            if type_trans == "Crypto-monnaie": factors["Moyen de Paiement"] = "+Medium"
                            if 1 <= heure <= 5: factors["Horaire Atypique"] = "+Medium"
                            
                            if not factors:
                                st.write("- Comportement standard (Normal)")
                            else:
                                st.json(factors)

                else:
                    # État initial (vide)
                    st.info("👈 Configurez la transaction et lancez l'analyse.")
                    st.image("https://cdn-icons-png.flaticon.com/512/6393/6393411.png", width=100)
    # -------------------------------------------------------------
    # MODE PORTFOLIO CLASSIQUE (Header + Menu + Contenu)
    # -------------------------------------------------------------
    else:
        # A. HEADER
        c1, c2, c3 = st.columns([3, 1, 0.5])
        
        with c1:
            st.markdown(f"<h1 style='font-size:3.5rem; margin-top: -10px;'>{UI['greeting']} <span style='color:#4F46E5'>{current_info['name']}</span></h1>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='font-size:1.5rem; color:#4B5563'>{current_info['role']}</p>", unsafe_allow_html=True)
        with c2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(UI["cv_title"])
            cv_col1, cv_col2 = st.columns(2)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            path_fr = os.path.join(current_dir, "assets", "CV_Mohamed_Dyn_FR.pdf")
            with cv_col1:
                if os.path.exists(path_fr):
                    with open(path_fr, "rb") as f:
                        st.download_button(label="FR", data=f, file_name="CV_Mohamed_Dyn_FR.pdf", mime="application/pdf", use_container_width=True)
                else: st.warning("FR?")
            path_en = os.path.join(current_dir, "assets", "CV_Mohamed_Dyn_EN.pdf")
            with cv_col2:
                if os.path.exists(path_en):
                    with open(path_en, "rb") as f:
                        st.download_button(label="EN", data=f, file_name="CV_Mohamed_Dyn_EN.pdf", mime="application/pdf", use_container_width=True)
                else: st.warning("EN?")
        
        # COLONNE 3 : SÉLECTEUR DE LANGUE (Avec mise à jour URL)
        with c3:
            st.markdown("<br>", unsafe_allow_html=True)
            flag_fr = "https://flagcdn.com/w40/fr.png"
            flag_en = "https://flagcdn.com/w40/gb.png"
            
            current_flag = flag_fr if lang == 'fr' else flag_en
            current_code = "FR" if lang == 'fr' else "EN"
            
            popover = st.popover(f"{current_code}", use_container_width=True)
            
            with popover:
                st.caption("Language / Langue")
                type_fr = "primary" if lang == 'fr' else "secondary"
                type_en = "primary" if lang == 'en' else "secondary"
                if st.button("Français", type=type_fr, use_container_width=True):
                    st.session_state.language = 'fr'
                    st.query_params["lang"] = "fr" 
                    st.rerun()
                
                # 3. On applique la couleur au bouton Anglais
                # AJOUTEZ : type=type_en
                if st.button("English", type=type_en, use_container_width=True):
                    st.session_state.language = 'en'
                    st.query_params["lang"] = "en" 
                    st.rerun()
              

            st.markdown(f"""
            <style>
                div[data-testid="column"]:nth-of-type(3) button[kind="secondary"] {{
                    border: 1px solid #ddd;
                    background-color: #F2F4F8;
                    color: #333;
                    font-weight: bold;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 5px;
                    padding-left: 30px; 
                    background-image: url('{current_flag}');
                    background-size: 20px;
                    background-repeat: no-repeat;
                    background-position: 10px center;
                    width: 90px;
                    height: 20px;
                }}
            </style>
            """, unsafe_allow_html=True)
        
        # --- TEXTE DE PRÉSENTATION ---
        st.markdown(UI["bio_html"], unsafe_allow_html=True)

        # --- LE "NUDGE" PRO ---
        st.markdown(UI["nudge_text"], unsafe_allow_html=True)

        # B. MENU DE NAVIGATION
        default_index = 0
        if active_tab == "experiences": default_index = 1
        elif active_tab == "competences": default_index = 2
        elif active_tab == "demos": default_index = 3
        elif active_tab == "contact": default_index = 4
        
        # Synchronisation Menu
        if active_tab == "demos": st.session_state["nav_menu"] = UI["menu_items"][3]
        elif active_tab == "experiences": st.session_state["nav_menu"] = UI["menu_items"][1]
        elif active_tab == "competences": st.session_state["nav_menu"] = UI["menu_items"][2]
        elif active_tab == "contact": st.session_state["nav_menu"] = UI["menu_items"][4]
        elif active_tab == "projets" or not active_tab: st.session_state["nav_menu"] = UI["menu_items"][0]

        selected = option_menu(
            menu_title=None,
            options=UI["menu_items"],
            icons=["rocket-takeoff", "briefcase", "tools", "play-circle-fill", "envelope-at"],
            default_index=default_index,
            orientation="horizontal",
            key="nav_menu",
            on_change=on_menu_change,
            styles={
                "container": {"padding": "0!important", "background-color": "#ffffff", "border": "1px solid #e5e7eb"},
                "icon": {"color": "#6B7280", "font-size": "14px"}, 
                "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "--hover-color": "#fff7ed"}, 
                "nav-link-selected": {"background-color": "#FF9F1C", "color": "white", "font-weight": "700"},
            }
        )
        
        st.divider()

        # D. CONTENU STANDARD

        # 1. PROJETS
        if selected == UI["menu_items"][0]:
            st.session_state.current_demo = None
            st.markdown(UI["section_projects"])
            col1, col2 = st.columns(2)
            for i, p in enumerate(current_projects_list):
                with (col1 if i % 2 == 0 else col2):
                    tags = "".join([f'<span class="skill-tag">{t}</span>' for t in p["tech"]])
                    btn_github = ""
                    if "link" in p:
                        btn_github = f"""<a href="{p['link']}" target="_blank" style="text-decoration: none; background-color: #111827; color: white; padding: 8px 12px; border-radius: 6px; font-weight: 600; font-size: 0.9rem; display: inline-flex; align-items: center; margin-right: 8px;">{UI['github_btn']}</a>"""
                    btn_demo = ""
                    if "demo_key" in p:
                        link_demo = f"/?tab=demos&demo_id={p['demo_key']}&lang={lang}"
                        btn_demo = f"""<a href="{link_demo}" target="_self" style="text-decoration: none; background-color: #FF9F1C; color: white; padding: 8px 12px; border-radius: 6px; font-weight: 600; font-size: 0.9rem; display: inline-flex; align-items: center;">{UI['demo_btn']}</a>"""

                    # Notez l'ajout de &lang={lang} dans le href du lien En savoir plus
                    html_card = f"""<div class="project-card-container" style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; background: white; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: flex; flex-direction: column; height: 100%;">
    <a href="/?project_id={i}&lang={lang}" target="_self" style="text-decoration: none; color: inherit; flex-grow: 1; display: block;">
    <h3 style="margin: 0 0 10px 0; color: #111827; font-size: 1.3rem; font-weight: 700;">{p['title']}</h3>
    <div style="color: #6B7280; font-size: 0.9rem; margin-bottom: 15px; font-weight: 500;">{p['type']}</div>
    <p style="color: #374151; font-size: 1rem; line-height: 1.6; margin-bottom: 20px;">{p['desc'][:150]}...</p>
    <div style="margin-bottom: 20px;">{tags}</div>
    </a>
    <div style="border-top: 1px solid #f3f4f6; padding-top: 15px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
    <div style="display: flex; align-items: center;">{btn_github}{btn_demo}</div>
    <a href="/?project_id={i}&lang={lang}" target="_self" style="color: #4F46E5; text-decoration: none; font-weight: 600;">{UI['more_btn']}</a>
    </div>
    </div>"""
                    st.markdown(html_card, unsafe_allow_html=True)
                    st.write("") 

        # 2. EXPÉRIENCES
        elif selected == UI["menu_items"][1]:
            st.session_state.current_demo = None
            st.markdown(UI["section_exp"])
            current_dir = os.path.dirname(os.path.abspath(__file__))
            btn_style = "text-decoration:none; color:white; padding:10px 20px; border-radius:8px; font-weight:700; font-size:1rem; display:inline-flex; align-items:center; justify-content:center; line-height:1.2; box-shadow: 0 2px 5px rgba(0,0,0,0.1);"

            for i, exp in enumerate(current_experiences_list):
                buttons_html = ""
                if "github" in exp and exp['github']:
                    buttons_html += f"""<a href="{exp['github']}" target="_blank" style="{btn_style} background-color:#111827; margin-right:12px;">GitHub 🐙</a>"""
                if "report" in exp and exp['report']:
                    full_path = os.path.join(current_dir, exp['report'])
                    style_pdf = f"{btn_style} background-color:#FF9F1C;"
                    buttons_html += get_pdf_button(full_path, UI["download_report"], custom_style=style_pdf)

                # Lien vers le détail avec la langue
                link_detail = f"/?exp_id={i}&tab=experiences&lang={lang}"

                st.markdown(f"""
    <div class="timeline-item" style="margin-bottom:20px;">
    <div class="timeline-card" style="border:1px solid #e5e7eb; padding:20px; border-radius:12px; background:white; position:relative; box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <div style="display:flex; justify-content:space-between; align-items:center;">
    <a href="{link_detail}" target="_self" style="text-decoration:none; color:#111827; flex-grow:1;">
    <h3 style="margin:0; font-size:1.3rem; font-weight:700;">{exp['role']}</h3>
    </a>
    </div>
    <p style="color:#4F46E5; font-weight:600; margin-top:5px;">{exp['company']}</p>
    <p style="color:#6B7280; font-size:0.9em; margin-bottom:10px;">{exp['period']}</p>
    <p style="color:#374151; line-height:1.6;">{exp['desc']}</p>
    <div style="margin-top: 20px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
    <div style="display:flex; align-items:center;">{buttons_html}</div>
    <a href="{link_detail}" target="_self" style="color:#4F46E5; font-weight:600; font-size:0.9em; text-decoration:none;">{UI['more_btn']}</a>
    </div>
    </div>
    </div>""", unsafe_allow_html=True)
                
        # 3. COMPÉTENCES
        elif selected == UI["menu_items"][2]:
            st.markdown(UI["section_skills"])
            for category, skills in current_skills.items():
                skills_html = "".join([f'<span class="tech-badge">{skill}</span>' for skill in skills])
                st.markdown(f"""<div class="skill-box"><div class="skill-category-title">🔹 {category}</div><div>{skills_html}</div></div>""", unsafe_allow_html=True)

        # 4. DÉMOS LIVE
        elif selected == UI["menu_items"][3]:
            st.markdown(UI["section_demos"])
            st.info(UI["demo_info"])
            st.markdown("""
            <style>
            /* Force le bouton à ne pas couper le texte et à s'adapter */
            div[data-testid="stButton"] button {
                white-space: nowrap;
                min-width: 100%;
            }
            </style>
            """, unsafe_allow_html=True)
            # ---------------------------
            cols = st.columns(3)
            for i, demo in enumerate(current_demos_list):
                with cols[i % 3]: 
                    with st.container(border=True):
                        st.markdown(f"#### {demo['title']}")
                        st.caption(demo['desc'])
                        st.button(demo['btn_label'], key=f"btn_{demo['key']}", use_container_width=True, on_click=set_demo, args=(demo['key'],))
        # 5. CONTACT
        elif selected == UI["menu_items"][4]:
            st.session_state.current_demo = None
            st.markdown(UI["section_contact"])
            
            st.markdown(UI["contact_intro"], unsafe_allow_html=True)

            c1, c2 = st.columns([1, 1.5], gap="large")

            with c1:
                st.markdown(UI["coord_title"])
                st.markdown(f"""
                <div style="font-size: 1.05rem; line-height: 2.2; color: #374151;">
                    <div>📧 <strong>Email :</strong><br>
                        <a href="mailto:{data.INFO['email']}" style="text-decoration:none; color:#4F46E5; font-weight:500;">{data.INFO['email']}</a>
                    </div>
                    <div style="margin-top: 15px;">📱 <strong>Téléphone :</strong><br>
                        <span style="color:#111827;">{data.INFO['phone']}</span>
                    </div>
                    <div style="margin-top: 15px;">🌍 <strong>Localisation :</strong><br>
                        <span style="color:#111827;">{current_info['location']}</span>
                    </div>
                    <div style="margin-top: 30px;">
                        <a href="{data.INFO['linkedin']}" target="_blank" style="display:inline-block; background-color: #0A66C2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.95rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            {UI['linkedin_btn']}
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True) 

            # --- COLONNE 2 : LE FORMULAIRE ---
            with c2:
                st.markdown(UI["msg_title"])
                st.markdown(f"""
                <p style="font-size: 0.95rem; color: #6B7280; margin-bottom: 15px;">
                    {UI['msg_subtitle']}
                </p>
                """, unsafe_allow_html=True)

                with st.form("contact_form"):
                    name = st.text_input(UI["form_name"])
                    email = st.text_input(UI["form_email"])
                    message = st.text_area(UI["form_msg"], height=150)
                    
                    submit_button = st.form_submit_button(UI["form_btn"], use_container_width=True)
                    
                    if submit_button:
                        if not name or not email or not message:
                            st.warning(UI["form_error"])
                        else:
                            try:
                                formspree_url = "https://formspree.io/f/mlgeerad" 
                                response = requests.post(
                                    formspree_url,
                                    json={"name": name, "email": email, "message": message}
                                )
                                if response.status_code == 200:
                                    st.success(UI["form_success"])
                                    st.balloons()
                                else:
                                    st.error("Error.")
                            except Exception as e:
                                st.error(f"Error : {e}")


# --- MAIN ROUTER ---

if project_id:
    if lang == 'en':
        show_project_detail_en(project_id)
    else:
        show_project_detail(project_id)
elif exp_id:
    if lang == 'en':
        show_experience_detail_en(exp_id)
    else:
        show_experience_detail(exp_id)
else:
    show_home_view()