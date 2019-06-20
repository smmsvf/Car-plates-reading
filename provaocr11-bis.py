from PIL import Image

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys
import time
import datetime
import pydrive

import numpy as np
import pytesseract
import gphoto2
import os
import csv
import imutils
import cv2

data='lista.csv'
g_login = GoogleAuth()
g_login.LoadCredentialsFile("mycreds.txt")
if g_login.credentials is None:
    # Authenticate if they're not there
    g_login.LocalWebserverAuth()
elif g_login.access_token_expired:
    # Refresh them if expired
    g_login.Refresh()
else:
    # Initialize the saved creds
    g_login.Authorize()
# Save the current credentials to a file
g_login.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(g_login)
file_drive = drive.CreateFile({'title': data})  
file_drive.SetContentFile(data)
file_drive.Upload()
print("L'arxiu ha pujat al drive")
sys.exit()
