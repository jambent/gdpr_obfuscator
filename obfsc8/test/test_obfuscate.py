import pytest

from obfsc8.src.obfsc8.obfuscate import obfuscate
from obfsc8.src.obfsc8.obfuscate_csv_file \
    import obfuscate_csv_file


test_json = """{
    "file_to_obfuscate": "s3://test_bucket/test_csv.csv",
    "pii_fields": ["name", "email_address"]
    }"""

test_json_json = """{
    "file_to_obfuscate": "s3://test_bucket/test_csv.json",
    "pii_fields": ["name", "email_address"]
    }"""

columns_for_obfuscation = ["name", "email_address"]
replacement_string = "***"


@pytest.mark.skip
# @mock_aws
def test_that_BytesIO_object_returned(csv_from_s3):
    obfuscation_result = (
        obfuscate_csv_file(
            csv_from_s3,
            columns_for_obfuscation,
            replacement_string))
    test_result = obfuscate(test_json)
    print(obfuscation_result)

    assert test_result == obfuscation_result


@pytest.mark.skip
# @patch(get_s3_bucket_and_key_names,return_values="test_bucket,test_csv.csv")
def test_failure_for_more_than_2_arguments(
        get_s3_bucket_and_key_names, csv_from_s3):
    s3_bucket, s3_key = get_s3_bucket_and_key_names(test_json)
    assert s3_bucket == 'test_bucket'
