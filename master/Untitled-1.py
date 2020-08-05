from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
daterey = (dt_string.replace("/","")).replace(":", "")
namer = 'DBFAinvoice '+ daterey+'.pdf'


custt = "balaji.pranav@outlook.in"
print("Please wait..")
fromaddr = "billing.dbfa@gmail.com"
toaddr = custt
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Your DBFA Purchase Invoice"
body = """Thanks for making your purchase at DBFA!

Please find your invoice attached herewith.

Regards,
The DBFA Team"""
msg.attach(MIMEText(body, 'plain')) 
filename = namer
attachment = open(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\'+'%s'%namer, "rb") 
attac= MIMEBase('application', 'octet-stream') 
attac.set_payload((attachment).read()) 
encoders.encode_base64(attac) 
attac.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(attac) 
email = smtplib.SMTP('smtp.gmail.com', 587)  
email.starttls() 
email.login(fromaddr, "dbfaidlepass") 
message = msg.as_string() 
email.sendmail(fromaddr, toaddr, message) 
print("Invoice mailed. ")