# content.py

INFO = {
    "name": "Mohamed Dyn",
    "role": "Ingénieur Data Science & Data Engineering",
    "school": "INSEA (3ème année)",
    "location": "Rabat, Maroc",
    "email": "contact@mohameddyn.me",
    "linkedin": "https://www.linkedin.com/in/mohamed-dyn-301ba6268/",
    "phone": "+212 657 722 751",
    "summary": """
    Élève-ingénieur en dernière année à l'INSEA, je fusionne Data Engineering, IA Générative et Analytics. 
    Je recherche un stage PFE pour transformer des données complexes en solutions stratégiques.
    """
}

SKILLS = {
    "Cloud & DevOps": ["AWS (Glue, Lambda, Redshift)", "Azure (Data Factory, Databricks)", "Docker", "CI/CD"],
    "Data Engineering": ["Spark (PySpark)", "Airflow", "Databricks", "DBT", "Kafka", "Hadoop", "DBT", "ETL/ELT"],
    "Data Science & AI": ["LLMs & RAG", "LangChain", "Machine Learning", "TensorFlow", "MLOps"],
    "Languages": ["Python (Avancé)", "SQL (Avancé)", "Scala", "Java"],
    "BI & Viz": ["Power BI", "Tableau", "AWS QuickSight"]
}

# Dans content.py

EXPERIENCES = [
{
        "role": "Data Scientist (Stagiaire)",
        "company": "TEMACONCEPT",
        "period": "Juil. 2023 - sept. 2023",
        "github": "https://github.com/dynmohamed/Affectation-des-professeurs-CPGE-AI-chatbot",
        "report": "assets/rapport_de_stage_PFA_dyn_mohamed.pdf",
        "desc": "Développement d'un moteur d'optimisation pour l'affectation des enseignants CPGE et conception d'un système RAG.",
        
# DESCRIPTION HTML : Narrative, Technique et Fluide
        "description": """
<div style="text-align: justify;">
            Ce projet stratégique visait à refondre intégralement le processus d'affectation des enseignants CPGE, jusqu'alors géré manuellement face à une <b>complexité combinatoire exponentielle</b>. 
            <br><br>
            Mon intervention s'est d'abord portée sur la modélisation mathématique du problème (Linear Assignment Problem). J'ai implémenté l'<b>algorithme Hongrois (Kuhn-Munkres)</b> pour traiter simultanément des contraintes multidimensionnelles strictes (géographie, spécialité, rang pédagogique) et garantir une optimalité mathématique impossible à atteindre humainement.
            <br><br>
            Pour assurer l'adoption de l'outil par les métiers et éviter l'effet "boîte noire", j'ai conçu un module d'<b>IA Générative (RAG)</b> connecté aux résultats. Ce système permet aux responsables RH d'interroger les affectations en langage naturel (ex: <i>"Pourquoi ce candidat n'a pas eu son vœu n°1 ?"</i>), apportant ainsi une transparence cruciale pour l'aide à la décision stratégique.
         </div>
        """,
        
        # LES CHIFFRES CLÉS RESTENT EN DESSOUS POUR L'IMPACT VISUEL
        "results": [
            "⚡ <b>Gain de temps massif :</b> Passage d'un traitement de 5 jours à seulement 2 heures (-95%).",
            "🎯 <b>Optimisation :</b> Maximisation mathématique de la satisfaction des vœux (100% de couverture).",
            "🤖 <b>Innovation :</b> Hybridation réussie entre Recherche Opérationnelle (Optimisation) et GenAI (Explicabilité)."
        ],
        
        "tags": ["Python", "Recherche Opérationnelle", "Algorithme Hongrois", "RAG", "LangChain"]
    },
{
        "role": "Data Analyst (Stagiaire)",
        "company": "Ministère chargé des Relations avec le Parlement",
        "period": "Juil. 2024 - Août 2024",
        # Pas de GitHub pour celui-ci, juste le rapport
        "report": "assets/Rapport_du_stage_de_decouverte_DynMohamed.pdf",
        "desc": "Conception de tableaux de bord pour le suivi des activités parlementaires.",
       
        # DESCRIPTION: Focus sur la BI, la Stratégie et la Rigueur
        "description": """
        <div style="text-align: justify;">
            Au cœur de la transformation numérique de l'administration, ma mission consistait à moderniser le pilotage des activités parlementaires (Questions écrites/orales, propositions de loi).
            <br><br>
            J'ai piloté la conception d'une <b>architecture décisionnelle (Business Intelligence)</b> complète. Partant de données brutes et dispersées, j'ai réalisé un travail approfondi de <b>Data Cleaning</b> et de modélisation (Star Schema) pour garantir l'intégrité des indicateurs.
            <br><br>
            L'aboutissement a été le déploiement de tableaux de bord <b>Power BI</b> interactifs. En utilisant des mesures <b>DAX avancées</b>, j'ai fourni aux décideurs une vue en temps réel sur les délais de réponse et les thématiques législatives, transformant une gestion administrative en un véritable <b>pilotage stratégique par la donnée</b>.
        </div>
        """,
        
        # RESULTATS: Impact sur la décision et la qualité
        "results": [
            "📊 <b>Gouvernance :</b> Création d'une 'Single Source of Truth' fiable pour les statistiques du Ministère.",
            "⚡ <b>Aide à la décision :</b> Identification immédiate des goulots d'étranglement (retards de réponse) grâce aux visuels dynamiques.",
            "🛠️ <b>Technique :</b> Modélisation de données optimisée pour des performances de filtrage instantanées."
        ],
        
        "tags": ["Power BI", "DAX", "Data Modeling", "SQL", "Gouvernance des données"]
    },
]

