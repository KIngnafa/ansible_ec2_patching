pipeline {
    agent any
    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
        ANSIBLE_CONFIG = '/var/ansible.cfg' 
	KEY = "$WORKSPACE/appkp.pem"
    }
    stages {
        stage ('Generate Inventory file') {
            steps {
                sh '''
		chmod +x $KEY
		echo $WORKSPACE
                python3 $WORKSPACE/instance_id.py
		
                '''
            }
        }

        stage ('Run Patching Playbook') {
            steps {
                sh '''
                ansible-playbook -i $WORKSPACE/hosts.ini $WORKSPACE/patch_ec2.yml
                '''
            }
        }
    }
}
