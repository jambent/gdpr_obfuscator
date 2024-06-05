import random
import datetime
import pandas as pd
from faker import Faker

fake = Faker("en_UK")

data = pd.DataFrame(
    index=range(
        0,
        10000),
    columns=[
        "student_id",
        "name",
        "course",
        "cohort",
        "graduation_date",
        "email_address"])
course_choices = ["Software", "Data", "Cloud"]
for i in range(0, 10000):
    data.loc[i, "student_id"] = random.randint(1, 10000)
    data.loc[i, "name"] = fake.name()
    data.loc[i, "course"] = random.choice(course_choices)
    data.loc[i, "cohort"] = random.randint(2018, 2045)
    data.loc[i, "graduation_date"] = fake.date_between(
        datetime.date(2018, 6, 1), datetime.date(2045, 6, 1))
    data.loc[i, "email_address"] = fake.email()

(data.to_json(
    "./utility_generated_data/one_mb_faked_index_oriented_json.json",
    orient="index"))
(data.to_json(
    "./utility_generated_data/one_mb_faked_columns_oriented_json.json",
    orient="columns"))
(data.to_json(
    "./utility_generated_data/one_mb_faked_records_oriented_json.json",
    index=False, orient="records"))
(data.to_json(
    "./utility_generated_data/one_mb_faked_table_oriented_json.json",
    index=False, orient="table"))


data = pd.DataFrame(
    index=range(
        0,
        13800),
    columns=[
        "student_id",
        "name",
        "course",
        "cohort",
        "graduation_date",
        "email_address"])
course_choices = ["Software", "Data", "Cloud"]
for i in range(0, 13800):
    data.loc[i, "student_id"] = random.randint(1, 13800)
    data.loc[i, "name"] = fake.name()
    data.loc[i, "course"] = random.choice(course_choices)
    data.loc[i, "cohort"] = random.randint(2018, 2045)
    data.loc[i, "graduation_date"] = fake.date_between(
        datetime.date(2018, 6, 1), datetime.date(2045, 6, 1))
    data.loc[i, "email_address"] = fake.email()


(data.to_json(
    "./utility_generated_data/one_mb_faked_split_oriented_json.json",
    index=False, orient="split"))
(data.to_json(
    "./utility_generated_data/one_mb_faked_values_oriented_json.json",
    index=False, orient="values"))
