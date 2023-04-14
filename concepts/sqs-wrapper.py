import boto3


class SQSWrapper:
    def __init__(self, queue_url):
        self.sqs = boto3.client('sqs')
        self.queue_url = queue_url

    def push_json(self, data):
        self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(data)
        )

    def pop_json(self):
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1
        )
        if 'Messages' in response:
            message = response['Messages'][0]
            body = message['Body']
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
            return json.loads(body)
        return None


def pop_json_with_backoff(self):
        # Initialize the backoff delay to 0
        backoff_delay = 0

        while True:
            response = self.sqs.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=1
            )
            if 'Messages' in response:
                message = response['Messages'][0]
                body = message['Body']
                self.sqs.delete_message(
                    QueueUrl=self.queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                return json.loads(body)
            else:
                # If there are no messages, wait for the backoff delay before trying again
                time.sleep(backoff_delay)
                # Increase the backoff delay for the next iteration
                backoff_delay = min(backoff_delay + 1, 32)

    def peek(self):
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1,
            VisibilityTimeout=0
        )
        if 'Messages' in response:
            message = response['Messages'][0]
            body = message['Body']
            return json.loads(body)
        return None
