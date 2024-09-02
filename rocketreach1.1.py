import rocketreach
import csv
from dotenv import load_dotenv
import os


if __name__ == "__main__":

    
    load_dotenv()

    API_KEY = os.getenv('ROCKETREACH_API_KEY')
    rr = rocketreach.Gateway(api_key=API_KEY)
    csv_file = 'data/person_info.csv'


    email_address = input("Enter the email address to search for: ")
    # emma.hardie@me.com


    search_result = rr.person.search().filter(email=email_address).execute()




    # Check if the search result is successful
    if search_result.is_success and search_result.people:
        # Print information about the first person found (assuming there's at least one result)
        person = search_result.people[0]
        
        
        print("Available attributes for Person object:")
        for attr, value in person.__dict__.items():
            print(f"{attr}: {value}")


        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            
            for attr, value in person.__dict__.items():
                writer.writerow([attr, value])
            
    else:
        print(f"No person found with the email address: {email_address}")



