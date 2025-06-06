import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Anh Hoang'
email['to'] = '_email_'
email['subject'] = 'Test Email'
email.set_content('This is a test email sent from Python!')
def send_email():
    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('_email_', '_password_')
            smtp.send_message(email)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

send_email()