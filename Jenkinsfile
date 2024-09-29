pipeline {
	agent any 
	environment {
		ANSIBLE_HOST_KEY_CHECKING = 'False'
	}
	stages {
		stage ('Generate Inventory file') {
			steps {
				sh '''
				chmod 700 $WORKSPACE/instance_id.py
				python3 /home/ec2-user/ansible_ec2_patching/instance_id.py
				'''
				}
			}

		stage ('Run Patching Playbook') {
			steps {
				sh '''
				ansible-playbook -i /home/ec2-user/ansible_ec2_patching/host.ini patch_ec2.yml
				'''
				}
			}
		}
	}	
