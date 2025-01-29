import boto3

aws_management_console = boto3.session.Session(profile_name="default", region_name="ap-south-1")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.stop_instances(
    ImageId='ami-08bf489a05e916bbd',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

#print(response)
