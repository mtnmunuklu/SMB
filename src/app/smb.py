from src.config import Config
from smb.SMBConnection import SMBConnection
from smb import smb_structs
import logging
from src.app.logger import Logger

class SMBClient:

    def __init__(self):
        self.username = Config.USERNAME
        self.password = Config.PASSWORD
        self.domain = Config.DOMAIN
        self.source_machine_name = Config.SOURCE_MACHINE_NAME
        self.server_ip = Config.SERVER_IP
        self.destination_machine_name = Config.DESTINATION_MACHINE_NAME
        self.use_ntlm_v2 = Config.USE_NTLM_V2
        self.sign_options = Config.SIGN_OPTIONS
        self.is_direct_tcp = Config.IS_DIRECT_TCP
        self.sock_family = Config.SOCK_FAMILY
        self.timeout = Config.TIMEOUT
        self.port = Config.PORT
        self.share_name = Config.SHARE_NAME
        self.file_paths = Config.FILE_PATHS
        self.file_upload_paths = Config.FILE_UPLOAD_PATHS

        smb_structs.SUPPORT_SMB2 = Config.SUPPORT_SMB2
        self.logger = Logger('SMBClient')


    def create_connection(self):
        """ 
        Connect and authenticate to the SMB share.
        :return: None
        """
        try:

            self.connection = SMBConnection(self.username, self.password, self.source_machine_name, self.destination_machine_name, domain=self.domain,
            use_ntlm_v2=self.use_ntlm_v2, sign_options=self.sign_options, is_direct_tcp=self.is_direct_tcp)

            connection_status = self.connection.connect(self.server_ip, port=int(self.port), sock_family=int(self.sock_family), timeout=int(self.timeout))

            # If connnection is succesfull, upload file
            if connection_status:
                files = self.file_paths.split(',')
                file_uploads = self.file_upload_paths.split(',')
                self.upload(files, file_uploads)
                self.connection.close()

        except Exception as e:
            self.logger.log(logging.WARNING, "Remote share connection error")
            self.logger.log(logging.ERROR, e)

    def upload(self, files: list, file_uploads: list):
        """
        Upload files to the remote share.
        :return: None 
        """
        try:
            for index, file in enumerate(files):
                with open(file, 'rb') as file_obj:
                    self.connection.storeFile(service_name=self.share_name,
                    path=file_uploads[index], file_obj=file_obj)
        except Exception as e:
            self.logger.log(logging.WARNING, "File upload error to remote share")
            self.logger.log(logging.ERROR, e)
