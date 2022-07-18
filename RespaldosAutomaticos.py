import paramiko
import os
import subprocess
import paramiko
from datetime import datetime
from datetime import *
from os import mkdir

Yesterday = (date.today() - timedelta(days = 1)).strftime('%Y_%m_%d')

if os.path.exists("D:/"+Yesterday) == False:
        mkdir("D:/"+Yesterday)


host="148.1.1.1"
port = 22
transport = paramiko.Transport((host, port))

password="password"
username="username"
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

source_folder="C:/Users/MyServerUser/Desktop/"+Yesterday+"/"
inbound_files=sftp.listdir(source_folder)


try:
 for file in inbound_files :
        
         filepath = source_folder+file
         localpath = "C:/"+Yesterday+"/"+file
         print(f"copying {file} --> {localpath} ... \n ", end="")
         sftp.get(filepath, localpath)
except:
         print("Fail")
         print("Error, could not copy file {file}")


