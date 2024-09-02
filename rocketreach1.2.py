import rocketreach
import csv
from dotenv import load_dotenv
import os


def display_person(person):
    print("Available attributes for Person object:")
    for attr, value in person.__dict__.items():
        print(f"{attr}: {value}")

def write_person_to_csv(person, csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Attribute', 'Value'])
        for attr, value in person.__dict__.items():
            writer.writerow([attr, value])

def search_person_and_process(api_key, email_address, csv_file):
    rr = rocketreach.Gateway(api_key=api_key)
    search_result = rr.person.search().filter(email=email_address).execute()

    if search_result.is_success and search_result.people:
        person = search_result.people[0]
        display_person(person)
        write_person_to_csv(person, csv_file)
    else:
        print(f"No person found with the email address: {email_address}")

if __name__ == "__main__":
    # api_key = '1384ae4k98f71eed1e812404414afea07712db53'
    load_dotenv()

    API_KEY = os.getenv('ROCKETREACH_API_KEY')
    csv_file = 'data/person_info.csv'
    email_address = input("Enter the email address to search for: ")

    search_person_and_process(API_KEY, email_address, csv_file)
