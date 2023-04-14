import boto3


class SNSWrapper:
    def init(self, region_name, access_key_id, secret_access_key):
        self.client = boto3.client('sns', region_name=region_name,
                                   aws_access_key_id=access_key_id,
                                   aws_secret_access_key=secret_access_key)

    def publish_json(self, topic_arn, payload):
        self.client.publish(TopicArn=topic_arn, Message=json.dumps(payload))

    def subscribe(self, topic_arn, protocol, endpoint):
        self.client.subscribe(TopicArn=topic_arn,
                              Protocol=protocol, Endpoint=endpoint)
