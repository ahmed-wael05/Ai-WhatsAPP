from datetime import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

schedule = {
    "Saturday": ["10:00 - 12:00 AI", "2:00 - 4:00 Math"],
    "Sunday": ["12:00 - 2:00 Physics"],
    "Monday": ["10:00 - 12:00 Programming"],
    "Tuesday": [],
    "Wednesday": ["11:00 - 1:00 Data Science"],
    "Thursday": [],
    "Friday": []
}

def create_message():
    today = datetime.now().strftime("%A")
    lectures = schedule.get(today, [])

    if not lectures:
        return "صباح الخير ☀️\nمفيش محاضرات النهارده 😎"

    msg = "صباح الخير ☀️\n\n📚 محاضراتك النهارده:\n\n"
    for lec in lectures:
        msg += f"- {lec}\n"

    return msg

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=create_message(),
    to='whatsapp:+201201766990'
)

print(message.sid)
print(account_sid)
print(auth_token)
