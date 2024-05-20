import os
import polars as pl
import polars.testing as pt

from src.obfuscate_csv_file import obfuscate_csv_file
from test_data.test_dataframe import test_dataframe


def test_that_csv_file_returned_is_not_equivalent_to_the_file_input():

    test_dataframe.write_csv("./test/test_data/test_csv.csv")
    columns_for_obfuscation = ["name", "email_address"]

    obfuscate_csv_file(
        "./test/test_data/test_csv.csv",
        columns_for_obfuscation,
        "./test/test_data/obfuscated_test_csv.csv")
    obfuscated_dataframe = (pl.read_csv
                            ("./test/test_data/obfuscated_test_csv.csv"))

    pt.assert_frame_not_equal(test_dataframe, obfuscated_dataframe)

    # Remove obfuscated CSV output file following completion of test
    if os.path.isfile("./test/test_data/test_csv.csv"):
        os.remove("./test/test_data/test_csv.csv")
    if os.path.isfile("./test/test_data/obfuscated_test_csv.csv"):
        os.remove("./test/test_data/obfuscated_test_csv.csv")


def test_that_all_values_in_non_target_columns_remain_unchanged():

    test_dataframe.write_csv("./test/test_data/test_csv.csv")
    columns_for_obfuscation = ["name", "email_address"]

    obfuscate_csv_file(
        "./test/test_data/test_csv.csv",
        columns_for_obfuscation,
        "./test/test_data/obfuscated_test_csv.csv")
    obfuscated_dataframe = (pl.read_csv
                            ("./test/test_data/obfuscated_test_csv.csv"))

    for column_name in obfuscated_dataframe.columns:
        if column_name not in columns_for_obfuscation:
            original_column_values = test_dataframe.get_column(column_name)
            obfuscated_column_values = (obfuscated_dataframe
                                        .get_column(column_name))

            (pt.assert_series_equal(original_column_values,
                                    obfuscated_column_values))

    # Remove obfuscated CSV output file following completion of test
    if os.path.isfile("./test/test_data/test_csv.csv"):
        os.remove("./test/test_data/test_csv.csv")
    if os.path.isfile("./test/test_data/obfuscated_test_csv.csv"):
        os.remove("./test/test_data/obfuscated_test_csv.csv")


def test_that_all_values_in_target_columns_made_equal_to_replacement_string():

    test_dataframe.write_csv("./test/test_data/test_csv.csv")
    columns_for_obfuscation = ["name", "email_address"]

    obfuscate_csv_file(
        "./test/test_data/test_csv.csv",
        columns_for_obfuscation,
        "./test/test_data/obfuscated_test_csv.csv")
    obfuscated_dataframe = (pl.read_csv
                            ("./test/test_data/obfuscated_test_csv.csv"))

    obfuscated_column_values_list = []
    for column_name in columns_for_obfuscation:
        obfuscated_column_values = (obfuscated_dataframe
                                    .get_column(column_name))
        obfuscated_column_values_list.append(obfuscated_column_values)

    for i in range(1, len(obfuscated_column_values_list)):
        (pt.assert_series_equal(obfuscated_column_values_list[0],
                                obfuscated_column_values_list[i],
                                check_names=False))

    # Remove obfuscated CSV output file following completion of test
    if os.path.isfile("./test/test_data/test_csv.csv"):
        os.remove("./test/test_data/test_csv.csv")
    if os.path.isfile("./test/test_data/obfuscated_test_csv.csv"):
        os.remove("./test/test_data/obfuscated_test_csv.csv")
