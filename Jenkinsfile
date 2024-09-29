pipeline {
	agent any 
	environment {
		ANSIBLE_HOST_KEY_CHECKING = 'False'
		ANSIBLE_CFG = '$WORKSPACE/ansible.cfg'
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
				sh '''
				ansible-playbook -i $WORKSPACE/host.ini $WORKSPACE/patch_ec2.yml
				'''
				}
			}
		}
	}	
