import os
import smtplib
from email.message import EmailMessage

sender = os.environ["EMAIL_USERNAME"]
password = os.environ["EMAIL_APP_PASSWORD"]
receiver = os.environ["EMAIL_TO"]
schedule = os.environ.get("SCHEDULE", "")

if schedule == "30 18 * * *":
    subject = "🎮 EVENING STREAK CHECK — LINKEDIN GAME KAR LE 🔥"
    message = """
🎮 EVENING STREAK CHECK

Bhai, evening ho gayi 😄

LinkedIn game/streak check kar le.
🔥 Streak ko break mat hone dena!

⏰ Smart Reminder — 6:30 PM
"""

elif schedule == "0 22 * * *":
    subject = "🚨🔥 STREAK ALERT — LINKEDIN GAME KAR LE 🔥🚨"
    message = """
🚨 STREAK ALERT 🚨

Bhai, sone se pehle LinkedIn game kar le! 😭🔥

Apni streak bachani hai.
🎮 Game check kar aur streak continue rakh!

⏰ Smart Reminder — 10:00 PM
"""

elif schedule == "30 0 * * *":
    subject = "🔥 LAST CALL — STREAK BACHA LE 🔥"
    message = """
🔥🔥 LAST CALL 🔥🔥

Bhai, ab last reminder hai! 😭

🎮 LinkedIn game kar le.
🔥 Streak bachani hai!

⏰ Smart Reminder — 12:30 AM
"""

else:
    subject = "🔔 SMART REMINDER — CHECK YOUR REMINDER"
    message = """
🔔 SMART REMINDER

Bhai, ye tumhara automatic reminder hai.

🎮 Apna LinkedIn game/streak check kar le.

🔥 DON'T BREAK THE STREAK!
"""

msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver
msg.set_content(message)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("✅ Reminder email sent successfully!")
