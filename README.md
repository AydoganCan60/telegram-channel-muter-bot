# Telegram Channel Notification Muter Bot

This Python script automatically **mutes notifications for all channels** in your Telegram account. It is built using the powerful `Telethon` library.

🚀 Features

- Automatically mute notifications for all joined Telegram channels and supergroups.
- Fast, efficient, and easy to use.
- Fully open-source and customizable to fit your needs.

Purpose: This code is designed to automatically mute notifications for all Telegram channels and supergroups, so you don't have to disable them one by one if you are in too many channels. It saves time and effort, especially for users overwhelmed by constant notifications.

🛠 Requirements

- Python 3.8 or higher
- Telethon library

📦 Installation

First, clone the repository or download the script.

To install the required dependencies, run:
```bash
pip install telethon
```
🔑 Setup

Before running the script, you need to provide:
```
- api_id
- api_hash
- phone_number
```
You can obtain your api_id and api_hash from https://my.telegram.org under the API Development Tools section.

⚠️ Important: Make sure you keep your api_id and api_hash safe and do not share them publicly.

⚙️ Usage

Run the script using:
```bash
python main.py
```
- On the first run, a verification code will be sent to your Telegram account to confirm your login.
- After login, the script will automatically mute notifications for all channels and supergroups you are a member of.
- Channels or groups you don't have access to (forbidden) will be skipped automatically.

📂 Project Structure

telegram-channel-muter-bot/
│
├── main.py                # Main Python script
├── requirements.txt       # List of required Python packages
├── README.md              # Project documentation
└── LICENSE                # License file (MIT)

📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

💬 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a pull request or submit an issue to help improve the project.
