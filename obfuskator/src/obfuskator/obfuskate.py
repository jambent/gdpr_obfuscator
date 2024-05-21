from obfuskator.get_s3_bucket_and_key_names import get_s3_bucket_and_key_names
from obfuskator.get_file_object_from_s3_bucket import get_file_object_from_s3_bucket
from obfuskator.get_filetype import get_filetype
from obfuskator.get_columns_to_be_obfuscated import get_columns_to_be_obfuscated
from obfuskator.obfuscate_csv_file import obfuscate_csv_file


def obfuskate(input_json, output_filepath="/tmp", replacement_string="***"):
    """
    Replaces all values within specified column/s, in file loaded from
    S3 bucket, with single replacement string, and writes resulting file
    in the same file format

    Args:
        input_json: JSON string detailing "file_to_obfuscate" and "pii_fields"
        , e.g.,
        '{
        "file_to_obfuscate": "s3://my_ingestion_bucket/new_data/file1.csv",
        "pii_fields": ["name", "email_address"]
        }'

        output_filepath: filepath where obfuscated file is written to
                        (default = /tmp)

        replacement_string: string to be used to replace all values in the
                            specified PII fields (default = "***")

    """
    s3_bucket_name, s3_key_name = get_s3_bucket_and_key_names(input_json)
    retrieved_file_object = (get_file_object_from_s3_bucket
                             (s3_bucket_name, s3_key_name))
    filetype = get_filetype(s3_key_name)
    columns_to_be_obfuscated = get_columns_to_be_obfuscated(input_json)

    if filetype == "csv":
        (obfuscate_csv_file(retrieved_file_object, columns_to_be_obfuscated,
                            output_filepath, replacement_string))
