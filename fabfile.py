
#!/usr/bin/env python

from fabric.api import cd, run, env, task, prefix

env.hosts = ['localhost']

@task
def ping_client():
    run('ping node-routeur')

@task
def run_playbook():
    with cd('/home/user-ansible/ansible2.7.10/local/bin'):
	with prefix('. ../bin/activate'):
            run('ansible-playbook -i /home/user-ansible/.ansible/inventaire.ini --user user-ansible --become --ask-become-pass /home/user-ansible/.ansible/install-roles.yml')
