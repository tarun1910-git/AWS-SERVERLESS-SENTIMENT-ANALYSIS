import json
import boto3

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    # event['body'] may come as JSON string
    if 'body' in event and isinstance(event['body'], str):
        body = json.loads(event['body'])
    else:
        body = event  # in test calls without API Gateway

    text = body['text']  # Will now work

    sentiment_response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )

    sentiment = sentiment_response['Sentiment']
    sentiment_score = sentiment_response['SentimentScore']

    # Optional: Save result to S3
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='sentiment-analysis-results-2025',
        Key='results/latest_result.json',
        Body=json.dumps({
            'input': text,
            'sentiment': sentiment,
            'score': sentiment_score
        })
    )
   
    # Save result to S3
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='sentiment-analysis-results-2025',
        Key='results/latest_result.json',
        Body=json.dumps({
            'input': text,
            'sentiment': sentiment,
            'score': sentiment_score
        })
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'sentiment': sentiment,
            'score': sentiment_score
        })
    }
