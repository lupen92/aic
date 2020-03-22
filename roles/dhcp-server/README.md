Role DHCP
=========

Ce role permets d'installer le paquet DHCP, nécessaire pour donner des adresses IP en automatique aux postes


Prérequis
------------

Aucun prérequis est demandé sur le serveur lui-même avant l'installation de ce paquet (les sources de Debian 9 sont à jour dès son installation)


Contenu du main.yml
----------------

Le fichier main.yml contient les lignes ci-dessous :

## Etape 1. Cette tâche permets d'installer le service ISC DHCP à l'aide du module apt

```yaml
 
      - name: "isc-dhcp-server installation"
        apt:
          name: "isc-dhcp-server"
          state: "present"  
```

## Etape 2. Ajout du fichier de configuration contenant la configuration de chaque interface (range, passerelle, DNS, etc..)

```yaml

      - name: "copie du fichier dhcpd.conf vers le répertoire /etc/dhcp"
        copy:
          src: /home/user-ansible/.ansible/roles/dhcp-server/tasks/dhcpd.conf
          dest: /etc/dhcp/dhcpd.conf
          owner: root
          mode: '0644'
```

## Etape 3. Ajout du fichier de configuration contenant les interfaces qui seront utilisées pour déployer du DHCP

```yaml

       - name: "copie du fichier isc-dhcp-server vers le répertoire /etc/default"
         copy:
           src: /home/user-ansible/.ansible/roles/dhcp-server/tasks/isc-dhcp-server
           dest: /etc/default/isc-dhcp-server
           owner: root
           mode: '0644'
```

## Etape 4. Cette tâche active le service dhcp

```yaml

        - name: "isc-dhcp-server service activation"
          systemd:
            name: "isc-dhcp-server"
            state: "started"
            enabled: "yes"
```
            
Le fichier dhcpd.conf contient le paramétrage des réseaux pour les différents services internes.
Ce paramétrage contient le pool d'adresses proposées, la passerelle, le DNS et le domaine de recherche.

Le fichier isc-dhcp-server contient les interfaces réseaux qui seront autorisées à déployer des adresses en DHCP.
 
 
 
