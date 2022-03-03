import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs
from account import Account

class Send_Email():

    def send_email(self, ):

        account_info = Account()
        account = account_info.info_Account()


        # your email
        email = account[0]
        # your password
        password = account[1]
        # the sender's email
        FROM = account[0]
        # the receiver's email
        TO   = account[3] 
        # the subject of the email (subject)
        subject = account[2] 
        # The mensage
        mensage = account[4]

        msg = MIMEMultipart("alternative")
        # set the sender's email
        msg["From"] = FROM
        # set the receiver's email
        msg["To"] = TO
        # set the subject
        msg["Subject"] = subject

        # set the body of the email as HTML
        html =  mensage

        # make the text version of the HTML
        text = bs(html, "html.parser").text

        # set the body of the email as HTML
        # html = open("mail.html").read()
        # make the text version of the HTML
        text = bs(html, "html.parser").text

        text_part = MIMEText(text, "plain")
        html_part = MIMEText(html, "html")
        # attach the email body to the mail message
        # attach the plain text version first
        msg.attach(text_part)
        msg.attach(html_part)

        print(msg.as_string())

        def send_mail(email, password, FROM, TO, msg):
            # initialize the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            # connect to the SMTP server as TLS mode (secure) and send EHLO
            server.starttls()
            # login to the account using the credentials
            server.login(email, password)
            # send the email
            server.sendmail(FROM, TO, msg.as_string())
            # terminate the SMTP session
            server.quit()


        attachment = str(input("Qual arquivo deseja anexa: "))
        files_to_send = [
            attachment+'.pdf',
        ]

        # initialize the message we wanna send
        msg = MIMEMultipart("alternative")
        # set the sender's email
        msg["From"] = FROM
        # set the receiver's email
        msg["To"] = TO
        # set the subject
        msg["Subject"] = subject
        # set the body of the email as HTML
        html = html
        # make the text version of the HTML
        text = bs(html, "html.parser").text

        text_part = MIMEText(text, "plain")
        html_part = MIMEText(html, "html")
        # attach the email body to the mail message
        # attach the plain text version first
        msg.attach(text_part)
        msg.attach(html_part)
        for file in files_to_send:
            # open the file as read in bytes
            with open(file, "rb") as f:
                # read the file content
                data = f.read()
                # create the attachment
                attach_part = MIMEBase("application", "octet-stream")
                attach_part.set_payload(data)
            # encode the data to base 64
            encoders.encode_base64(attach_part)
            # add the header
            attach_part.add_header("Content-Disposition", f"attachment; filename= {file}")
            msg.attach(attach_part)
        input()
        # send the mail
        send_mail(email, password, FROM, TO, msg)

# test = Send_Email
# test.send_email()