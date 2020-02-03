Projet 6, participez à la vie de la communauté OpenSource

====================

Scenario dans ce projet est le suivant : 

Une machine (serveur) sous Debian 9 Stretch sert de Node-Manager contenant les roles à déployer.

Une machine (client) sous Debian 9 Stretch sert comme routeur et recoit via SSH les commandes du playbook (Apache, Postfix, IPTables, DHCP).

Ce scénario est réalisé sur un réseau dédié dans GNS3


Le répertoire actuel contient le contenu ci-dessous:
- Répertoire Roles, contenant les rôles qui seront déployé dans notre scenario.
- Le fichier inventaire.ini, contenant le nom du routeur qui va recevoir ces rôles.
- Le fichier install-roles.yml permettant d'appeler les fichiers yml dans le répertoire rôle et pouvoir les déployer.
Le lancement de ces rôles se fait via la commande ansible-playbook, comme indiqué ci-dessous:
ansible-playbook -i inventaire.ini --user user-ansible --become --ask-become-pass install-roles.yml

# Le fichier install-roles.yml est présenté comme ci-dessous :

---------------------------------------------------------------------------

Etape 1 : Appeler le role apache afin de le déployer sur le serveur node-routeur. Ce rôle permets d'installer le paquet apache avec la dernière version de PHP 

      - name: "Installation apache"
        hosts: node-routeur
        roles:
          - role: "apache"
          php_install: "yes"

Etape 2 : Appeler le role iptables, permettant d'installer le paquet iptables-persistent afin de sauvegarder les règles ajoutées ou modifiées durant le travail

      - name: "Installation Iptables"
        hosts: node-routeur
        roles:
          - role: "iptables"

Etape 3 : Appeler le role postfix, permettant d'installer le paquet postifx afin d'envoyer des mails depuis notre routeur vers des destinataires externes ou internes

       - name: "Installation postfix"
         hosts: node-routeur
         roles:
           - role: "postfix"

Etape 4 : Appeler le role dhcp-serveur, permettant d'installer le paquet isc-dhcp-serveur sur notre routeur afin de distribuer des adresses IP aux nouveaux postes (PC, portables, téléphones, etc..) qui rejoignent le parc informatique

       - name: "Installation isc-dhcp-server"
         hosts: node-routeur
         roles:
           - role: "dhcp-server"


Avec ces roles, nous pouvons deployer la configuration d'un routeur sous Debian de façon automatique et très rapide.
