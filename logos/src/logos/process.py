
import os
import time
from pathlib import Path
import argparse

def get_size(file: str) -> int:

    if not os.path.exists(file):
        raise FileNotFoundError(f"{file} n existe pas")

    donnees = os.stat(file)
    return donnees.st_size


def get_creation_date(file: str) -> str:

    if not os.path.exists(file):
        raise FileNotFoundError(f"{file} n existe pas")

    donnees = os.stat(file)
    temps = donnees.st_ctime
    date = time.gmtime(temps)

    return time.strftime("%d-%m-%Y %H:%M", date)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Afficher les proprietes d’un fichier")
    parser.add_argument("file", type=Path, help="Chemin du fichier à analyser")
    args = parser.parse_args()
    file = args.file
    if not file.exists():
        parser.error(f"Le fichier {file} n existe pas")
    size = get_size(file)
    date = get_creation_date(file)
    print(f"Fichier {file} : taille {size}, date de creation {date}")

