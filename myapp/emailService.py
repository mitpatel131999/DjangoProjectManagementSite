from django.conf import settings
from django.core.mail import send_mail

class sendEmail:
    email_from = settings.EMAIL_HOST_USER
    email_target = ['mitpatelr1999@gmail.com','patelshrirang54@gmail.com']
    subject = ''
    message = f''
    recipient_list = []
    def __init__(self,subject,message,recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
    
    def sendEmail(self):
        return send_mail(self.subject, self.message, self.email_from, self.recipient_list)