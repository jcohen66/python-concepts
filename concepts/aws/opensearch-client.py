import boto3

class OpenSearch:
  def __init__(self, region, endpoint, access_key, secret_key):
    self.region = region
    self.endpoint = endpoint
    self.access_key = access_key
    self.secret_key = secret_key
    self.client = boto3.client('opensearch', region_name=self.region, endpoint_url=self.endpoint, aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)

  def search(self, index_name, query):
    response = self.client.search(
      query=query,
      indexName=index_name
    )
    return response

# Example usage
opensearch = OpenSearch('us-east-1', 'https://opensearch.us-east-1.amazonaws.com', 'ACCESS_KEY', 'SECRET_KEY')
response = opensearch.search('my_index', 'my_query')