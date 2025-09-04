from flask import Flask, request, render_template_string
import datetime
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

def dow(date_str):
    """Return weekday from date string yyyy-mm-dd"""
    dateobj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title):
    """Create email message"""
    weekday = dow(date)
    msg = EmailMessage()
    msg['Subject'] = f'Meeting reminder: "{title}"'
    msg.set_content(f"""
Hi all,

This is a quick mail to remind you all that we have a meeting about:
"{title}"
The {weekday} {date}.

See you there!
""")
    return msg

def send_message(message, emails):
    """Send message using local debug SMTP"""
    try:
        smtp = smtplib.SMTP('localhost', 1025)  # Debug server
        message['From'] = "noreply@example.com"

        # Tách từng email và gửi riêng
        email_list = [e.strip() for e in emails.split(',') if e.strip()]
        if not email_list:
            raise ValueError("No valid email addresses provided.")

        sent_list = []
        for email_addr in email_list:
            # tạo bản copy của message để tránh overwrite header
            msg_copy = EmailMessage()
            msg_copy.set_content(message.get_content())
            msg_copy['Subject'] = message['Subject']
            msg_copy['From'] = message['From']
            msg_copy['To'] = email_addr
            smtp.send_message(msg_copy)
            sent_list.append(email_addr)

        smtp.quit()
        return sent_list
    except Exception as e:
        print("Failed to send reminders:", e)
        return []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Meeting Reminder</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        label { display: block; margin-top: 10px; }
        input[type=text], input[type=date] { width: 300px; padding: 5px; }
        button { margin-top: 20px; padding: 10px 20px; }
        .result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Send Meeting Reminder</h2>
    <form method="post">
        <label>Date (yyyy-mm-dd):</label><br>
        <input type="date" name="date" required><br><br>
        <label>Title:</label><br>
        <input type="text" name="title" required><br><br>
        <label>Emails (comma separated):</label><br>
        <input type="text" name="emails" required><br><br>
        <input type="submit" value="Send Reminder">
    </form>
    {% if result %}
    <h3>Result:</h3>
    <p>{{ result|safe }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        date = request.form.get('date')
        title = request.form.get('title')
        emails = request.form.get('emails')
        try:
            message = message_template(date, title)
            sent_list = send_message(message, emails)
            if sent_list:
                result_lines = [f"Successfully sent reminders to: {email}\n" for email in sent_list]
                result = "<br>".join(result_lines)
            else:
                result = "Failed to send reminders. Please check SMTP server."
        except Exception as e:
            result = f"Failed to send reminders: {e}"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
