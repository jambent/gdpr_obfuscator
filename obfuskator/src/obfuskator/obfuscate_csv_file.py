import polars as pl


def obfuscate_csv_file(csv_file_object,
                       columns_for_obfuscation,
                       output_filepath,
                       replacement_string):
    """
    For a single CSV file object input, replaces all values in
    specified columns with a single replacement string value

    Args:
        csv_file_object: target CSV file object
        columns_for_obfuscation: list of target columns
        output_filepath: location where obfuscated CSV file
                                should be written to
        replacement_string: string to be used to replace
                              target column values
    """

    csv_obfuscation_operation = (
        pl.read_csv(csv_file_object).lazy()
        .with_columns(pl.col(columns_for_obfuscation)
                      .str.replace_all(r"(?s).*", replacement_string))
    )
    obfuscated_csv_df = csv_obfuscation_operation.collect()

    obfuscated_csv_df.write_csv(output_filepath)
