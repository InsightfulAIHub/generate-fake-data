from faker import Faker
import csv

faker = Faker()

rows = ['name', 'age', 'job', 'skills', 'years of experience', 'salary', 'company', 'email', 'phone number', 'country']
store = []

def generate_data(file, row):
    with open(f'data/{file}.csv', "w", newline='') as csvfile:
        data = csv.DictWriter(csvfile, fieldnames=rows)
        data.writeheader()
        
        for _ in range(int(row)):
            list_dict = {}
            list_dict['name'] = faker.name()
            list_dict['age'] = faker.random_int(min=18, max=65)
            list_dict['job'] = faker.job()
            list_dict['skills'] = ', '.join(faker.words(nb=3))
            list_dict['years of experience'] = faker.random_int(min=1, max=20)
            list_dict['salary'] = faker.random_int(min=3000, max=100000)
            list_dict['company'] = faker.company()
            list_dict['email'] = faker.email()
            list_dict['phone number'] = faker.phone_number()
            list_dict['country'] = faker.country()

            store.append(list_dict)
        
        data.writerows(store)

file = input('Enter file name: ')
row = input('Enter number of rows: ')

generate_data(file, row)
