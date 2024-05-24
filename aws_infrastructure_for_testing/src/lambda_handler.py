import json
import boto3
import obfsc8 as ob

def lambda_handler(event, context):

    obfuscation_instructions = json.dumps(event["detail"])
    print(obfuscation_instructions)
     
    buffer = ob.obfuscate(obfuscation_instructions)
    s3 = boto3.client("s3", region_name="eu-west-2")
    put_response = (s3.put_object(
        Bucket="obfuscator-destination-bucket-84628959687373",
        Key="test_csv.csv", Body=buffer))
            
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }