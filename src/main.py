from src.app.smb import SMBClient

if __name__ == "__main__":
    smbconnect = SMBClient()
    smbconnect.create_connection()