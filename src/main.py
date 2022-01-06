import json

def lambda_handler(event, context):
  print('Hello, world')
  # TODO implement
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
  }