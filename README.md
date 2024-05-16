Bien sûr, voici un exemple de README pour votre programme basé sur les informations que vous avez fournies :

---

# Eye Controlled Mouse

## Auteur
Enzo Sebiane ( thanks to Programming Hero )

## Description
Ce programme utilise OpenCV, MediaPipe et PyAutoGUI pour permettre le contrôle de la souris à l'aide des mouvements des yeux détectés par la caméra. L'idée est inspirée du tutoriel de la chaîne YouTube Programming Hero.

## Fonctionnalités
- Détection des points du visage et des yeux à l'aide de MediaPipe.
- Contrôle de la souris en fonction des mouvements des yeux détectés.
- Détection du clignement des yeux pour effectuer des actions telles que le clic de souris.

## Prérequis
- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

## Installation
1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Installez les bibliothèques requises :
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

## Utilisation
1. Lancez le programme en exécutant le fichier `eye_controlled_mouse.py`.
2. Assurez-vous que la caméra est fonctionnelle et positionnée de manière à capturer votre visage.
3. Contrôlez la souris en bougeant vos yeux. Clignez des yeux pour simuler un clic de souris.

## Avertissement
- Ce programme désactive la fonction de sécurité de PyAutoGUI (`FAILSAFE`) pour permettre un contrôle plus sensible de la souris. Utilisez-le avec prudence et vérifiez que le script est contrôlé dans un environnement sûr.
- Assurez-vous de comprendre les implications de l'utilisation de ce script, notamment en termes de sécurité et de responsabilité.

## Contribuer
Les contributions sont les bienvenues ! Si vous avez des suggestions d'amélioration, des correctifs de bogues ou des fonctionnalités à ajouter, n'hésitez pas à ouvrir une demande de tirage (pull request) ou à soumettre une issue.

---

Ce README fournit des informations sur l'auteur, la description du programme, ses fonctionnalités, les prérequis, l'installation, l'utilisation, les avertissements et la contribution. Vous pouvez l'adapter selon vos besoins et ajouter d'autres détails si nécessaire.
