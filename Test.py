from email.message import EmailMessage
import ssl
import smtplib
email_sender = 'secure2faotpbot@gmail.com'
email_pass='uksm hvgd ojzp juov'
email_receiver='spandanspatel14122006@gmail.com'

Subject= "TESTING"
body = "TESTING for project"

em= EmailMessage()
em['From']=email_sender
em['To']=email_receiver 
em['Subject']=Subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_pass)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
