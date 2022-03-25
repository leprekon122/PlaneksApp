import pandas as pd
import random


def make_files(req):
    column = ['name', 'job', 'email', 'domain_name', 'phone_number', 'text', 'address', 'date']
    name = ['Nick', 'Vova', 'Igor', 'Gosha', 'Alex', 'Stan', 'Bradley']
    job = ['Apple inc', 'Google inc', 'BMW', 'Toyota', 'Mazda', 'Samsung']
    email = ['1234@hmail.com', '34@hmail.com', '14@hmail.com', '23141234@hmail.com']
    domain = ['google.com', 'jobs.it', 'news.com', 'trade.pl']
    phone = ['235235325', '4213412352153', '1234124124', '3512352315']
    text = [
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid at blanditiis consectetur eius, iste libero mollitia nihil perspiciatis rem saepe similique ut vero voluptatem? Illo itaque neque odio repellendus sint?']
    address = ['Kiev, Ukraine', 'kharkiv, Ukraine', 'Palo-Alto, USA']
    dates = ['2021-04-05', '2022-01-12', '2020-12-31']
    data = []
    for el in range(int(req)):
        data.append([random.choice(name), random.choice(job), random.choice(email), random.choice(domain),
                     random.choice(phone), random.choice(text), random.choice(address), random.choice(dates)])
    create = pd.DataFrame(data, columns=column)
    create.to_csv(r"/Users/priest/PycharmProjects/PLANEKS/planeks_app/csv_files/my_file.csv")
