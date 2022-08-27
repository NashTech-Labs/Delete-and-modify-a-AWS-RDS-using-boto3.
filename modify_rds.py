# import the boto3 which will use to interact  with the aws
import boto3

# We will take the all imput from the end user.

# You need to enter rds as input
AWS_service= input("Enter the service name\n")

database_name=input("Enter the database name\n")

user_password=input("Enter the password to modify\n")

res = boto3.client(AWS_service)

modify_rds = res.modify_db_instance(
  
    DBInstanceIdentifier=database_name,
    MasterUserPassword=user_password
  )  
print(modify_rds)

print("Your RDS has been modified Successfully ")