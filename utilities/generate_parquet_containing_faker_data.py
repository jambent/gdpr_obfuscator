import random
import datetime
import pandas as pd
from faker import Faker

fake = Faker("en_UK")

data = pd.DataFrame(
    index=range(
        0,
        32000),
    columns=[
        "student_id",
        "name",
        "course",
        "cohort",
        "graduation_date",
        "email_address"])
data = data.astype(dtype={'student_id': str,
                          'name': str,
                          'course': str,
                          'cohort': str,
                          'graduation_date': str,
                          'email_address': str})

data['graduation_date'] = pd.to_datetime(data['graduation_date'])


course_choices = ["Software", "Data", "Cloud"]
for i in range(0, 32000):
    data.loc[i, "student_id"] = random.randint(1, 32000)
    data.loc[i, "name"] = fake.name()
    data.loc[i, "course"] = random.choice(course_choices)
    data.loc[i, "cohort"] = random.randint(2018, 2045)
    data.loc[i, "graduation_date"] = (pd.to_datetime(
        fake.date_between(datetime.date(2018, 6, 1),
                          datetime.date(2045, 6, 1))))
    data.loc[i, "email_address"] = fake.email()

data.to_parquet("./utilities/faker.parquet", index=False, engine="fastparquet")


df = pd.read_parquet("./utilities/faker.parquet")
