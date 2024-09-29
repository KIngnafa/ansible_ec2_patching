pipeline {
	agent any 
	environment {
		ANSIBLE_HOST_KEY_CHECKING = 'False'
	}
	stages {
		stage ('Generate Inventory file') {
			steps {
				sh '''
				python3 instance_id.py
				'''
				}
			}

		stage ('Run Patching Playbook')
			steps {
				sh '''
				ansible-playbook -i host.ini patch_ec2.yml
				'''
				}
			}
		}
	
