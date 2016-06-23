import requests, time

datestring = time.strftime("%Y-%m-%d")
filename = "reddit-" + datestring + ".csv"

def send_message(to='paul.ronga@laposte.net', subject='No Subject', message='Test message', file='test.csv'):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd0b0701ec9a74e0eba05c70bd49ed81a.mailgun.org/messages",
        auth=("api", "THE-KEY"),
        files=[("attachment", open(file))],
        data={"from": "Paul Ronga (MG) <mailgun@mg.tcch.ch>",
              "to": [to],
              "subject": subject,
              "text": message})

result = send_message(subject='Your last scraping', message='Here you are!', file=filename)
print("File sent:", filename)
