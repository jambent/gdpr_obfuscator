import json
import os
import boto3
import obfsc8 as ob


def lambda_handler(event, context):

    try:
        obfuscation_instructions = json.dumps(event["detail"])
        buffer = ob.obfuscate(obfuscation_instructions)

        source_filepath_elements = event["detail"]["file_to_obfuscate"].split(
            "/")
        source_filepath_elements[-1] = "obfs_" + source_filepath_elements[-1]
        obfuscated_file_key = ("/").join(source_filepath_elements[3:])

        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = os.environ['DESTINATION_S3_ID']
        (s3.put_object(
            Bucket=bucket,
            Key=obfuscated_file_key, Body=buffer))

        return {'statusCode': 200, 'body': json.dumps(
            f"Successfully obfuscated: {obfuscation_instructions}")}

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Failed to obfuscate file: {e}")
        }
