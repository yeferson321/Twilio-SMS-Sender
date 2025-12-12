# SEND SMS WITH Twilio library

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from the .env file
load_dotenv()

# Retrieve credentials from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def send_message(destination_number: str, message_text: str):
    try:
        message = client.messages.create(
            body=message_text,
            from_='+15737495150', # Your Twilio phone number
            to=destination_number
        )

        print("Mensaje enviado correctamente", message.body)

    except Exception as e: print("Error sending message:", str(e))

if __name__ == "__main__":
    print("=== Twilio SMS Sender ===")

    # Request destination number
    destination_number = input("Enter the destination phone number including the country code (e.g., +57XXXXXXXXXX): ").strip()

    if not destination_number.startswith("+"):
        print("Invalid format. The phone number must start with '+'.")
        exit(1)
        
    # Request message text
    message_text = input("Enter the message you want to send: ").strip()

    send_message(destination_number, message_text)
