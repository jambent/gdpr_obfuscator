import boto3


def get_file_from_s3_bucket(bucket, key):
    """
    Retrieves file from S3 bucket

    Args:
        bucket: target S3 bucket
        key:    target S3 file key
    Returns:
        Requested file
    """
    try:
        s3 = boto3.client("s3", region_name="eu-west-2")
        retrieved_file = s3.get_object(Bucket=bucket, Key=key)

        return retrieved_file

    except Exception as e:
        print(f"File retrieval from S3 bucket failed: {e}")
