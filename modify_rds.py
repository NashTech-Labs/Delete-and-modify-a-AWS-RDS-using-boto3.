# import the boto3 which will use to interact  with the aws
import boto3

client = boto3.client('rds')

response = client.modify_db_instance(
    DBInstanceIdentifier=input("Enter the instance name"),
    MasterUserPassword=input("Enter the password")
    # DBInstanceIdentifier='database-instance-01',
    # MasterUserPassword='new-pa$$word'
  )  
print(response)