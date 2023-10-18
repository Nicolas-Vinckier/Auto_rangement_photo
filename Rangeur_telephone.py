import os
import shutil
import re


def copier_coller_media(source, destination):
    destination_doublon = os.path.join(destination, "doublon")
    if not os.path.exists(destination_doublon):
        os.makedirs(destination_doublon)
        print("Répertoire des doublons créé :", destination_doublon)

    mois_fr = {
        "01": "Janvier",
        "02": "Février",
        "03": "Mars",
        "04": "Avril",
        "05": "Mai",
        "06": "Juin",
        "07": "Juillet",
        "08": "Août",
        "09": "Septembre",
        "10": "Octobre",
        "11": "Novembre",
        "12": "Décembre",
    }

    for root, dirs, files in os.walk(source):
        for filename in files:
            filepath = os.path.join(root, filename)

            # Utiliser une expression régulière pour extraire les informations de la date à partir du nom de fichier
            match = re.match(
                r"(IMG|VID|AMBI|PANO)_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})",
                filename,
            )

            if match:
                file_type, annee, mois, jour, heure, minutes, secondes = match.groups()

                # Utiliser le nom du mois en français
                mois = mois_fr.get(mois, mois)

                # Créer les répertoires de destination en utilisant les informations extraites
                destination_annee = os.path.join(destination, str(annee))
                destination_mois = os.path.join(destination_annee, mois)

                if not os.path.exists(destination_annee):
                    os.makedirs(destination_annee)
                    print(
                        "Répertoire de destination pour l'année créé :",
                        destination_annee,
                    )

                if not os.path.exists(destination_mois):
                    os.makedirs(destination_mois)
                    print(
                        "Répertoire de destination pour le mois créé :",
                        destination_mois,
                    )

                destination_filepath = os.path.join(destination_mois, filename)

                if os.path.exists(destination_filepath):
                    destination_doublon_mois = os.path.join(destination_doublon, mois)
                    if not os.path.exists(destination_doublon_mois):
                        os.makedirs(destination_doublon_mois)
                        print(
                            "Répertoire de destination pour les doublons du mois créé :",
                            destination_doublon_mois,
                        )
                    shutil.move(
                        filepath, os.path.join(destination_doublon_mois, filename)
                    )
                    print(
                        "Fichier déplacé vers le répertoire des doublons du mois :",
                        os.path.join(destination_doublon_mois, filename),
                    )
                else:
                    shutil.move(filepath, destination_filepath)
                    print("Fichier déplacé :", destination_filepath)

    for root, dirs, files in os.walk(source, topdown=False):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print("Dossier vide supprimé :", dir_path)


source = "photo_telephone"
destination = "phto_rangee"

# Créer les répertoires de source et de destination si ils n'existent pas
if not os.path.exists(source):
    os.makedirs(source)
if not os.path.exists(destination):
    os.makedirs(destination)

copier_coller_media(source, destination)
