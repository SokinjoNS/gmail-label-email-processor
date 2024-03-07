# Gmail Label Email Processor

The Gmail Label Email Processor is a Python toolkit designed to automate the process of managing and processing emails through the Gmail API. This tool facilitates the fetching of emails based on specific labels, extraction of email addresses from these emails, and exporting the processed data into a CSV file for further analysis or use. Ideal for individuals and businesses looking to enhance their email management and data extraction workflows.

## Features

- Authenticate with the Gmail API securely.
- Fetch emails by user-defined labels.
- Extract 'To', 'Cc', and 'Bcc' email addresses from emails.
- Export extracted email addresses to a CSV file.
- Simplify the automation of email processing tasks.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- Access to a Google Cloud Platform account with the Gmail API enabled.
- A `credentials.json` file obtained from the Google Developer Console for your Gmail API project.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/gmail-label-email-processor.git
cd gmail-label-email-processor
```

Install the required dependencies:
```
bash
Copy code
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Usage

To use the Gmail Label Email Processor, follow these steps:

Place your credentials.json file in the root directory of the project.
Modify the main.py script to specify the label you want to process.
Run the script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
