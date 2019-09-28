import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-02f706d959cedf892',
     MinCount=1,
     MaxCount=4,
     InstanceType='t2.medium',
     KeyName='vinod-keypair'
 )
