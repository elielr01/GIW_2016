import smtplib

#Capturar servidor

#Capturar remitente
#Capturar destinatario
#Capturar mensaje

msg = "\r\n".join([
  "From: eli.emmanuel01@gmail.com",
  "To: eli.emmanuel01@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

server.login("eli.emmanuel01@gmail.com", "eli_010295")

server.sendmail("eli.emmanuel01@gmail.com", "eli.emmanuel01@gmail.com", msg)

server.quit()
