
import asyncio
from truecallerpy import search_phonenumber
import json
from dotenv import load_dotenv
import os

async def main():
    load_dotenv()

    INSTALLATION_ID = os.getenv('TRUECALLERPY_INSTALLATION_ID')
    phone_number = input("Please enter the mobile number in International format (+91919234567890): ")
    country_code = input("Enter the country code (US): ")
    

    response = await search_phonenumber(phone_number, country_code, INSTALLATION_ID)
    
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
