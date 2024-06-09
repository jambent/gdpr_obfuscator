from decouple import config
import json
import pandas as pd
from io import BytesIO

from obfsc8.src.obfsc8.get_file_object_from_s3_bucket import \
    get_file_object_from_s3_bucket
from obfsc8.src.obfsc8.get_filetype import get_filetype


if __name__ == "__main__":

    obfuscated_data_bucket = config("DESTINATION_S3_BUCKET")
    file_to_download = "obfs_one_mb_faked_data.csv"
    # file_to_download = "./obfuscated_records_json.json"
    filetype = get_filetype(file_to_download)

    if filetype != 'json':
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
        with open(file_to_download) as fh:
            data = pd.DataFrame(json.load(fh))
            dataframe_width = len(data["columns"])

            columns_as_series = []
            for i in range(dataframe_width):
                columns_as_series.append(pd.Series(data["columns"][i]))
            df = pd.concat(columns_as_series, axis=1)

            explosion_index_list = []
            for i in range(dataframe_width):
                explosion_index_list.append(i)
            df = df.explode(explosion_index_list)

            df.columns = df.iloc[0]
            df.drop(["datatype", "bit_settings"], inplace=True)
            df.drop(df.index[0], inplace=True)
            df.reset_index(drop=True, inplace=True)

            print(f"{file_to_download}\n")
            print(df.head(15))
