pipeline {
	agent any 
	environment {
		ANSIBLE_HOST_KEY_CHECKING = 'False'
		ANSIBLE_CONFIG = '/var/ansible.cfg'
	}
	stages {
		stage ('Generate Inventory file') {
			steps {
				sh '''
				python3 $WORKSPACE/instance_id.py
				'''
				}
			}

		stage ('Run Patching Playbook') {
			steps {
				sh label: '', script: 'export ANSIBLE_CONFIG=$ANSIBLE_CONFIG'
				ansible-playbook -i $WORKSPACE/host.ini $WORKSPACE/patch_ec2.yml
				'''
				}
			}
		}
	}	
