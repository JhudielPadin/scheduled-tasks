import os
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "jhudiel243@gmail.com"
password = "lqmn jdme avzt pbpm"

my_email = os.environ.get("my_email")
password = os.environ.get("password")

now = dt.datetime.now()
today_tuple = (now.month, now.day)
print(today_tuple)

data = pd.read_csv("birthdays.csv")

birthday_dict = {
    (row["month"], row["day"]): row for (index, row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        message = contents.replace("[NAME]", birthday_person["name"].capitalize()).replace("[SENDER]", "Manoy Jhudiel")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= birthday_person["email"],
                            msg=f"Subject:It's {birthday_person["name"].capitalize()}'s Birthday!\n\n{message}")
