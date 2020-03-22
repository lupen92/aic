# Projet 6, participez à la vie de la communauté OpenSource

====================

Scenario dans ce projet est le suivant : 

Une machine (serveur) sous Debian 9 Stretch sert de Node-Manager contenant les roles à déployer.

Une machine (client) sous Debian 9 Stretch sert comme routeur et recoit via SSH les commandes du playbook (Apache, Postfix, IPTables, DHCP).

Ce scénario est réalisé sur un réseau dédié dans GNS3


Le répertoire actuel contient le contenu ci-dessous:
- Répertoire Roles, contenant les rôles qui seront déployé dans notre scenario.
- Le fichier inventaire.ini, contenant le nom du routeur qui va recevoir ces rôles.
- Le fichier fabfile.py est un script en python (framework fabric) permettant d'appeler la commande pour lancer le playbook, ce qui permets un lancement facile et rapide.
- Le fichier install-roles.yml (qui est appelé par fab) permet d'appeler les fichiers yml dans le répertoire rôle et pouvoir les déployer.
Le lancement de ces rôles se fait via la commande fab , comme indiqué ci-dessous:
fab install-roles

Le fichier fabfile est présenté comme ci-dessous :

## Import des librairies Python

```python

from fabric.api import cd, run, env, task, prefix
```

## L'importation des modules from fabric.api est possible à condition que le framework soit installé avec la commande ci-dessous (je mets également la commande pour installer pip, obligatoire pour installer les libraires python)

```bash

sudo apt-get install pip
sudo pip install fabric3
```
 
 ## Création des tâches (les modules qui seront appelés par fabric)

```python

@task
def ping_client():
    run('ping node-routeur')

@task
def run_playbook():
    with cd('/home/user-ansible/ansible2.7.10/local/bin'):
	with prefix('. ../bin/activate'):
            run('ansible-playbook -i /home/user-ansible/.ansible/inventaire.ini --user user-ansible --become --ask-become-pass /home/user-ansible/.ansible/install-roles.yml')
```

 Le fichier install-roles.yml est présenté comme ci-dessous :

---------------------------------------------------------------------------

## Etape 1 : Appeler le role apache afin de le déployer sur le serveur node-routeur. Ce rôle permets d'installer le paquet apache avec la dernière version de PHP

```yaml

      - name: "Installation apache"
        hosts: node-routeur
        roles:
          - role: "apache"
          php_install: "yes"
```

## Etape 2 : Appeler le role iptables, permettant d'installer le paquet iptables-persistent afin de sauvegarder les règles ajoutées ou modifiées durant le travail

```yaml

      - name: "Installation Iptables"
        hosts: node-routeur
        roles:
          - role: "iptables"
```

## Etape 3 : Appeler le role postfix, permettant d'installer le paquet postifx afin d'envoyer des mails depuis notre routeur vers des destinataires externes ou internes

```yaml

       - name: "Installation postfix"
         hosts: node-routeur
         roles:
           - role: "postfix"
```

## Etape 4 : Appeler le role dhcp-serveur, permettant d'installer le paquet isc-dhcp-serveur sur notre routeur afin de distribuer des adresses IP aux nouveaux postes (PC, portables, téléphones, etc..) qui rejoignent le parc informatique

```yaml

       - name: "Installation isc-dhcp-server"
         hosts: node-routeur
         roles:
           - role: "dhcp-server"
```


Avec ces roles, nous pouvons deployer la configuration d'un routeur sous Debian de façon automatique et très rapide.
