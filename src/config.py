import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

# load enviorment variables
env_path = '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """
    Set CIS configuration vars from .env file
    """

    # Load in environment variables
    # These fields are associated with logger
    LOG_FILE = os.getenv('LOG_FILE')
    LOG_FORMAT = os.getenv('LOG_FORMAT')
    # These fields are associated with smb connection
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    DOMAIN = os.getenv('DOMAIN')
    SOURCE_MACHINE_NAME = os.getenv('SOURCE_MACHINE_NAME')
    SERVER_IP = os.getenv('SERVER_IP')
    DESTINATION_MACHINE_NAME = os.getenv('DESTINATION_MACHINE_NAME')
    USE_NTLM_V2 = os.getenv('USE_NTLM_V2')
    # SIGN_NEVER (value=0),  SIGN_WHEN_SUPPORTED (value=1), SIGN_WHEN_REQUIRED (value=2)
    SIGN_OPTIONS = os.getenv('SIGN_OPTIONS')
    IS_DIRECT_TCP = os.getenv('IS_DIRECT_TCP')
    SUPPORT_SMB2 = os.getenv('SUPPORT_SMB2')
    SOCK_FAMILY = os.getenv('SOCK_FAMILY')
    TIMEOUT = os.getenv('TIMEOUT')
    PORT = os.getenv('PORT')
    SHARE_NAME = os.getenv('SHARE_NAME')
    # Multiple files can be exported using virgul.
    FILE_PATHS = os.getenv('FILE_PATHS')
    FILE_UPLOAD_PATHS = os.getenv('FILE_UPLOAD_PATHS')