from dotenv import load_dotenv
import os
from src.validators.rule3 import Rule3Validator

load_dotenv()

validator = Rule3Validator(gemini_api_key=os.getenv("GEMINI_API_KEY"))

assert validator.validate("Disengage the lock and lift the handle carefully.") == False

assert validator.validate("Set the switch and release the button.")  == True