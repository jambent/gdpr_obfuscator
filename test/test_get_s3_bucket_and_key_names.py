from src.get_s3_bucket_and_key_names import get_s3_bucket_and_key_names

test_json = """{
    "file_to_obfuscate": "s3://my_ingestion_bucket/new_data/file1.csv",
    "pii_fields": ["name", "email_address"]
    }"""


def test_that_2_strings_returned():
    s3_bucket, s3_key = get_s3_bucket_and_key_names(test_json)

    assert isinstance(s3_bucket, str)
    assert isinstance(s3_key, str)


def test_that_s3_key_contains_period_but_s3_bucket_does_not():
    s3_bucket, s3_key = get_s3_bucket_and_key_names(test_json)

    assert '.' not in s3_bucket
    assert '.' in s3_key


def test_that_s3_key_and_bucket_names_match_those_in_json():
    s3_bucket, s3_key = get_s3_bucket_and_key_names(test_json)

    assert s3_bucket == "my_ingestion_bucket"
    assert s3_key == "new_data/file1.csv"
