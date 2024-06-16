import pytest
import boto3
from moto import mock_aws
import io


from obfsc8.src.obfsc8.get_file_object_from_s3_bucket \
    import get_file_object_from_s3_bucket
from test_data.test_dataframe import test_dataframe


@pytest.fixture(scope="function")
def s3_client():
    with mock_aws():
        yield boto3.client('s3', region_name="eu-west-2")


@pytest.fixture
def test_bucket(s3_client):
    s3_client.create_bucket(Bucket="test_bucket",
                            CreateBucketConfiguration={
                                'LocationConstraint': "eu-west-2"
                            }
                            )


@pytest.fixture()
def csv_from_s3(s3_client, test_bucket):
    test_csv = test_dataframe.write_csv()
    s3_client.put_object(
        Bucket="test_bucket",
        Key="test_csv.csv",
        Body=test_csv)

    csv_file_object_from_s3 = get_file_object_from_s3_bucket(
        bucket="test_bucket", key="test_csv.csv")

    return csv_file_object_from_s3


@pytest.fixture()
def parquet_from_s3(s3_client, test_bucket):
    buffer = io.BytesIO()
    test_dataframe.write_parquet(buffer)
    buffer.seek(0)
    s3_client.put_object(
        Bucket="test_bucket",
        Key="test_parquet.parquet",
        Body=buffer)

    parquet_file_object_from_s3 = get_file_object_from_s3_bucket(
        bucket="test_bucket", key="test_parquet.parquet")

    return parquet_file_object_from_s3


@pytest.fixture()
def json_from_s3(s3_client, test_bucket):
    buffer = io.BytesIO()
    test_dataframe.write_json(buffer, row_oriented=True)
    buffer.seek(0)
    s3_client.put_object(
        Bucket="test_bucket",
        Key="test_json.json",
        Body=buffer)

    json_file_object_from_s3 = get_file_object_from_s3_bucket(
        bucket="test_bucket", key="test_json.json")

    return json_file_object_from_s3
