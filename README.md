# This basic python program not only creates a key pair in AWS, it also captures and stores it on your local machine. We can use this keypair to ssh into virtual machines later.
Below are the steps involved to proceed further.
1.create a user and get AWS access ID and Secret Key(Programatic access)
2.Set permissions(eg: EC2FullAccess) 
3.Download the keys and keep it secure( eg: S3, Vault or etc)
4.Configure AWS Credentials locally.(aws cnfigure) and provide the inputs and check credentials works well with AWS cli tools. 
5.Run the python script to create ec2-keypair 
6.provide 400 permission to the keypair. 7.run the ec2-instance provisioning script.
