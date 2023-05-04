import boto3
from django.conf import settings
# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id='AKIAQP2LLV3QABH45LHY',
    aws_secret_access_key='xckJ0XZJo7QHGszrH+9GSk5wTSZXEQ6cuU3fyZSd',
    region_name='ap-south-1',
)

# Send your sms message.
def sendSms(data:dict):
    try:
        client.publish(
            PhoneNumber=data['mobile'],
            Message=data['message']
        )
        return True
    except Exception as e:
        print(e)
        return False