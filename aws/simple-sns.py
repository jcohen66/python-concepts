import boto3
import json
import env

def main():
    topicArn = 'arn...'
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=env.accessKey,
        aws_secret_access=env.secretKey,
        region_name='us-east-1'
    )
    
    response = snsClient.publish(TopicArn=topicArn,
                                 Message=json.dumps(publishObject),
                                 Subject='PURCHASE',
                                 MessageAttributes = {"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}})
    
    print(response['ResponseMetaData']['HTTPStatusCode'])