Role IPTABLE
=========

Ce role permets d'installer le paquet iptables-persistent, nécessaires pour sauvegarder les modifications du pare-feu


Prérequis
------------

Aucun prérequis est demandé sur le serveur lui-même avant l'installation de ce paquet (les sources de Debian 9 sont à jour dès son installation)


Contenu du main.yml
----------------

Le fichier main.yml contient les lignes ci-dessous :

## Etape 1. Cette tâche permets d'installer iptables-persistent à l'aide du module apt, ce qui permettra de sauvegarder les règles du pare-feu

```yaml

       - name: "iptables-persistent installation"
         apt:
           name: "iptables-persistent"
           state: "present"
```

## Etape 2. Cette tâche active le service iptables

```yaml

       - name: "iptables service activation"
         systemd:
           name: "netfilter-persistent"
           state: "started"
           enabled: "yes"
```

## Etape 3. Ajout du fichier interfaces pour configurer les cartes réseaux du routeur

```yaml

       - name: "copie du fichier interfaces vers le répertoire /etc/network/interfaces"
         copy:
           src: /home/user-ansible/.ansible/roles/iptables/tasks/interfaces
           dest: /etc/network/interfaces
           owner: root
           mode: '0644'
 
```

## Etape 3. Ajout du fichier de configuration

```yaml

       - name: "copie du fichier rules.v4 vers le répertoire /etc/iptables"
         copy:
           src: /home/user-ansible/.ansible/roles/iptables/tasks/rules.v4
           dest: /etc/iptables/rules.v4
           owner: root
           mode: '0644'
```

## Etape 4. Autorisation ip_forward pour accès internet

```yaml

       - name: "changement valeur sur ip_forward"
         shell:
           echo '1' >> /proc/sys/net/ipv4/ip_forward
```
           
Le fichier rules.v4 contient des règles déjà faites sur des plusieurs interfaces afin d'isoler le réseau des services internes.
Ce fichier est pratique lorsqu'on doit deployer des règles sur plusieurs routeurs via Ansible.

La commande sur l'étape 4 permets d'autoriser l'ip forward, ce qui permettra aux postes clients d'accéder à l'internet via le routeur Debian