# --- TRES IMPORTANT : AJOUTEZ CECI A LA TOUTE FIN DU FICHIER content.py ---
# Sans cela, vous aurez l'erreur "module content has no attribute DATA"
DATA = {
    "EXPERIENCES": EXPERIENCES,
    "SKILLS": {
        "💻 Langages & BDD": [
            "Python", "SQL", "Java", "C++", "NoSQL", "MongoDB","PostgreSQL"
        ],
        "🧠 Data Science & AI": [
            "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", 
            "Scikit-Learn", "NLP", "Computer Vision", "LLMs (Gemini/GPT)"
        ],
        "⚙️ Data Engineering": [
            "Spark", "Hadoop", "Kafka", "Databricks", "DBT", "Airflow", "ETL Pipelines", "Big Data"
        ],
        "☁️ Cloud & DevOps": [
            "AWS", "Azure", "Docker", "Kubernetes", "Git/GitHub", "CI/CD", "Linux"
        ],
        "📊 Visualisation": [
            "Streamlit", "PowerBI", "Tableau", "Matplotlib", "Seaborn"
        ]
    }
}
# Fusion des projets CV (Business) et GitHub (Tech)
PROJECTS = [
    # --- PROJETS DU CV (Priorité Business) ---
    {
        "title": "Clinical Decision Support System (GenAI)",
        "type": "GenAI / MLOps",
        "period": "Projet Personnel Avancé",
        # 1. Le Hook : On définit le problème technique tout de suite
        "desc": "Moteur d'inférence médical sécurisé (RAG) avec boucle d'alignement expert (RLHF/DPO).",
        
        # 2. Stack de Production (Montre que vous savez déployer, pas juste coder)
        "tech": [
            "Llama-3 (Quantized 4-bit)", # Modèle optimisé
            "LangChain & ChromaDB",      # Orchestration & Vector Store
            "FastAPI (Async)",           # Backend performant
            "Python (Async IO)",         # Pour la performance
            "RLHF (DPO)"                 # Alignement avancé
        ],
        
        "link": "https://github.com/dynmohamed/Medical-chatbot-generative-AI",
        "demo_key": "chatbot",

        # 3. L'Histoire Technique (Architecture & Flux de données)
        "details": """
        <strong>Situation :</strong> L'usage des LLMs standards en milieu médical est critique en raison des "hallucinations" (taux d'erreur ~15-20%) et des risques de fuite de données patients.
        <br><br>
        <strong>Architecture & Solution :</strong>
        Conception d'un système <strong>RAG (Retrieval-Augmented Generation)</strong> "Privacy-First" déployable sur site (On-Premise).
        <ul>
            <li><strong>Ingestion Pipeline :</strong> ETL personnalisé traitant des documents hétérogènes (PDF, Protocoles HTML) avec un <i>Recursive Character Splitter</i> pour préserver le contexte sémantique.</li>
            <li><strong>Moteur de Recherche Hybride :</strong> Combinaison de recherche vectorielle (Dense Retrieval) et par mots-clés (BM25) via <strong>ChromaDB</strong> pour maximiser le rappel (Recall) des informations médicales.</li>
            <li><strong>Boucle d'Alignement (RLHF) :</strong> Implémentation d'un module de feedback utilisateur collectant les préférences (A/B Testing) pour affiner le modèle via <strong>DPO (Direct Preference Optimization)</strong>.</li>
        </ul>
        """,
        
        # 4. Impact Chiffré & KPI (Langage Recruteur)
        "impact": """
        🛡️ <b>Fiabilité Critique :</b> Élimination des hallucinations via <i>Strict Fact-Grounding</i> (chaque réponse cite sa source).<br>
        ⚡ <b>Performance :</b> Latence d'inférence réduite de 5s à <b>1.2s</b> grâce à la quantification 4-bit du modèle Llama-3.<br>
        ⚡ <b>Accessibilité :</b> Transformation d'un modèle complexe en une interface web simple utilisable par non-techniciens.        """,

        # 5. Challenges (Preuve de compétence en résolution de problèmes)
        "challenges": [
            "Réduction de la latence RAG (Optimisation du Top-K retrieval)",
            "Gestion du 'Lost in the Middle' (Reranking des documents)",
            "Alignement du ton médical (Prompt Engineering avancé & Few-Shot)"
        ]
    },
    {
        "title": "Real-time Financial Fraud Detection",
        "type": "FinTech / Cybersec",
        "period": "Projet GitHub",
        "desc": "Système de détection d'anomalies hybride (Supervisé/Non-supervisé) pour sécuriser les flux financiers en temps réel.",
        
        "tech": [
            "Scikit-Learn (Isolation Forest)",
            "XGBoost (Gradient Boosting)",
         
            "SHAP (Explainability)",
            "Pandas (Time-series features)"
        ],
        
        "link": "https://github.com/dynmohamed/detection-de-fraude-en-temps-reel",
        "demo_key": "fraude",

        "details": """
        <strong>Problématique Métier :</strong> La détection de fraude est un problème de "déséquilibre extrême" (Imbalanced Classification) : moins de 0.1% des transactions sont frauduleuses. Les modèles classiques biaisent vers la classe majoritaire et ratent les fraudes.
        <br><br>
        <strong>Approche Data Science Avancée :</strong>
        <ul>
        <li><strong>1. Feature Engineering Temporel :</strong> Les données brutes (Montant, Heure) ne suffisent pas. J'ai créé des agrégats temporels complexes (Rolling Windows) : 
            <i>"Moyenne des dépenses des dernières 24h"</i>, <i>"Écart-type des transactions vs historique client"</i>, <i>"Vitesse géographique entre deux paiements"</i>.</li>
            
        <li><strong>2. Stratégie de Modélisation Hybride :</strong>
                <br>- <b>Isolation Forest (Non-supervisé) :</b> Pour détecter les "Outliers" inconnus (nouveaux modes opératoires de fraudeurs).
                <br>- <b>XGBoost (Supervisé) :</b> Entraîné sur les fraudes historiques pour classifier les attaques connues avec une haute précision.</li>
            
        <li><strong>3. Gestion du Déséquilibre :</strong> Application de la technique <strong>SMOTE</strong> (Synthetic Minority Over-sampling Technique) pendant l'entraînement pour générer des fraudes synthétiques et forcer le modèle à apprendre les caractéristiques de la classe minoritaire.</li>
        </ul>
        """,
        
        "impact": """
        ⚖️ <b>Performance Métier :</b> Maximisation du <b>F1-Score</b> plutôt que de l'Accuracy, permettant de réduire les Faux Négatifs (fraudes ratées) sans bloquer les clients légitimes (Faux Positifs).<br>
        🔍 <b>Explainable AI (XAI) :</b> Intégration de la librairie <b>SHAP</b> pour générer une explication locale pour chaque alerte (ex: "Transaction bloquée car montant 5x supérieur à la moyenne habituelle").<br>
        ⏱️ <b>Inférence Temps Réel :</b> Pipeline optimisé capable de traiter une transaction et renvoyer un score de risque en millisecondes.
        """,

        "challenges": [
            "Lutte contre le 'Concept Drift' (les schémas de fraude évoluent dans le temps)",
            "Risque d'Overfitting sur les données synthétiques générées par SMOTE",
            "Nettoyage des données bruitées (valeurs manquantes, formats incohérents)"
        ]
    },
    {
        "title": "Détection d'Objets (YOLOv8)",
        "type": "Computer Vision",
        "period": "GitHub / Research",
        "desc": "Système de vision par ordinateur temps réel pour la détection d'objets spécifiques (Custom Dataset).",
        
        "tech": [
            "YOLOv8 (Ultralytics)", 
            "OpenCV (Image Processing)", 
            "PyTorch", 
            "Albumentations (Augmentation)", 
            "CUDA (GPU Acceleration)"
        ],
        "link": "https://github.com/dynmohamed/Custom-Object-Detection-using-YOLOv8",
        "demo_key": "yolo",
        
        "details": """
        <strong>Défi Technique :</strong> Les modèles pré-entraînés (COCO dataset) échouent à détecter des objets spécifiques ou rares dans des environnements industriels complexes (éclairage variable, occultations).
        <br><br>
        <strong>Stratégie MLOps :</strong>
        <ul>
            <li><strong>Data Curation :</strong> Constitution et annotation manuelle d'un dataset propriétaire via <b>Roboflow</b>.</li>
            <li><strong>Data Augmentation Avancée :</strong> Application de transformations robustes (Mosaïque, Flou gaussien, Cutout) avec la librairie <b>Albumentations</b> pour forcer le modèle à généraliser et éviter l'overfitting.</li>
            <li><strong>Transfer Learning :</strong> Fine-tuning de l'architecture YOLOv8 nano pour atteindre un compromis optimal entre vitesse (FPS) et précision (mAP).</li>
        </ul>
        """,
        
        "impact": """
        👁️ <b>Précision :</b> Atteinte d'un <b>mAP@50 de 0.92</b> sur le jeu de test, surpassant les modèles génériques.<br>
        ⏱️ <b>Temps Réel :</b> Inférence stable à <b>30+ FPS</b> sur GPU standard, permettant un déploiement sur flux vidéo live.<br>
        📦 <b>Déploiement :</b> Export du modèle au format ONNX pour une interopérabilité maximale.
        """,

        "challenges": [
            "Gestion des faux positifs dus aux arrière-plans complexes",
            "Équilibrage des classes (certains objets étaient sous-représentés)",
            "Optimisation des hyperparamètres (Learning Rate, Batch Size) pour la convergence"
        ]
    },
    {
        "title": "Sentiment Analysis",
        "type": "NLP / MLOps",
        "period": "Projet académique",
        "desc": "API de classification de texte ultra-rapide (<50ms) pour l'analyse de tonalité en temps réel.",
        
        "tech": [
            "NLTK (Preprocessing)", 
            "Scikit-Learn (TF-IDF & SVM)", 
            "Flask (API Serving)", 
            "Pickle (Serialization)",
            "Python"
        ],
        "link": "https://github.com/dynmohamed/sentiment-prediction",
        "demo_key": "nlp",
        
        "details": """
        <strong>Contexte Engineering :</strong> Les modèles de Deep Learning (comme BERT) sont parfois "trop lourds" (overkill) pour des tâches simples nécessitant une latence minimale (ex: modération de chat en direct).
        <br><br>
        <strong>Approche "Lightweight" :</strong>
        <ul>
            <li><strong>NLP Pipeline Classique :</strong> Implémentation d'une chaîne de traitement robuste : Nettoyage (Regex) ➔ Stopwords removal ➔ Stemming (Snowball) ➔ Vectorisation (TF-IDF).</li>
            <li><strong>Modélisation Statistique :</strong> Choix d'un algorithme <b>SVM (Support Vector Machine)</b> ou <b>Naive Bayes</b> pour leur efficacité redoutable sur des données textuelles éparses, offrant un compromis vitesse/précision idéal.</li>
            <li><strong>Model Serving :</strong> Encapsulation du modèle dans une <b>API REST (Flask)</b>. Le modèle est sérialisé (Pickle) au démarrage pour garantir des réponses instantanées aux requêtes HTTP.</li>
        </ul>
        """,
        
        "impact": """
        🚀 <b>Latence Ultra-Faible :</b> Temps d'inférence sous les <b>20ms</b>, permettant une intégration synchrone dans des applications web.<br>
        🔧 <b>Intégrabilité :</b> Architecture micro-service découplée, facile à consommer par n'importe quel front-end.<br>
        📉 <b>Efficacité :</b> Consommation mémoire minime (<200MB RAM) comparée aux modèles Transformers (>2GB).
        """,

        "challenges": [
            "Gestion des négations (ex: 'Pas mal' doit être positif)",
            "Réduction de la dimensionnalité du vocabulaire (Feature Selection)",
            "Nettoyage des caractères spéciaux et Emojis"
        ]
    },

    {
        "title": "Architecture ELT Serverless (AWS)",
        "type": "Data Engineering / Cloud",
        "period": "Mars 2025",
        "desc": "Pipeline 'Event-Driven' entièrement automatisé sur AWS (Zero-Infrastructure).",
        
        "tech": [
            "AWS Glue (Spark Jobs)", 
            "AWS Lambda (Triggers)", 
            "Amazon S3 (Data Lake)", 
            "Redshift (Data Warehousing)", 
            "IAC (Terraform)"
        ],
        
        "details": """
        <strong>Défi Infrastructure :</strong> L'entreprise traitait ses logs via des scripts manuels, causant une latence de 24h et des coûts de maintenance élevés (serveurs EC2 inactifs 80% du temps).
        <br><br>
        <strong>Solution Serverless :</strong> Conception d'une architecture réactive :
        <ul>
            <li><strong>Ingestion Event-Driven :</strong> Utilisation de <b>S3 Event Notifications</b> pour déclencher une fonction <b>AWS Lambda</b> dès l'arrivée d'un fichier, éliminant le besoin d'orchestrateur externe pour les tâches simples.</li>
            <li><strong>Transformation Scalable :</strong> Jobs <b>AWS Glue</b> (PySpark) pour nettoyer, dédupliquer et convertir les logs bruts (JSON) en format colonnaire optimisé (Parquet).</li>
            <li><strong>Warehousing :</strong> Chargement automatique dans <b>Redshift</b> via la commande <i>COPY</i> pour permettre des requêtes analytiques SQL performantes.</li>
        </ul>
        """,
        
        "impact": """
        ⚡ <b>Latence Réduite :</b> Passage d'un batch quotidien à un traitement en <b>quasi temps réel (15 min)</b>.<br>
        💰 <b>FinOps :</b> Réduction de 40% de la facture Cloud grâce au modèle "Pay-as-you-go" (Serverless) vs serveurs dédiés.<br>
        📈 <b>Scalabilité :</b> Le pipeline encaisse automatiquement les pics de charge sans intervention humaine.
        """,

        "challenges": [
            "Gestion des 'Cold Starts' des fonctions Lambda",
            "Optimisation du partitionnement S3 (Hive-style) pour réduire les coûts de scan",
            "Implémentation de Dead Letter Queues (DLQ) pour rejouer les événements échoués"
        ]
    },
    {
        "title": "Flux ETL Big Data (Azure & Databricks)",
        "type": "Big Data Engineering",
        "period": "Avr. 2025",
        "desc": "Implémentation d'une 'Medallion Architecture' (Bronze/Silver/Gold) pour un Data Lake d'entreprise.",
        
        "tech": [
            "Azure Data Factory (Orchestration)", 
            "Databricks (PySpark)", 
            "ADLS Gen2 (Storage)", 
            "Delta Lake (ACID)", 
            "Power BI"
        ],
        
        "details": """
        <strong>Problématique Data Quality :</strong> Les données sources (ERP, CRM) étaient cloisonnées et incohérentes, rendant impossible la création d'une "Single Source of Truth".
        <br><br>
        <strong>Architecture Medallion :</strong>
        <ul>
            <li><strong>Couche Bronze (Raw) :</strong> Ingestion brute des données historiques via <b>Azure Data Factory</b> dans le Data Lake (ADLS Gen2).</li>
            <li><strong>Couche Silver (Clean) :</strong> Nettoyage et standardisation via <b>Spark sur Databricks</b>. Utilisation du format <b>Delta Lake</b> pour garantir les transactions ACID et permettre le "Time Travel" (versioning).</li>
            <li><strong>Couche Gold (Aggregated) :</strong> Création de tables dimensionnelles (Star Schema) prêtes pour la consommation BI.</li>
        </ul>
        """,
        
        "impact": """
        ✅ <b>Qualité de Donnée :</b> Fiabilité des rapports passée de 60% à 99.9% grâce aux contraintes de schéma (Schema Enforcement) de Delta Lake.<br>
        🚀 <b>Performance :</b> Traitement des données 40% plus rapide grâce à l'optimisation du moteur Photon de Databricks.<br>
        🔄 <b>Auditabilité :</b> Capacité de revenir à n'importe quelle version antérieure de la donnée via les logs de transaction.
        """,

        "challenges": [
            "Gestion des 'Schema Drifts' (évolution de la structure des données sources)",
            "Optimisation des Shuffle Partitions dans Spark pour gérer les gros volumes (TB)",
            "Sécurisation des accès via Azure Key Vault et Service Principals"
        ]
    },
    {
        "title": "Speech Emotion Recognition (SER)",
        "type": "Deep Learning / Audio",
        "period": "GitHub",
        "desc": "Classification des émotions humaines à partir de signaux audio bruts via CNN.",
        
        "tech": [
            "Librosa (Feature Extraction)", 
            "TensorFlow / Keras", 
            "CNN (Convolutional Neural Network)", 
            "Matplotlib (Spectrograms)"
        ],
        "link": "https://github.com/dynmohamed/Speech-Emotion-Recognition---Sound-Classification",
        
        "details": """
        <strong>Complexité du Signal :</strong> L'audio brut est une donnée non structurée difficile à exploiter directement par des algorithmes classiques. L'enjeu est d'extraire des caractéristiques représentatives de l'état émotionnel (Colère, Joie, Tristesse).
        <br><br>
        <strong>Pipeline de Traitement :</strong>
        <ul>
            <li><strong>Feature Extraction :</strong> Transformation des fichiers audio (.wav) en représentations visuelles et spectrales : extraction des <b>MFCCs</b> (Mel-Frequency Cepstral Coefficients) et des <b>Mel-Spectrograms</b> qui capturent la texture du son.</li>
            <li><strong>Architecture Deep Learning :</strong> Conception d'un réseau de neurones convolutif (CNN) adapté aux données séquentielles, capable d'apprendre des motifs temporels et fréquentiels dans les spectrogrammes.</li>
        </ul>
        """,
        
        "impact": """
        🎧 <b>Analyse Acoustique :</b> Capacité à distinguer 7 émotions fondamentales indépendamment du contenu sémantique (ce qui est dit importe peu, c'est le "ton" qui compte).<br>
        📊 <b>Performance :</b> Accuracy de 80%+ sur le dataset de référence (RAVDESS/TESS).<br>
        🧩 <b>Applications :</b> Brique technologique utilisable pour l'analyse de satisfaction en centre d'appels.
        """,

        "challenges": [
            "Normalisation des durées audio (Padding/Truncating)",
            "Réduction du bruit de fond dans les enregistrements",
            "Augmentation des données audio (Time stretching, Pitch shifting) pour enrichir le dataset"
        ]
    },   
{
        "title": "Market Intelligence Bancaire",
        "type": "Web Scraping / Analytics",
        "period": "GitHub",
        "desc": "Pipeline d'extraction et d'analyse de sentiment sur les avis clients des banques marocaines.",
        
        "tech": [
            "Selenium & BeautifulSoup", 
            "NLP (Sentiment Analysis)", 
            "Plotly / Dash", 
            "Pandas"
        ],
        "link": "https://github.com/dynmohamed/Analyzing-Customer-Reviews-of-Bank-Agencies-in-Morocco-using-a-Modern-Data-Stack",
        
        "details": """
        <strong>Besoin Business :</strong> Les banques manquent de visibilité consolidée sur la satisfaction client exprimée publiquement (Google Maps, Trustpilot), perdant des opportunités d'amélioration.
        <br><br>
        <strong>Solution End-to-End :</strong>
        <ul>
            <li><strong>Scraping Robuste :</strong> Développement de bots <b>Selenium</b> capables de naviguer, scroller et extraire des milliers d'avis tout en gérant les délais et les erreurs de chargement.</li>
            <li><strong>Enrichissement NLP :</strong> Analyse de chaque commentaire pour extraire le sentiment global (Polarité) et les sujets récurrents (ex: "Attente", "Application mobile").</li>
            <li><strong>Visualisation :</strong> Restitution des insights via des dashboards interactifs pour le benchmarking concurrentiel.</li>
        </ul>
        """,
        
        "impact": """
        💡 <b>Insights Stratégiques :</b> Identification automatique des agences les moins performantes.<br>
        📊 <b>Benchmarking :</b> Comparaison quantitative de la satisfaction (NPS estimé) entre les acteurs du marché.<br>
        🔄 <b>Automatisation :</b> Remplacement d'une veille manuelle fastidieuse par un script exécutable à la demande.
        """,

        "challenges": [
            "Maintenance des sélecteurs CSS face aux mises à jour des sites web",
            "Nettoyage des données textuelles très bruitées (mélange Français / Darija / Arabe)",
            "Détection et filtrage des faux avis (Spam)"
        ]
    },
    {
        "title": "Hate Speech Detection (NLP)",
        "type": "NLP / Trust & Safety",
        "period": "GitHub",
        "desc": "Système de modération automatique basé sur les Transformers (BERT) pour identifier les contenus toxiques.",
        
        "tech": [
            "Hugging Face Transformers", 
            "BERT (Fine-tuning)", 
            "PyTorch", 
            "Scikit-Learn (Evaluation)",
            "Pandas"
        ],
        "link": "https://github.com/dynmohamed/Hate-Speach-Detection",
        
        "details": """
        <strong>Enjeu Sociétal :</strong> Les méthodes basées sur des mots-clés (Regex) sont inefficaces face au sarcasme, aux fautes d'orthographe ou au contexte implicite des discours haineux.
        <br><br>
        <strong>Approche State-of-the-Art :</strong>
        <ul>
            <li><strong>Preprocessing NLP :</strong> Nettoyage avancé (Tokenization, Lemmatization, suppression URLs) pour réduire le bruit textuel.</li>
            <li><strong>Transfer Learning :</strong> Utilisation d'un modèle <b>BERT</b> (Bidirectional Encoder Representations from Transformers) pré-entraîné. Contrairement aux modèles simples (LSTM), BERT comprend le contexte bidirectionnel de la phrase.</li>
            <li><strong>Fine-Tuning :</strong> Ré-entraînement des dernières couches du modèle sur un corpus classifié pour spécialiser la détection.</li>
        </ul>
        """,
        
        "impact": """
        🛡️ <b>Sécurité :</b> Automatisation de la modération avec un Recall élevé (minimisation des contenus haineux non détectés).<br>
        🧠 <b>Contextualisation :</b> Distinction efficace entre une discussion offensive et l'usage de termes argotiques non haineux.<br>
        """,

        "challenges": [
            "Gestion du déséquilibre des classes (peu de contenu haineux vs contenu normal)",
            "Optimisation du temps d'entraînement sur GPU (Gradient Accumulation)",
            "Traitement du langage informel et des abréviations SMS"
        ]
    }
]
# --- AJOUTER À LA FIN DE content.py ---

