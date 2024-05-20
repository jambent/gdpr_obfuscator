import polars as pl


def obfuscate_csv_file(csv_input_filepath,
                       columns_for_obfuscation,
                       output_filepath="/tmp",
                       replacement_string="***"):
    """
    For a single CSV file, replaces all values in specified columns
    with a single replacement string value

    Args:
        csv_input_filepath: target CSV filepath
        columns_for_obfuscation: list of target columns
        output_filepath: location where obfuscated CSV file
                                should be written to (defaults to "/tmp")
        replacement_string: string to be used to replace
                              target column values (defaults to "***")

    Returns:
        CSV file, with all values in the target columns replaced
        by the value of replacement_string
    """
    csv_obfuscation_operation = (
        pl.scan_csv(csv_input_filepath)
        .with_columns(pl.col(columns_for_obfuscation)
                      .str.replace_all(r"(?s).*", replacement_string))
    )

    obfuscated_csv_df = csv_obfuscation_operation.collect()

    obfuscated_csv_df.write_csv(output_filepath)
