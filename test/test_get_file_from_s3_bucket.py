import boto3
from moto import mock_aws
import polars as pl
from polars.testing import assert_frame_equal


from src.get_file_from_s3_bucket import get_file_from_s3_bucket


test_df = pl.DataFrame(
    {
        "student_id": [1234, 2785, 4891, 5593],
        "name": ["John Smith", "Debbie McKay", "John Lee", "Barry Hercules"],
        "course": ["Software", "Data", "Software", "Cloud"],
        "cohort": ["Aug23", "Aug23", "May23", "Feb23"],
        "graduation_date": ["2023-11-17", "2023-11-17",
                            "2023-08-20", "2023-05-14"],
        "email_address": ["jsmith@email.com", "debbiemk88@bkinternet.com",
                          "jwlee@lemail.com", ""]
    }
)


@mock_aws
def test_that_csv_file_put_in_s3_can_be_retrieved_without_change():
    s3 = boto3.client('s3', region_name="eu-west-2")
    s3.create_bucket(Bucket="test_bucket",
                     CreateBucketConfiguration={
                            'LocationConstraint': "eu-west-2"
                     }
                     )

    test_csv = test_df.write_csv()

    s3.put_object(Bucket="test_bucket", Key="test_csv.csv", Body=test_csv)

    csv_file_from_s3 = get_file_from_s3_bucket(bucket="test_bucket",
                                               key="test_csv.csv")
    csv_file_from_s3_as_df = pl.read_csv(csv_file_from_s3["Body"])

    assert_frame_equal(test_df, csv_file_from_s3_as_df)
