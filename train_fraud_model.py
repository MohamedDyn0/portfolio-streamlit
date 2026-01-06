# train_fraud_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

print("🧠 Entraînement du modèle de fraude en cours...")

# 1. Génération de données synthétiques (10 000 transactions)
n_samples = 10000
np.random.seed(42)

data = {
    'montant': np.random.exponential(scale=500, size=n_samples), # Beaucoup de petites sommes, peu de grosses
    'heure': np.random.randint(0, 24, size=n_samples),
    'type_paiement': np.random.choice([0, 1, 2], size=n_samples), # 0:CB, 1:Virement, 2:Crypto
    'pays': np.random.choice([0, 1, 2, 3, 4, 5], size=n_samples), # Mappé manuellement
    'categorie': np.random.choice([0, 1, 2, 3, 4, 5], size=n_samples)
}

df = pd.DataFrame(data)

# 2. Création de la logique de fraude (Le "Pattern" que l'IA doit découvrir)
def generate_fraud(row):
    score = 0
    # Montant élevé
    if row['montant'] > 5000: score += 4
    # Heures tardives (Minuit - 4h)
    if 0 <= row['heure'] <= 4: score += 3
    # Crypto (2) est plus risqué
    if row['type_paiement'] == 2: score += 3
    # Pays risqués (Russie=4, Nigeria=5)
    if row['pays'] in [4, 5]: score += 5
    # Catégorie (Jeux=4, Luxe=3)
    if row['categorie'] in [3, 4]: score += 2
    
    # Probabilité aléatoire basée sur le score
    probability = 1 / (1 + np.exp(-(score - 6))) # Sigmoid
    return 1 if np.random.random() < probability else 0

df['is_fraud'] = df.apply(generate_fraud, axis=1)

# 3. Entraînement du modèle
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X, y)

# 4. Sauvegarde
joblib.dump(model, 'fraud_model.pkl')
print("✅ Modèle sauvegardé sous 'fraud_model.pkl'")