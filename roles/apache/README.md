Role Apache et PHP
=========

Ce role permets d'installer le paquet Apache et PHP, nécessaires pour monter un serveur Web


Prérequis
------------

Aucun prérequis est demandé sur le serveur lui-même avant l'installation de ces deux paquets (les sources de Debian 9 sont à jour dès son installation)


Contenu du main.yml
----------------

Le fichier main.yml contient les lignes ci-dessous :

Etape 1 : Cette tâche permets d'installer Apache à l'aide du module apt

     - name: "apache installation"
       apt:
         name: "apache2"
         state: "present"

Etape 2 : Cette tâche active le service apache2

      - name: "apache service activation"
        service:
           name: "apache2"
           state: "started"
           enabled: "yes"
           
Etape 3 : Cette tâche fait appel à un autre fichier de conf pour installer php7

      - name: "install php7"
        apt:
           name: "php"
           state: latest