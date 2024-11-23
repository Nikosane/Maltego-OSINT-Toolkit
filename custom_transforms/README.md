# VirusTotal Domain Transform

`transform2.py` is a Maltego custom transform that integrates with the VirusTotal API to gather domain-related intelligence. This transform fetches details such as categories and popularity rankings of a domain.

## Features
- Queries VirusTotal for domain information.
- Displays detected categories and descriptions.
- Fetches popularity ranks from multiple sources (e.g., Alexa, Cisco Umbrella).

## Setup Instructions
1. **Install Dependencies**:
   Ensure you have Python and the required libraries installed:
   ```bash
   pip install requests maltego-trx

