import rocketreach
import csv
from dotenv import load_dotenv
import os

class TerminalDisplay:
    @staticmethod
    def display_person(person):
        print("Available attributes for Person object:")
        for attr, value in person.__dict__.items():
            print(f"{attr}: {value}")

class CSVWriter:
    @staticmethod
    def write_person_to_csv(person, csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Attribute', 'Value'])
            for attr, value in person.__dict__.items():
                writer.writerow([attr, value])

class RocketReachSearch:
    def __init__(self, api_key):
        self.rr = rocketreach.Gateway(api_key=api_key)
    
    def search_person_by_email(self, email_address):
        search_result = self.rr.person.search().filter(email=email_address).execute()
        return search_result

if __name__ == "__main__":
    load_dotenv()

    API_KEY = os.getenv('ROCKETREACH_API_KEY')
    csv_file = 'data/person_info.csv'

    email_address = input("Enter the email address to search for: ")

    rocket_reach = RocketReachSearch(API_KEY)
    search_result = rocket_reach.search_person_by_email(email_address)

    if search_result.is_success and search_result.people:
        person = search_result.people[0]

        
        TerminalDisplay.display_person(person)

        
        CSVWriter.write_person_to_csv(person, csv_file)
    else:
        print(f"No person found with the email address: {email_address}")
