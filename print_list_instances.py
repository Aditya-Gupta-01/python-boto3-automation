# Import all the modules and Libraries
import boto3
# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default",region_name="ap-south-1")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")
# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
result = ec2_console.describe_instances()['Reservations']
for each_instance in result:
    for value in each_instance['Instances']:
        # Print instance ID
        print("Instance ID:", value['InstanceId'])
        
        # Print instance Name if it exists
        instance_name = None
        if 'Tags' in value:
            for tag in value['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break
        if instance_name:
            print("Instance Name:", instance_name)
        else:
            print("Instance Name: [No name tag found]")
