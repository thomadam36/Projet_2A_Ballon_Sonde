# Projet_2A_Ballon_Sonde
Description de l'avancement du projet de deuxième année sur le ballon sonde atmosphérique

Nous avons dans ce projet le code utilisé pour récupérer les données de notre ballon sonde.

Les fichiers pythons capteurs (pour le MPL3115 et le DHT22) comprennent chacune une fonction d'initialisation des capteur et d'une fonction pour retourner chauque valeur mesurée par le capteur (humidité, température, pression, altitude).

Les fichiers pythons AllumeCamera et EteintCamera ont une fonction du même nom qui permettent d'allumer et d'éteindre la caméra.

Enfin la fonction ajouter dans ce même fichier python permet d'ajouter une donnée dans le fichier texte qui est créer au début de notre programme principal.

Toutes ces fonctions sont utilisées dans le programme python principal qui est vol.py. Celui-ci permet de prendre des données toutes les 30 secondes après 30 minutes (pour permettre au ballon de se gonfler). Puis à la descente à 5000m, on éteint la caméra (pour des soucis de législation au niveau des prises de vues).

La fonction testvol a permis de faire la démo et de vérifier l'ensemble des sous-fonctions utilisées.

la fonction lat-long permet de retourner les données du gps mais cela n'a pas été implémenté car le gps avait du mal à capter assez de satellites. De ce fait il faut une antenne mieux adaptée pour capter les satellites.

Pour lancer ce programme au démarrage, il faut écrire de lancer le fichier vol au démarrage et cela ce fait en écrivant la commande dans le fichier rc.local (fichier qui finit le boot au lancement).
