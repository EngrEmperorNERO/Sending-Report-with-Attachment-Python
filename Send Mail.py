#BP_Consignment_Order_Report_email.py

import os
import fnmatch
import shutil
from datetime import date, timedelta
import pandas as pd
import numpy as np
import time
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
#put your email here
sender = 'your email'

CleanPath = r"C:\Users\Zemo\Documents\Python Tutorial\Scrape File\Raw Data\world_population_modified.csv"
# Get today's date, at this point the file downloaded 'today' which has yesterday's sales will have yesterday's date in the file name
today = date.today()
yesterday = today - timedelta(days=1)
today_string = str(today)
yesterday_string = str(yesterday)
year = today_string[0:4]
month = today_string[5:7]
day_yesterday = today_string[8:10]


#put receiver email here
receivers = ''
msg = MIMEMultipart()
body_Of_Email = """Hi,
This is the world population report sample.

Best,
Marvin"""

text = """\
Hi,

This is the world population report sample.

Best,
Marvin"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
# Add HTML/plain-text parts to MIMEMultipart message
msg.attach(part1)

msg['Subject'] = 'Population Report'
msg['From'] = sender
msg['To'] = receivers

filename1 = r"C:\Users\Zemo\Documents\Python Tutorial\Scrape File\Raw Data\world_population_modified.csv"

attachment1 = open(r"C:\Users\Zemo\Documents\Python Tutorial\Scrape File\Raw Data\world_population_modified.csv", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment1).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename1)

msg.attach(part)

s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)


#Go to google account settings, Go to App Password, Create App Name, Copy the alphanumeric code.
#refer to this tutorial -- https://itsupport.umd.edu/itsupport?id=kb_article_view&sysparm_article=KB0015112
s.login(user=sender, password='')
s.sendmail(sender, receivers, msg.as_string())
s.quit()
time.sleep(20)