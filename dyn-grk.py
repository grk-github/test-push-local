#!/usr/bin/env python3
import json
import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
output = {
	'all': {
		'hosts': [],
		'vars': {
			'ansible_user': 'ec2-user',
			'ansible_ssh_private_key_file': './.ssh/demo-key'
		}
	},
    '_meta': {
        "hostvars": {}
        }
}
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            public_ip = instance['PublicIpAddress']
            output['all']['hosts'].append(public_ip)
            output['_meta']['hostvars'][public_ip] = {
                'ansible_host': public_ip
            }

print(json.dumps(output))
