import boto3
import json

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    for record in event['Records']:
        # Get the S3 bucket and key where the object was uploaded
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Analyze the picture with Amazon Rekognition
        response = rekognition.recognize_celebrities(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}}
        )

        # Get the list of detected celebrities
        celebrities = []
        for celebrity in response['CelebrityFaces']:
            celebrities.append(celebrity['Name'])

        # Store the results in DynamoDB
        table = dynamodb.Table('test')
        table.put_item(
            Item={
                'ImageName': key,
                'detected_celebrities': celebrities,
                'upload_time': str(record['eventTime'])
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Picture analysis complete.')
    }