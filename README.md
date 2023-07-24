# Script de copie et de déplacement de médias

Ce script Python permet de copier et de déplacer des médias (photos et vidéos) à partir d'un répertoire source vers un répertoire de destination. Il prend également en charge la gestion des doublons et la création des répertoires nécessaires selon la date de modification des fichiers.

## Prérequis

Pour exécuter ce script, vous devez disposer de Python installé sur votre machine. Vous pouvez le télécharger depuis le site officiel de Python : [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Utilisation

Avant d'exécuter le script, vous devez spécifier le répertoire source et le répertoire de destination dans les variables `source` et `destination`, respectivement. Assurez-vous que ces répertoires existent ou seront créés lors de la première exécution du script.

```python
source = "Source_photo"
destination = "Destination_photo"

copier_coller_media(source, destination)
```

Une fois que vous avez configuré les répertoires, exécutez le script Python. Il parcourra le répertoire source et copiera les fichiers dans le répertoire de destination en les organisant selon la date de modification.

## Fonctionnalités

Le script effectue les opérations suivantes :

1. Vérifie si les répertoires : source, destination et doublons existe, sinon les crées.
2. Parcourt tous les fichiers et dossiers dans le répertoire source.
3. Obtient la date de modification de chaque fichier.
4. Définit les répertoires de destination en utilisant le format français pour l'année et le mois.
5. Vérifie si le fichier est une photo ou une vidéo.
6. Vérifie si le répertoire de destination pour l'année existe, sinon le crée.
7. Vérifie si le répertoire de destination pour le mois existe, sinon le crée.
8. Déplace le fichier dans le répertoire de destination en utilisant le chemin de destination approprié.
9. Gère les doublons en déplaçant les fichiers existants dans le répertoire des doublons.
10. Supprime les dossiers vides du répertoire source.

## Formats de médias pris en charge

Ce script prend en charge les formats de médias suivants : .png, .jpg, .jpeg, .gif, .bmp, .mp4, .avi, .mov.

**Remarque :** Vous pouvez modifier ces formats dans la condition `filename.lower().endswith()` selon vos besoins.

## Remarques

- Ce script utilise la bibliothèque standard `os` pour les opérations sur le système de fichiers.
- La bibliothèque `shutil` est utilisée pour déplacer les fichiers.
- La bibliothèque `datetime` est utilisée pour obtenir la date de modification des fichiers.
- Les noms des mois sont convertis en français à l'aide d'un dictionnaire.

Assurez-vous d'avoir les autorisations appropriées pour créer et déplacer des fichiers sur votre système de fichiers avant d'exécuter ce script.

N'hésitez pas à personnaliser le script selon vos besoins spécifiques et à l'adapter à votre structure de dossiers.