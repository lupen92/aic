Role POSTFIX
=========

Ce role permets d'installer le paquet postfix, nécessaires pour envoyer des mails depuis notre routeur


Prérequis
------------

Aucun prérequis est demandé sur le serveur lui-même avant l'installation de ce paquet (les sources de Debian 9 sont à jour dès son installation)


Contenu du main.yml
----------------

Le fichier main.yml contient les lignes ci-dessous :

Etape 1. Cette tâche permets d'installer postfix à l'aide du module apt

     - name: "postfix installation"
       apt:
         name: "postfix"
         state: "present"

Etape 2. Cette tâche active le service postfix

     - name: "postfix service activation"
       service:
         name: "postfix"
         state: "started"
         enabled: "yes"

Etape 3. Ajout du fichier de configuration

     - name: "copie du fichier main.cf vers le répertoire /etc/postfix"
       copy:
         src: /home/user-ansible/.ansible/roles/postfix/tasks/main.cf
         dest: /etc/postfix/main.cf
         owner: root
         mode: '0644'

Etape 4. Ajout du fichier de configuration

     - name: "copie du fichier sasl_pawwd vers le répertoire /etc/postfix"
       copy:
         src: /home/user-ansible/.ansible/roles/postfix/tasks/sasl_passwd
         dest: /etc/postfix/sasl_passwd
         owner: root
         mode: '0644'

Etape 5. Ajout du fichier de configuration

     - name: "copie du fichier sasl_passwd.db vers le répertoire /etc/postfix"
       copy:
         src: /home/user-ansible/.ansible/roles/postfix/tasks/sasl_passwd.db
         dest: /etc/postfix/sasl_passwd.db
         owner: root
         mode: '0644'

Le fichier main.cf contient la configuration du relay SMTP (dans mon cas, j'ai utilisé mon compte GMAIL) avec le serveur SMTP, son port et le protocole.
Ce fichier permets d'avoir un role postfix déjà configuré suite à son déploiement sur le routeur

Les fichier sasl_passwd et sasl_passwd.db contiennent le mot de passe du compte GMAIL en mode base de données qui est lu par postfix lors de l'envoi mail.




