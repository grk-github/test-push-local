import boto3
ec2 = boto3.resource('ec2')
#create a list of instances which are running state
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])
#create a list of instance ids
ids = [ instance.id for instance in instances ]
#if any running instances found, terminate them
if ids:
    print("Found instances, terminating them:", ids)
    response = ec2.instances.filter(InstanceIds = ids).terminate()
    print(response)
else:
    print("no running instances found !")
