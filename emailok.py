import smtplib
email = input("SENDER EMAIL: ")
# app_password=input("ENTER YOUR PASS: ")
recever_email= input("RECIVER EMAIL: ")
subject = input("SUBJECT: ")
message=input("Message: ")
text = f"Subject: {subject}\\n\n{message}"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email, "ekjz vskr ndkv eqne")
server.sendmail(email,recever_email,text)
print("Email has been sent to " + recever_email)
