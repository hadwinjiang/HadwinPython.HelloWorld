import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete a user
iam.delete_user(
    UserName='NEW_IAM_USER_NAME'
)