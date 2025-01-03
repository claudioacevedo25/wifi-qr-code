# WiFi QR Code Generator

This project generates a QR code to connect to a WiFi network. The network data (SSID, authentication type, and password) are securely stored in a `.env` file to avoid exposing sensitive information in the repository.

## Requirements

Before running the script, make sure you have the following installed:

- **Python 3.6 or higher**
- The following Python libraries:
  - `qrcode`
  - `Pillow` (required by `qrcode` to handle images)
  - `python-dotenv`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies
3. Create `.env` file with

- WIFI_S=YourNetworkName
- WIFI_T=WPA2
- WIFI_P=YourNetworkPassword

## Usage

Run `python3 qr-wifi.py`
