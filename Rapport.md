# Projet_2A_Ballon_Sonde
Description de l'avancement du projet de deuxième année sur le ballon sonde atmosphérique :

Nous avons placé dans ce dossier Github l'ensemble du code utilisé par l'électronique embarquée de notre ballon sonde. La plupart de ces codes sont en python et ont été implémentés sur une Raspberry Pi 4B.

Les fichiers pythons capteurs servent pour le MPL3115 (Pression, Altitude, Température) et le DHT22 (Température, Humidité). Ces fichiers comprennent chacun une fonction d'initialisation des capteurs et une fonction pour retourner chaque valeur mesurée par le capteur (humidité, température, pression, altitude selon le capteur).

Les fichiers pythons AllumeCamera et EteintCamera contiennent une fonction du même nom et ils nous permettent de gérer la caméra emabrquée dans notre ballon sonde (de l'allumage jusqu'à l'extinction.)

Enfin la fonction ajouter dans ce même fichier python permet d'écrire une donnée dans le fichier texte à chaque fois qu'un capteur vient faire une acquisition. Ce fichier texte est créé au début de notre programme principal.

Toutes ces fonctions sont utilisées dans le programme python principal qui est vol.py. Il est un peu comme le cerveau général qui coordonne tout le reste. Celui-ci permet de faire des acquisitions toutes les 30 secondes après un temps de pause de 30 minutes (ces minutes correspondent au temps pour nous permettre de gonfler le ballon au départ). Il nous permet aussi déteindre la caméra à la descente à 5000m du sol pour des soucis de législation au niveau des prises de vues.

La fonction testvol est une fonction inutile lors du véritable vol mais qui nous a permis de faire la démonstration lors de la présentation du projet et a aussi permis de vérifier l'ensemble des sous-fonctions utilisées.

La fonction lat-long (pour lattitude et longitude) permet de retourner les données acquises par le gps 

Pour lancer ce programme au démarrage, il faut spécifier à la Raspberry Pi de lancer le fichier vol à son démarrage. Cela se fait en écrivant une ligne de commande dans le fichier rc.local (fichier qui finit le boot au moment du lancement).
