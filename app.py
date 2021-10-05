import smtplib, ssl, json
from flask import Flask, request


app = Flask(__name__)

def list_builder(file):
    file.seek(0)
    file_lines = file.read()
    list = file_lines.split("\n")
    return list

def send_email(email_body):
    sender_email = <UPDATE_VALUE>
    sender_password = <UPDATE_VALUE>
    receiver_email = <UPDATE_VALUE>
    subject = "Anchore Notification"
    content = email_body
    ssl_context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n{content}")
    server.quit()
    

#This route will receive the anchore notifications. Iterate through email address list stored in .txt file in container and send the notifications to each user
@app.route('/anchore_webhook', methods=['POST'])
def anchore_webhook():
    if request.method == 'POST':
        email_body = json.dumps(request.json, sort_keys=True, indent=4)
        send_email(email_body)
        return 'success', 200
    else:
        abort(400)

#Test route to test the webhooks initially are being received properly.
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        send_email()
        return 'success', 200
    else:
        abort(400)

#Route to receive new email addresses to add to the user list.
@app.route('/email', methods=['POST'])
def email():
    if request.method == 'POST':
        data = (request.json)
        print(data)
        new_user_email = data["email_address"]
        with open("user_emails.txt", 'a+') as f:
            f.write(new_user_email + "\n")
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5080')