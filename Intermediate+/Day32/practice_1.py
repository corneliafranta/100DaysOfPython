import smtplib
my_email = 'frantacorneliat@yahoo.com'
password = 'hjfzfdoralgziqpd'
connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="corneliaDeGossonDeVarennes@gmail.com", msg="Subject:Hallo\n\nThis is the body of my email")
connection.close()