# import the boto3 which will use to interact  with the aws
import boto3

client = boto3.client('rds')
response = client.delete_db_instance(
    DBInstanceIdentifier= input("Enter the instance name"),
    # DBInstanceIdentifier='db-instance-01-readreplica',
    SkipFinalSnapshot=True,
)
print(response)