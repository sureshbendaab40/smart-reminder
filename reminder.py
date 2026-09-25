import os
import smtplib
from email.message import EmailMessage

sender = os.environ["EMAIL_USERNAME"]
password = os.environ["EMAIL_APP_PASSWORD"]
receiver = os.environ["EMAIL_TO"]

msg = EmailMessage()
msg["Subject"] = "🚨 SMART REMINDER — CHECK YOUR REMINDER 🚨"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("""
🔔 SMART REMINDER

Bhai, ye tumhara scheduled reminder hai.

⏰ Time ho gaya hai — apna important task check kar lo.

🔥 Smart Reminder System
""")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("✅ Reminder email sent successfully!")
