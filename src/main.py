from acquisition import collect_files
from normalisation import normalize_corpus

folder = "data"
fichiers = collect_files(folder)
corpus = normalize_corpus(fichiers)

for doc, tokens in corpus.items():
    print(f"{doc} : {tokens[:20]}...")  # affiche les 20 premiers tokens
