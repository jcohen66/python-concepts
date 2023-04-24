import boto3

# Set up a Boto3 Athena client
client = boto3.client('athena', region_name='your-region')

# Set the Athena query string
query_string = 'SELECT * FROM your_table'

# Set the query execution context, including the database and output format
query_execution_context = {
    'Database': 'your_database',
    'OutputLocation': 's3://your-bucket/your-path/',
}

# Execute the query and wait for the results
query_execution = client.start_query_execution(
    QueryString=query_string,
    QueryExecutionContext=query_execution_context,
    ResultConfiguration={
        'OutputLocation': 's3://your-bucket/your-path/'
    }
)
query_execution_id = query_execution['QueryExecutionId']
query_execution_status = client.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']
while query_execution_status == 'RUNNING':
    query_execution_status = client.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']

# Get the query results as a dictionary
query_results = client.get_query_results(QueryExecutionId=query_execution_id)
result_dict = {}
for row in query_results['ResultSet']['Rows'][1:]:
    result_dict[row['Data'][0]['VarCharValue']] = row['Data'][1]['VarCharValue']

print(result_dict)
