import os
from dotenv import load_dotenv

load_dotenv()

META_VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
META_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PHONE_NUMBER_ID = os.getenv('PHONE_NUMBER_ID')