DEMOS = [
    {
        "key": "yolo",
        "title": "👁️ Vision",
        "desc": "Détection d'objets (YOLOv8).",
        "btn_label": "Lancer 🚀"
    },
    {
        "key": "nlp",
        "title": "🧠 NLP",
        "desc": "Analyse de Sentiment.",
        "btn_label": "Lancer 📝"
    },
    {
        "key": "chatbot",
        "title": "🩺 Santé",
        "desc": "Assistant Médical (RAG).",
        "btn_label": "Lancer 🤖"
    },
    {
        "key": "fraude",
        "title": "💳 FinTech",
        "desc": "Détection de Fraude (ML).",
        "btn_label": "Lancer 🔍"
    }
]

# ==============================================================================
# 2. AJOUT DU CONTENU ANGLAIS (NOUVEAU)
# ==============================================================================

INFO_EN = {
    "name": "Mohamed Dyn",
    "role": "Data Science & Data Engineering Engineer",
    "location": "Rabat, Morocco",
    "summary": """
    Final-year engineering student at INSEA, I bridge the gap between Data Engineering, Generative AI, and Analytics.
    I am looking for an End-of-Studies Internship (PFE) to transform complex data into strategic solutions.
    """
}

EXPERIENCES_EN = [
    {
        "role": "Data Scientist (Intern)",
        "company": "TEMACONCEPT",
        "period": "Jul 2023 - Sep 2023",
        "github": "https://github.com/dynmohamed/Affectation-des-professeurs-CPGE-AI-chatbot",
        "report": "assets/rapport_de_stage_PFA_dyn_mohamed.pdf",
        "desc": "Development of an optimization engine for CPGE teacher assignments and design of a RAG system.",
        
        # HTML DESCRIPTION: Narrative, Technical, and Fluid
        "description": """
        <div style="text-align: justify;">
            This strategic project aimed to completely overhaul the CPGE teacher assignment process, previously managed manually in the face of <b>exponential combinatorial complexity</b>. 
            <br><br>
            My intervention first focused on the mathematical modeling of the problem (Linear Assignment Problem). I implemented the <b>Hungarian algorithm (Kuhn-Munkres)</b> to simultaneously handle strict multidimensional constraints (geography, specialty, pedagogical rank) and guarantee mathematical optimality impossible to achieve manually.
            <br><br>
            To ensure tool adoption by stakeholders and avoid the "black box" effect, I designed a <b>Generative AI (RAG)</b> module connected to the results. This system allows HR managers to query assignments in natural language (e.g., <i>"Why didn't this candidate get their #1 choice?"</i>), thus providing crucial transparency for strategic decision-making.
        </div>
        """,
        
        # KEY FIGURES REMAIN BELOW FOR VISUAL IMPACT
        "results": [
            "⚡ <b>Massive time saving:</b> Reduced processing time from 5 days to just 2 hours (-95%).",
            "🎯 <b>Optimization:</b> Mathematical maximization of preference satisfaction (100% coverage).",
            "🤖 <b>Innovation:</b> Successful hybridization between Operations Research (Optimization) and GenAI (Explainability)."
        ],
        
        "tags": ["Python", "Operations Research", "Hungarian Algorithm", "RAG", "LangChain"]
    },
    {
        "role": "Data Analyst (Intern)",
        "company": "Ministry of Parliamentary Relations",
        "period": "Jul 2024 - Aug 2024",
        # No GitHub for this one, just the report
        "report": "assets/Rapport_du_stage_de_decouverte_DynMohamed.pdf",
        "desc": "Design of dashboards for monitoring parliamentary activities.",
        
        # DESCRIPTION: Focus on BI, Strategy, and Rigor
        "description": """
        <div style="text-align: justify;">
            At the heart of the administration's digital transformation, my mission was to modernize the management of parliamentary activities (Written/oral questions, bill proposals).
            <br><br>
            I led the design of a complete <b>Business Intelligence (BI) architecture</b>. Starting from raw and scattered data, I performed in-depth <b>Data Cleaning</b> and modeling (Star Schema) to ensure indicator integrity.
            <br><br>
            The result was the deployment of interactive <b>Power BI</b> dashboards. By using advanced <b>DAX measures</b>, I provided decision-makers with a real-time view of response times and legislative themes, transforming administrative management into true <b>data-driven strategic steering</b>.
        </div>
        """,
        
        # RESULTS: Impact on decision and quality
        "results": [
            "📊 <b>Governance:</b> Creation of a reliable 'Single Source of Truth' for Ministry statistics.",
            "⚡ <b>Decision Support:</b> Immediate identification of bottlenecks (response delays) thanks to dynamic visuals.",
            "🛠️ <b>Technical:</b> Optimized data modeling for instant filtering performance."
        ],
        
        "tags": ["Power BI", "DAX", "Data Modeling", "SQL", "Data Governance"]
    },
]
# Merging CV (Business) and GitHub (Tech) projects
PROJECTS_EN = [
    # --- CV PROJECTS (Business Priority) ---
    {
        "title": "Clinical Decision Support System (GenAI)",
        "type": "GenAI / MLOps",
        "period": "Advanced Personal Project",
        # 1. The Hook: Define the technical problem immediately
        "desc": "Secure medical inference engine (RAG) with expert alignment loop (RLHF/DPO).",
        
        # 2. Production Stack (Shows deployment skills, not just coding)
        "tech": [
            "Llama-3 (Quantized 4-bit)", # Optimized model
            "LangChain & ChromaDB",      # Orchestration & Vector Store
            "FastAPI (Async)",           # High-performance Backend
            "Python (Async IO)",         # For concurrency
            "RLHF (DPO)"                 # Advanced Alignment
        ],
        
        "link": "https://github.com/dynmohamed/Medical-chatbot-generative-AI",
        "demo_key": "chatbot",

        # 3. The Technical Story (Architecture & Data Flow)
        "details": """
        <strong>Situation:</strong> The use of standard LLMs in medical settings is critical due to "hallucinations" (error rate ~15-20%) and patient data privacy risks.
        <br><br>
        <strong>Architecture & Solution:</strong>
        Design of a <strong>RAG (Retrieval-Augmented Generation)</strong> "Privacy-First" system deployable On-Premise.
        <ul>
            <li><strong>Ingestion Pipeline:</strong> Custom ETL processing heterogeneous documents (PDF, HTML Protocols) with a <i>Recursive Character Splitter</i> to preserve semantic context.</li>
            <li><strong>Hybrid Search Engine:</strong> Combination of vector search (Dense Retrieval) and keyword search (BM25) via <strong>ChromaDB</strong> to maximize medical information Recall.</li>
            <li><strong>Alignment Loop (RLHF):</strong> Implementation of a user feedback module collecting preferences (A/B Testing) to refine the model via <strong>DPO (Direct Preference Optimization)</strong>.</li>
        </ul>
        """,
        
        # 4. Impact & KPIs (Recruiter Language)
        "impact": """
        🛡️ <b>Critical Reliability:</b> Elimination of hallucinations via <i>Strict Fact-Grounding</i> (every answer cites its source).<br>
        ⚡ <b>Performance:</b> Inference latency reduced from 5s to <b>1.2s</b> thanks to Llama-3 4-bit quantization.<br>
        ⚡ <b>Accessibility:</b> Transformation of a complex model into a simple web interface usable by non-technical staff.
        """,

        # 5. Challenges (Proof of problem-solving skills)
        "challenges": [
            "Reducing RAG latency (Top-K retrieval optimization)",
            "Handling 'Lost in the Middle' phenomenon (Document Reranking)",
            "Aligning medical tone (Advanced Prompt Engineering & Few-Shot)"
        ]
    },
    {
        "title": "Real-time Financial Fraud Detection",
        "type": "FinTech / Cybersec",
        "period": "GitHub Project",
        "desc": "Hybrid anomaly detection system (Supervised/Unsupervised) to secure financial flows in real-time.",
        
        "tech": [
            "Scikit-Learn (Isolation Forest)",
            "XGBoost (Gradient Boosting)",
            "SHAP (Explainability)",
            "Pandas (Time-series features)"
        ],
        
        "link": "https://github.com/dynmohamed/detection-de-fraude-en-temps-reel",
        "demo_key": "fraude",

        "details": """
        <strong>Business Problem:</strong> Fraud detection is an "extreme imbalance" problem (Imbalanced Classification): less than 0.1% of transactions are fraudulent. Classic models bias towards the majority class and miss frauds.
        <br><br>
        <strong>Advanced Data Science Approach:</strong>
        <ul>
        <li><strong>1. Temporal Feature Engineering:</strong> Raw data (Amount, Time) is insufficient. I created complex temporal aggregates (Rolling Windows): 
            <i>"Average spend over last 24h"</i>, <i>"Standard deviation vs client history"</i>, <i>"Geographic velocity between two payments"</i>.</li>
            
        <li><strong>2. Hybrid Modeling Strategy:</strong>
                <br>- <b>Isolation Forest (Unsupervised):</b> To detect unknown "Outliers" (new fraud patterns).
                <br>- <b>XGBoost (Supervised):</b> Trained on historical fraud to classify known attacks with high precision.</li>
            
        <li><strong>3. Handling Imbalance:</strong> Application of <strong>SMOTE</strong> (Synthetic Minority Over-sampling Technique) during training to generate synthetic frauds and force the model to learn minority class characteristics.</li>
        </ul>
        """,
        
        "impact": """
        ⚖️ <b>Business Performance:</b> Maximization of <b>F1-Score</b> rather than Accuracy, reducing False Negatives (missed fraud) without blocking legitimate clients (False Positives).<br>
        🔍 <b>Explainable AI (XAI):</b> Integration of <b>SHAP</b> library to generate local explanations for each alert (e.g., "Transaction blocked because amount is 5x higher than usual average").<br>
        ⏱️ <b>Real-Time Inference:</b> Optimized pipeline capable of processing a transaction and returning a risk score in milliseconds.
        """,

        "challenges": [
            "Combating 'Concept Drift' (fraud patterns evolve over time)",
            "Risk of Overfitting on synthetic data generated by SMOTE",
            "Cleaning noisy data (missing values, inconsistent formats)"
        ]
    },
    {
        "title": "Object Detection (YOLOv8)",
        "type": "Computer Vision",
        "period": "GitHub / Research",
        "desc": "Real-time computer vision system for specific object detection (Custom Dataset).",
        
        "tech": [
            "YOLOv8 (Ultralytics)", 
            "OpenCV (Image Processing)", 
            "PyTorch", 
            "Albumentations (Augmentation)", 
            "CUDA (GPU Acceleration)"
        ],
        "link": "https://github.com/dynmohamed/Custom-Object-Detection-using-YOLOv8",
        "demo_key": "yolo",
        
        "details": """
        <strong>Technical Challenge:</strong> Pre-trained models (COCO dataset) fail to detect specific or rare objects in complex industrial environments (variable lighting, occlusions).
        <br><br>
        <strong>MLOps Strategy:</strong>
        <ul>
            <li><strong>Data Curation:</strong> Creation and manual annotation of a proprietary dataset via <b>Roboflow</b>.</li>
            <li><strong>Advanced Data Augmentation:</strong> Application of robust transformations (Mosaic, Gaussian Blur, Cutout) with the <b>Albumentations</b> library to force generalization and avoid overfitting.</li>
            <li><strong>Transfer Learning:</strong> Fine-tuning of the YOLOv8 nano architecture to reach an optimal compromise between speed (FPS) and precision (mAP).</li>
        </ul>
        """,
        
        "impact": """
        👁️ <b>Precision:</b> Achieved a <b>mAP@50 of 0.92</b> on the test set, outperforming generic models.<br>
        ⏱️ <b>Real-Time:</b> Stable inference at <b>30+ FPS</b> on standard GPU, allowing deployment on live video streams.<br>
        📦 <b>Deployment:</b> Model export to ONNX format for maximum interoperability.
        """,

        "challenges": [
            "Handling false positives due to complex backgrounds",
            "Class balancing (some objects were under-represented)",
            "Hyperparameter optimization (Learning Rate, Batch Size) for convergence"
        ]
    },
    {
        "title": "Sentiment Analysis",
        "type": "NLP / MLOps",
        "period": "Academic Project",
        "desc": "Ultra-fast text classification API (<50ms) for real-time tone analysis.",
        
        "tech": [
            "NLTK (Preprocessing)", 
            "Scikit-Learn (TF-IDF & SVM)", 
            "Flask (API Serving)", 
            "Pickle (Serialization)",
            "Python"
        ],
        "link": "https://github.com/dynmohamed/sentiment-prediction",
        "demo_key": "nlp",
        
        "details": """
        <strong>Engineering Context:</strong> Deep Learning models (like BERT) are sometimes "overkill" for simple tasks requiring minimal latency (e.g., live chat moderation).
        <br><br>
        <strong>"Lightweight" Approach:</strong>
        <ul>
            <li><strong>Classic NLP Pipeline:</strong> Implementation of a robust processing chain: Cleaning (Regex) ➔ Stopwords removal ➔ Stemming (Snowball) ➔ Vectorization (TF-IDF).</li>
            <li><strong>Statistical Modeling:</strong> Choice of <b>SVM (Support Vector Machine)</b> or <b>Naive Bayes</b> algorithm for their formidable efficiency on sparse text data, offering an ideal speed/precision trade-off.</li>
            <li><strong>Model Serving:</strong> Encapsulation of the model in a <b>REST API (Flask)</b>. The model is serialized (Pickle) at startup to guarantee instant responses to HTTP requests.</li>
        </ul>
        """,
        
        "impact": """
        🚀 <b>Ultra-Low Latency:</b> Inference time under <b>20ms</b>, allowing synchronous integration into web applications.<br>
        🔧 <b>Integrability:</b> Decoupled micro-service architecture, easy to consume by any front-end.<br>
        📉 <b>Efficiency:</b> Minimal memory consumption (<200MB RAM) compared to Transformer models (>2GB).
        """,

        "challenges": [
            "Handling negations (e.g., 'Not bad' should be positive)",
            "Dimensionality reduction of vocabulary (Feature Selection)",
            "Cleaning special characters and Emojis"
        ]
    },

    {
        "title": "Serverless ELT Architecture (AWS)",
        "type": "Data Engineering / Cloud",
        "period": "Mar. 2025",
        "desc": "Fully automated 'Event-Driven' pipeline on AWS (Zero-Infrastructure).",
        
        "tech": [
            "AWS Glue (Spark Jobs)", 
            "AWS Lambda (Triggers)", 
            "Amazon S3 (Data Lake)", 
            "Redshift (Data Warehousing)", 
            "IAC (Terraform)"
        ],
        
        "details": """
        <strong>Infrastructure Challenge:</strong> The company processed logs via manual scripts, causing 24h latency and high maintenance costs (EC2 servers inactive 80% of the time).
        <br><br>
        <strong>Serverless Solution:</strong> Design of a reactive architecture:
        <ul>
            <li><strong>Event-Driven Ingestion:</strong> Using <b>S3 Event Notifications</b> to trigger an <b>AWS Lambda</b> function as soon as a file arrives, eliminating the need for an external orchestrator for simple tasks.</li>
            <li><strong>Scalable Transformation:</strong> <b>AWS Glue</b> (PySpark) jobs to clean, deduplicate, and convert raw logs (JSON) into optimized columnar format (Parquet).</li>
            <li><strong>Warehousing:</strong> Automatic loading into <b>Redshift</b> via the <i>COPY</i> command to enable high-performance SQL analytical queries.</li>
        </ul>
        """,
        
        "impact": """
        ⚡ <b>Reduced Latency:</b> Shift from daily batch to <b>near real-time (15 min)</b> processing.<br>
        💰 <b>FinOps:</b> 40% reduction in Cloud bill thanks to "Pay-as-you-go" (Serverless) model vs dedicated servers.<br>
        📈 <b>Scalability:</b> The pipeline automatically handles load spikes without human intervention.
        """,

        "challenges": [
            "Managing 'Cold Starts' of Lambda functions",
            "Optimizing S3 partitioning (Hive-style) to reduce scan costs",
            "Implementing Dead Letter Queues (DLQ) to replay failed events"
        ]
    },
    {
        "title": "Big Data ETL Pipeline (Azure & Databricks)",
        "type": "Big Data Engineering",
        "period": "Apr. 2025",
        "desc": "Implementation of a 'Medallion Architecture' (Bronze/Silver/Gold) for an Enterprise Data Lake.",
        
        "tech": [
            "Azure Data Factory (Orchestration)", 
            "Databricks (PySpark)", 
            "ADLS Gen2 (Storage)", 
            "Delta Lake (ACID)", 
            "Power BI"
        ],
        
        "details": """
        <strong>Data Quality Problem:</strong> Source data (ERP, CRM) was siloed and inconsistent, making it impossible to create a "Single Source of Truth".
        <br><br>
        <strong>Medallion Architecture:</strong>
        <ul>
            <li><strong>Bronze Layer (Raw):</strong> Raw ingestion of historical data via <b>Azure Data Factory</b> into the Data Lake (ADLS Gen2).</li>
            <li><strong>Silver Layer (Clean):</strong> Cleaning and standardization via <b>Spark on Databricks</b>. Usage of <b>Delta Lake</b> format to guarantee ACID transactions and enable "Time Travel" (versioning).</li>
            <li><strong>Gold Layer (Aggregated):</strong> Creation of dimensional tables (Star Schema) ready for BI consumption.</li>
        </ul>
        """,
        
        "impact": """
        ✅ <b>Data Quality:</b> Report reliability increased from 60% to 99.9% thanks to Delta Lake Schema Enforcement constraints.<br>
        🚀 <b>Performance:</b> Data processing 40% faster thanks to Databricks Photon engine optimization.<br>
        🔄 <b>Auditability:</b> Ability to revert to any previous data version via transaction logs.
        """,

        "challenges": [
            "Managing 'Schema Drifts' (evolution of source data structure)",
            "Optimizing Spark Shuffle Partitions to handle large volumes (TB)",
            "Securing access via Azure Key Vault and Service Principals"
        ]
    },
    {
        "title": "Speech Emotion Recognition (SER)",
        "type": "Deep Learning / Audio",
        "period": "GitHub",
        "desc": "Classification of human emotions from raw audio signals via CNN.",
        
        "tech": [
            "Librosa (Feature Extraction)", 
            "TensorFlow / Keras", 
            "CNN (Convolutional Neural Network)", 
            "Matplotlib (Spectrograms)"
        ],
        "link": "https://github.com/dynmohamed/Speech-Emotion-Recognition---Sound-Classification",
        
        "details": """
        <strong>Signal Complexity:</strong> Raw audio is unstructured data difficult to exploit directly by classic algorithms. The challenge is to extract features representative of the emotional state (Anger, Joy, Sadness).
        <br><br>
        <strong>Processing Pipeline:</strong>
        <ul>
            <li><strong>Feature Extraction:</strong> Transforming audio files (.wav) into visual and spectral representations: extraction of <b>MFCCs</b> (Mel-Frequency Cepstral Coefficients) and <b>Mel-Spectrograms</b> which capture sound texture.</li>
            <li><strong>Deep Learning Architecture:</strong> Design of a Convolutional Neural Network (CNN) adapted to sequential data, capable of learning temporal and frequency patterns in spectrograms.</li>
        </ul>
        """,
        
        "impact": """
        🎧 <b>Acoustic Analysis:</b> Ability to distinguish 7 fundamental emotions independently of semantic content (what is said matters little, it's the "tone" that counts).<br>
        📊 <b>Performance:</b> 80%+ Accuracy on the reference dataset (RAVDESS/TESS).<br>
        🧩 <b>Applications:</b> Tech brick usable for satisfaction analysis in call centers.
        """,

        "challenges": [
            "Normalizing audio durations (Padding/Truncating)",
            "Reducing background noise in recordings",
            "Audio Data Augmentation (Time stretching, Pitch shifting) to enrich dataset"
        ]
    },   
    {
        "title": "Banking Market Intelligence",
        "type": "Web Scraping / Analytics",
        "period": "GitHub",
        "desc": "Pipeline for extraction and sentiment analysis of Moroccan bank customer reviews.",
        
        "tech": [
            "Selenium & BeautifulSoup", 
            "NLP (Sentiment Analysis)", 
            "Plotly / Dash", 
            "Pandas"
        ],
        "link": "https://github.com/dynmohamed/Analyzing-Customer-Reviews-of-Bank-Agencies-in-Morocco-using-a-Modern-Data-Stack",
        
        "details": """
        <strong>Business Need:</strong> Banks lack consolidated visibility on publicly expressed customer satisfaction (Google Maps, Trustpilot), missing improvement opportunities.
        <br><br>
        <strong>End-to-End Solution:</strong>
        <ul>
            <li><strong>Robust Scraping:</strong> Development of <b>Selenium</b> bots capable of navigating, scrolling, and extracting thousands of reviews while handling timeouts and loading errors.</li>
            <li><strong>NLP Enrichment:</strong> Analysis of each comment to extract global sentiment (Polarity) and recurring topics (e.g., "Waiting time", "Mobile App").</li>
            <li><strong>Visualization:</strong> Insight delivery via interactive dashboards for competitive benchmarking.</li>
        </ul>
        """,
        
        "impact": """
        💡 <b>Strategic Insights:</b> Automatic identification of underperforming branches.<br>
        📊 <b>Benchmarking:</b> Quantitative comparison of satisfaction (estimated NPS) between market players.<br>
        🔄 <b>Automation:</b> Replacement of tedious manual monitoring with an on-demand executable script.
        """,

        "challenges": [
            "Maintaining CSS selectors against website updates",
            "Cleaning highly noisy text data (mix of French / Darija / Arabic)",
            "Detection and filtering of fake reviews (Spam)"
        ]
    },
    {
        "title": "Hate Speech Detection (NLP)",
        "type": "NLP / Trust & Safety",
        "period": "GitHub",
        "desc": "Automated moderation system based on Transformers (BERT) to identify toxic content.",
        
        "tech": [
            "Hugging Face Transformers", 
            "BERT (Fine-tuning)", 
            "PyTorch", 
            "Scikit-Learn (Evaluation)",
            "Pandas"
        ],
        "link": "https://github.com/dynmohamed/Hate-Speach-Detection",
        
        "details": """
        <strong>Societal Issue:</strong> Keyword-based methods (Regex) are ineffective against sarcasm, spelling mistakes, or implicit context of hate speech.
        <br><br>
        <strong>State-of-the-Art Approach:</strong>
        <ul>
            <li><strong>NLP Preprocessing:</strong> Advanced cleaning (Tokenization, Lemmatization, URL removal) to reduce text noise.</li>
            <li><strong>Transfer Learning:</strong> Use of a pre-trained <b>BERT</b> (Bidirectional Encoder Representations from Transformers) model. Unlike simple models (LSTM), BERT understands the bidirectional context of the sentence.</li>
            <li><strong>Fine-Tuning:</strong> Retraining the model's final layers on a classified corpus to specialize detection.</li>
        </ul>
        """,
        
        "impact": """
        🛡️ <b>Safety:</b> Automated moderation with high Recall (minimizing undetected hate content).<br>
        🧠 <b>Contextualization:</b> Effective distinction between offensive discussion and the use of non-hateful slang terms.<br>
        """,

        "challenges": [
            "Handling class imbalance (few hate content vs. normal content)",
            "Optimizing training time on GPU (Gradient Accumulation)",
            "Processing informal language and SMS abbreviations"
        ]
    }
]