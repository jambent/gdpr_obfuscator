import random
import datetime
import pandas as pd
from faker import Faker

fake = Faker("en_UK")

data = pd.DataFrame(
    index=range(
        0,
        16000),
    columns=[
        "student_id",
        "name",
        "course",
        "cohort",
        "graduation_date",
        "email_address"])
course_choices = ["Software", "Data", "Cloud"]
for i in range(0, 16000):
    data.loc[i, "student_id"] = random.randint(1, 16000)
    data.loc[i, "name"] = fake.name()
    data.loc[i, "course"] = random.choice(course_choices)
    data.loc[i, "cohort"] = random.randint(2018, 2045)
    data.loc[i, "graduation_date"] = fake.date_between(
        datetime.date(2018, 6, 1), datetime.date(2045, 6, 1))
    data.loc[i, "email_address"] = fake.email()

data.to_csv("./utilities/faker.csv", index=False)
