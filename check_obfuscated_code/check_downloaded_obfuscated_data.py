from decouple import config
import pandas as pd
from io import BytesIO

from obfsc8.src.obfsc8.get_file_object_from_s3_bucket import \
    get_file_object_from_s3_bucket
from obfsc8.src.obfsc8.get_filetype import get_filetype


if __name__ == "__main__":

    obfuscated_data_bucket = config("DESTINATION_S3_BUCKET")
    # file_to_download = "obfs_one_mb_faked_data.csv"
    file_to_download = "obfs_one_mb_faked_data.parquet"
    # file_to_download = "obfs_one_mb_faked_records_oriented_json.json"
    filetype = get_filetype(file_to_download)

    retrieved_file_object = (get_file_object_from_s3_bucket(
        obfuscated_data_bucket, file_to_download
    ))

    if filetype == "csv":
        df = pd.read_csv(retrieved_file_object)
        print(f"{file_to_download}\n")
        print(df.head(15))

    elif filetype == "parquet":
        df = pd.read_parquet(BytesIO(retrieved_file_object.read()))
        print(f"{file_to_download}\n")
        print(df.head(15))

    elif filetype == "json":
        df = pd.read_json(retrieved_file_object)
        print(f"{file_to_download}\n")
        print(df.head(15))
