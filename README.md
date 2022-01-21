# python-imessages

## Usage

1. Create a Google Sheet
   - Note the id of the spreadsheet (between `/d/` and `/edit...`) and the name of the sheet.
     - Add these to the configuration files.
     - (That is, `config.toml`)
   - Set the spreadsheet to be shared with anyone with a link.

2. Clone the repository
   - Use git on cli/gui or just Code > Download

3. Write Python Script
   - Edit the python script to get the desired effect.
   - This is marked with a comment in `imessages.py`

4. Run the script
```bash
# one time setup
pip3 install -r requirements.txt

python3 imessages.py
```

5. Accept permissions on first runtime.

For SMS capablites, [follow this guide](https://support.apple.com/guide/messages/get-sms-texts-from-iphone-on-your-mac-icht8a28bb9a/mac).
