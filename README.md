# Twilio SMS Sender (Python)

This project provides a simple and clean Python script for sending SMS messages using the official Twilio Python SDK.  
Environment variables are managed using `python-dotenv`, allowing sensitive credentials to be stored securely in a `.env` file instead of being hard-coded in the script.

## Features

- Sends SMS messages using the Twilio REST API  
- Loads credentials from a `.env` file  
- Input validation for phone numbers and message content  
- Error handling for API and connection issues  
- Clean and well-structured code for easy maintenance and reuse  

## Requirements

- Python 3.8 or higher  
- A Twilio account  
- A verified Twilio phone number  
- The following Python packages:
  - `twilio`
  - `python-dotenv`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yeferson321/twilio-sms-sender.git
cd twilio-sms-sender
```

### 2. Install dependencies 

```bash
pip install twilio python-dotenv
```

### 3. Create a .env file

- Create a file named .env in the root of the project:

```bash
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
```

- The script relies on the following variables loaded from .env:

  | Variable             | Description                         |
  |----------------------|-------------------------------------|
  | TWILIO_ACCOUNT_SID   | Your Twilio account SID             |
  | TWILIO_AUTH_TOKEN    | Your Twilio API authentication token |

## Project Structure

```bash
.
├── main.py       # Main script for sending SMS
├── .env          # Environment variables (ignored by Git)
├── README.md     # Project documentation
```

## Usage

- Run the main script:

```bash
python main.py
```

- You will be prompted to:

   - Enter the destination phone number (E.164 format, e.g., +57XXXXXXXXXX).
   - Enter the message text you want to send.

### Example usage:

```bash
Enter the destination phone number including the country code (e.g., +57XXXXXXXXXX): +573001234567
Enter the message you want to send: Hello, this is a Twilio test!
```

### When successful, you will see:

```bash
Message sent successfully.
Message SID: SMxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Notes

- If you are using a Twilio trial account, the destination phone number must be verified in the Twilio console.

- All messages must be sent from the Twilio phone number assigned to your account.

- Keep your .env file private and never upload it to version control.

## License

- This project is licensed under the MIT License.