import os
import smtplib
from email.message import EmailMessage

sender = os.environ["EMAIL_USERNAME"]
password = os.environ["EMAIL_APP_PASSWORD"]
receiver = os.environ["EMAIL_TO"]

msg = EmailMessage()
msg["Subject"] = "🚨🔥 STREAK ALERT — LINKEDIN GAME KAR LE 🔥🚨"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("""
🚨🚨 SMART REMINDER 🚨🚨

BHAI, RUK MAT! 😭🔥

🎮 LinkedIn game/streak check kar le.
🔥 Apni streak bachani hai!

⏰ Ye automatic Smart Reminder hai.
☁️ Laptop OFF hone par bhi GitHub se reminder aa jayega.

━━━━━━━━━━━━━━━━━━━━
💪 STAY CONSISTENT
🔥 DON'T BREAK THE STREAK
━━━━━━━━━━━━━━━━━━━━
""")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("✅ Reminder email sent successfully!")
