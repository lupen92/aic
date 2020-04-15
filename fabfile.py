
#!/usr/bin/env python

#Importation des modules ci-dessous grace au fabric.api, installe avec la commande pip install fabric3
from fabric.api import cd, run, env, task, prefix

#Definition du hote sur lequel tourne l'env
env.hosts = ['localhost']

#Creation du fonction ping_client, permettant de faire un ping vers node-routeur
@task
def ping_client():
    run('ping node-routeur')

#Creation du fonction run_playbook, permettant de demarrer le playbook vers node-routeur
@task
def run_playbook():
    with cd('/home/user-ansible/ansible2.7.10/local/bin'):
	with prefix('. ../bin/activate'):
            run('ansible-playbook -i /home/user-ansible/.ansible/inventaire.ini --user user-ansible --become --ask-become-pass /home/user-ansible/.ansible/install-roles.yml')
