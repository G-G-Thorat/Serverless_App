import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event['body'])
    name = body['name']
    email = body['email']
    message = body['message']
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ContactForm')
    table.put_item(Item={'email': email, 'name': name, 'message': message})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'msg': 'Saved successfully'})
    }
