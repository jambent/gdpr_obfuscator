import polars as pl

example_dataframe = pl.DataFrame({
    "student_id": [1234, 2785, 4891, 5593],
    "name": ["John Smith", "Debbie McKay", "John Lee", "Barry Hercules"],
    "course": ["Software", "Data", "Software", "Cloud"],
    "cohort": ["Aug23", "Aug23", "May23", "Feb23"],
    "graduation_date": ["2023-11-17", "2023-11-17",
                        "2023-08-20", "2023-05-14"],
    "email_address": ["jsmith@email.com", "debbiemk88@bkinternet.com",
                      "jwlee@lemail.com", "bbh1959@daimail.jp"]
}
)
