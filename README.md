# Mini moteur documentaire (Flask)

Prototype pédagogique pour :
- Upload d'un dossier (ZIP)
- Parcours récursif
- Conversion en texte brut
- Normalisation + Extraction + Indexation
- Recherche booléenne (AND/OR)
- Visualisation (nuage de mots)

## Lancer en local

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py