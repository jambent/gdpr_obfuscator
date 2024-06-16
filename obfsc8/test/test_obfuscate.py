from moto import mock_aws
import pandas as pd
import boto3
import io

from obfsc8.src.obfsc8.obfuscate \
    import obfuscate
from test_data.test_dataframe import test_dataframe


@mock_aws
def test_that_csv_file_results_in_csv_bytes_object():
    s3 = boto3.client('s3', region_name="eu-west-2")

    s3.create_bucket(Bucket="test_bucket",
                     CreateBucketConfiguration={
                            'LocationConstraint': "eu-west-2"
                     }
                     )

    test_csv = test_dataframe.write_csv()
    s3.put_object(Bucket="test_bucket", Key="test_csv.csv", Body=test_csv)

    test_csv_json = """{
    "file_to_obfuscate": "s3://test_bucket/test_csv.csv",
    "pii_fields": ["name", "email_address"]
    }"""

    buffer = obfuscate(test_csv_json)
    df = pd.read_csv(buffer)
    assert isinstance(df, pd.DataFrame)


@mock_aws
def test_that_parquet_file_results_in_parquet_bytes_object():
    s3 = boto3.client('s3', region_name="eu-west-2")
    s3.create_bucket(Bucket="test_bucket",
                     CreateBucketConfiguration={
                            'LocationConstraint': "eu-west-2"
                     }
                     )

    test_parquet = io.BytesIO()
    test_dataframe.write_parquet(test_parquet)
    test_parquet.seek(0)
    s3.put_object(
        Bucket="test_bucket",
        Key="test_parquet.parquet",
        Body=test_parquet)

    test_parquet_json = """{
    "file_to_obfuscate": "s3://test_bucket/test_parquet.parquet",
    "pii_fields": ["name", "email_address"]
    }"""
    buffer = obfuscate(test_parquet_json)
    df = pd.read_parquet(buffer)
    assert isinstance(df, pd.DataFrame)


@mock_aws
def test_that_json_file_results_in_json_bytes_object():
    s3 = boto3.client('s3', region_name="eu-west-2")
    s3.create_bucket(Bucket="test_bucket",
                     CreateBucketConfiguration={
                            'LocationConstraint': "eu-west-2"
                     }
                     )

    test_json_file = test_dataframe.write_json(row_oriented=True)
    s3.put_object(
        Bucket="test_bucket",
        Key="test_json.json",
        Body=test_json_file)

    test_json_json = """{
    "file_to_obfuscate": "s3://test_bucket/test_json.json",
    "pii_fields": ["name", "email_address"]
    }"""
    buffer = obfuscate(test_json_json)
    df = pd.read_json(buffer)
    assert isinstance(df, pd.DataFrame)
