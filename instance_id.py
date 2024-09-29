import boto3
import botocore
import json
import os
import subprocess
from botocore.exceptions import ClientError

WORKSPACE=os.getenv("WORKSPACE")


# Assume role in the dev account
sts_client = boto3.client('sts')

# Requesting temporary credentials
response_source = sts_client.assume_role(
    RoleArn="arn:aws:iam::891377046654:role/Engineer",
    RoleSessionName="Engineer@Dev"
)

# Extracting temporary credentials
credentials = response_source['Credentials']

region_name = 'us-east-1'

# Creating a new session using the assumed role credentials
session = boto3.Session(
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
    region_name=region_name
)


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
            private_key_file = '{}/appkp.pem'.format(WORKSPACE)

            # Write each instance details in the desired format using %s formatting

            f.write("%s ansible_host=%s ansible_user=%s ansible_ssh_private_key_file=%s\n" %
                    (instance_id, public_ip, ansible_user, private_key_file))

print("Ansible inventory file has been written to %s" % output_file)



