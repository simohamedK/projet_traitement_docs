import os

def collect_files(folder_path, extensions=[".txt",".pdf",".docx",".html"]):
    all_files= []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                all_files.append(os.path.join(root, file))
    return all_files

if __name__ == "__main__" :
    folder = "data" # chemin relatif au dossier data
    fichiers = collect_files(folder)
    print(f"Fichiers trouvés : {fichiers}")
