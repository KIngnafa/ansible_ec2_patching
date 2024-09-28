import boto3
import botocore
import json
import os
import subprocess
from botocore.exceptions import ClientError

#setting environemt variables 
os.environ["AWS_PROFILE"]="default"

session = boto3.Session()


ec2=session.client('ec2')

tag_key= 'Environment'
tag_value= 'Development'


output_file = 'hosts.ini'


# Describe instances with the specific tag
response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:%s' % tag_key,
                'Values': ['%s' % tag_value]  # Ensure this is a list
            }
        ]
    )

#opening file to write into it
with open(output_file,'w') as f:
    f.write("[development]\n")


# Loop through the response to gather instance details and write to file
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            public_ip = instance.get('PublicIpAddress', 'No Public IP')
            ansible_user = 'ec2-user'
            private_key_file = '/home/ec2-user/appkp.pem'

            # Write each instance details in the desired format using %s formatting
            f.write("%s ansible_host=%s ansible_user=%s ansible_ssh_private_key_file=%s\n" %
                    (instance_id, public_ip, ansible_user, private_key_file))

print("Ansible inventory file has been written to %s" % output_file)



