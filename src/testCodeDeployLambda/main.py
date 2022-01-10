import json

def lambda_handler(event, context):
  if 'status' in event.keys():
    if event['status'] == 'test':
      return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
      }
    else:
      return {
        'statusCode': 400,
        'body': json.dumps('Not found status')
      }
  return {
    'statusCode': 400,
    'body': json.dumps('Not found input data')
  }