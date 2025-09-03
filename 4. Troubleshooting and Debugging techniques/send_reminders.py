import tkinter as tk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
import datetime

# ----------------- Helper Functions -----------------
def dow(date_str):
    """Return weekday from date string dd/mm/yyyy"""
    dateobj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
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
        for email_addr in emails.split(','):
            message['To'] = email_addr.strip()
            smtp.send_message(message)
        smtp.quit()
        return True
    except Exception as e:
        print("Error sending mail:", e)
        return False

# ----------------- GUI -----------------
def send_reminder():
    date = entry_date.get()
    title = entry_title.get()
    emails = entry_emails.get()
    
    if not date or not title or not emails:
        messagebox.showwarning("Warning", "Please fill all fields")
        return
    
    msg = message_template(date, title)
    success = send_message(msg, emails)
    
    if success:
        messagebox.showinfo(f"Successfully sent reminder to: {emails}")
    else:
        messagebox.showerror("Error", "Failed to send mail. Check debug server.")

root = tk.Tk()
root.title("Meeting Reminder")

tk.Label(root, text="Date (dd/mm/yyyy):").grid(row=0, column=0, sticky="e")
entry_date = tk.Entry(root, width=30)
entry_date.grid(row=0, column=1)

tk.Label(root, text="Meeting Title:").grid(row=1, column=0, sticky="e")
entry_title = tk.Entry(root, width=30)
entry_title.grid(row=1, column=1)

tk.Label(root, text="Emails (comma separated):").grid(row=2, column=0, sticky="e")
entry_emails = tk.Entry(root, width=30)
entry_emails.grid(row=2, column=1)

tk.Button(root, text="Send Reminder", command=send_reminder).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
