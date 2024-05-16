import cv2  # Importation de la bibliothèque OpenCV pour le traitement d'images
import mediapipe as mp  # Importation de la bibliothèque MediaPipe pour la détection des points du visage
import pyautogui  # Importation de la bibliothèque PyAutoGUI pour le contrôle de la souris

# Initialisation de la capture vidéo depuis la caméra (index 0 pour la caméra par défaut)
cam = cv2.VideoCapture(0)

# Chargement du modèle de détection des points du visage avec l'option refine_landmarks=True pour une meilleure précision
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Obtention des dimensions de l'écran à l'aide de PyAutoGUI
screen_w, screen_h = pyautogui.size()
'''
# Désactivation du fail-safe de PyAutoGUI (non recommandé dans un environnement de production)
pyautogui.FAILSAFE = False
'''
# Boucle infinie pour traiter les images de la caméra en continu
while True:
    # Lecture d'une image depuis la caméra
    _, frame = cam.read()

    # Renversement horizontal de l'image (parfois nécessaire car les caméras retournent une image miroir)
    frame = cv2.flip(frame, 1)

    # Conversion de l'image en format RGB requis par MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Détection des points du visage sur l'image
    output = face_mesh.process(rgb_frame)

    # Extraction des points de repère du visage s'ils sont détectés
    landmark_points = output.multi_face_landmarks

    # Obtention des dimensions de l'image capturée
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        # Extraction des points de repère du visage pour chaque visage détecté
        landmarks = landmark_points[0].landmark

        # Boucle pour traiter les points de repère des yeux
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)  # Calcul de la coordonnée x de l'œil
            y = int(landmark.y * frame_h)  # Calcul de la coordonnée y de l'œil

            # Dessin d'un cercle sur l'image à l'emplacement de l'œil détecté
            cv2.circle(frame, (x, y), 3, (0, 255, 0), cv2.FILLED)

            # Déplacement de la souris si le deuxième œil est détecté (id == 1)
            if id == 1:
                screen_x = (screen_w / (frame_w) )* x# Calcul de la coordonnée x sur l'écran
                screen_y = (screen_h /(frame_h) )  * y  # Calcul de la coordonnée y sur l'écran
                pyautogui.moveTo(screen_x, screen_y)  # Déplacement de la souris

    # Extraction des points de repère du coin gauche de l'œil
    left = [landmarks[145], landmarks[159]]

    # Dessin de cercles sur l'image aux emplacements des coins gauche des yeux
    for landmark in left:
        x = int(landmark.x * frame_w)  # Calcul de la coordonnée x du coin gauche de l'œil
        y = int(landmark.y * frame_h)  # Calcul de la coordonnée y du coin gauche de l'œil
        cv2.circle(frame, (x, y), 3, (0, 255, 255), cv2.FILLED)

    # Détection d'un clignement d'œil (si l'écart vertical entre les deux points est inférieur à 0.004)
    if (left[0].y - left[1].y) < 0.004:
        print('click')  # Affichage d'un message de débogage
        pyautogui.click()  # Émission d'un clic de souris
        pyautogui.sleep(1)  # Pause d'une seconde

    # Affichage de l'image avec les annotations
    cv2.imshow('Eye Controlled mouse', frame)

    # Attente d'une touche pour quitter la boucle (attente maximale de 1 milliseconde)
    cv2.waitKey(1)
