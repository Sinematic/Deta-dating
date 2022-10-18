# Deta

### L'appli de date pour les gens *Deta*rminés

Globalement, l'application semble a priori assez traditionnelle,
des profils sont soumis à l'utilisateur et il choisit de swipe à droite ou à gauche
(comprendre : aimer le profil ou l'ignorer). Si deux utilisateurs ont aimé le profil
de l'autre: il y a match.

En cas de match, il devient alors possible de d'interagir grâce à un chat privé.

À terme, différentes fonctionnalités seront déployées afin de permettre d'effectuer des
recherches de profils en prenant en compte certains paramètres très précis!

Voici une **première ébauche** de l'intégration du site:

![](schema.png)

Au début, ce sera une **application web** qui pourrait être revue / adaptée au **format mobile.**

Niveau technologies:  
- du Python au menu (avec des modules tels que Socket et Threading) 
- MySQL/SQL pour la base de données
- une pincée de CSS maison & Bootstrap
- Kivy pour "émuler" le mouvement du Swipe
- un moyen d'assimiler de réutiliser la géolocalisation des utilisateurs
- Flask suivant l'avancée du projet

<br/>

Un petit aperçu après une rapide intégration de la page de Swipe

![](1.png)


<br/>

Liens utiles :

- https://trello.com/b/7qF1CnO5/dating-app
- https://kivy.org/
- https://flask.palletsprojects.com/en/2.2.x/