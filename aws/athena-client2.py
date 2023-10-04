# sourcery skip: avoid-builtin-shadow
import boto3
import time

client = boto3.client('athena')

response_query = client.start_query_execution(
    QueryString='SELECT * FROM "dev_raw"."vw_openactive_api_individual_facility_use_slots_offers" limit 10;',
    QueryExecutionContext={
        'Database': 'dev_raw'
    },
    ResultConfiguration={
        'OutputLocation': 's3://athena-results-usta/athena-results/unsaved'
    },
    WorkGroup='primary'
    
)
time.sleep(60)
id = response_query['QueryExecutionId']
response = client.get_query_results(
    QueryExecutionId=id,
    MaxResults=10
)
print(response)



