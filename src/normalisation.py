import re
from nltk.corpus import stopwords
import os
from PyPDF2 import PdfReader
from docx import Document
from bs4 import BeautifulSoup


stop_words = set(stopwords.words('french'))

def normalize(text):
    """
    Transforme le texte en tokens propres :
    - minuscules
    - suppression ponctuation et chiffres
    - suppression des stopwords
    """
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + " "
        return text
    elif ext == ".docx":
        doc = Document(file_path)
        return " ".join([p.text for p in doc.paragraphs])
    elif ext == ".html":
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            return soup.get_text()
    else:
        return ""

def normalize_corpus(file_paths):
    
    corpus = {}
    for file_path in file_paths:
        text = read_file(file_path)
        tokens = normalize(text)
        corpus[os.path.basename(file_path)] = tokens
    return corpus

# Test rapide
if __name__ == "__main__":
    exemple = "Bonjour! Ceci est un exemple de texte avec des chiffres 123 et des mots inutiles."
    print(normalize(exemple))