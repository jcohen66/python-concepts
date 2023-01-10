import boto3


class S3Connection:
    def __init__(self, access_key, secret_key, region_name):
        self.s3 = boto3.client('s3', aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key,
                               region_name=region_name)

    def create_bucket(self, bucket_name):
        self.s3.create_bucket(Bucket=bucket_name)

    def create_folder(self, bucket_name, folder_name):
        self.s3.put_object(Bucket=bucket_name, Key=folder_name+'/')

    def write_object(self, bucket_name, file_name, file_content):
        self.s3.put_object(Bucket=bucket_name,
                           Key=file_name, Body=file_content)

    def read_file(self, bucket_name, file_name):
        response = self.s3.get_object(Bucket=bucket_name, Key=file_name)
        return response['Body'].read()


# Example usage
conn = S3Connection('ACCESS_KEY', 'SECRET_KEY', 'REGION_NAME')
conn.create_bucket('my-bucket')
conn.create_folder('my-bucket', 'folder1')
conn.write_object('my-bucket', 'folder1/file1.txt', b'Hello, World!')
content = conn.read_file('my-bucket', 'folder1/file1.txt')
print(content)  # b'Hello, World!'
