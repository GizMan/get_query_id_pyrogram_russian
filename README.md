# get_query_id_pyrogram

A Python script using Pyrogram to manage sessions and retrieve query IDs through Telegram bot webviews. This script requires configuring API credentials for Telegram.

## Requirements

- Python 3.7+
- [Pyrogram](https://docs.pyrogram.org/) library
- A valid `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org/)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ululazmi18/get_query_id_pyrogram.git
   cd get_query_id_pyrogram
   ```

2. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Credentials**
   - In the root folder of the project, you will find a `config.json` file created by the script. Open this file and fill in your `api_id` and `api_hash`.
   - Example:
     ```json
     {
       "api_id": 1234567,
       "api_hash": "your_api_hash_here"
     }
     ```

4. **Run the Script**
   - Start the program by running:
     ```bash
     python main.py
     ```
   - Follow the on-screen prompts:
     - **Option 1:** Create a new session by entering your phone number.
     - **Option 2:** Request query IDs from all available sessions.
     - **Option 3:** Exit the program.

## Usage

1. **Creating a New Session**
   - When prompted, choose `1` to create a new session.
   - Enter your Telegram phone number to initialize and store the session in the `sessions` directory.

2. **Retrieving Query IDs**
   - Choose `2` to retrieve query IDs for the configured bot.
   - Follow the prompts to select or add a bot with its referral URL.
   - The script will create two output files, `user.txt` and `query_id.txt`, storing the retrieved user and query IDs.

## Notes

- Ensure that the `sessions` folder exists in the root directory.
- Edit the `bot.json` file to manage multiple bot usernames and their referral URLs.

