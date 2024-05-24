import pytest
from moto import mock_aws
import boto3

from obfsc8.src.obfsc8.get_file_object_from_s3_bucket \
    import get_file_object_from_s3_bucket
from test_data.test_dataframe import test_dataframe


@pytest.fixture()
@mock_aws
def csv_from_s3():
    s3 = boto3.client('s3', region_name="eu-west-2")
    s3.create_bucket(Bucket="test_bucket",
                     CreateBucketConfiguration={
                            'LocationConstraint': "eu-west-2"
                     }
                     )

    test_csv = test_dataframe.write_csv()
    s3.put_object(Bucket="test_bucket", Key="test_csv.csv", Body=test_csv)

    csv_file_object_from_s3 = get_file_object_from_s3_bucket(
        bucket="test_bucket", key="test_csv.csv")

    return csv_file_object_from_s3
