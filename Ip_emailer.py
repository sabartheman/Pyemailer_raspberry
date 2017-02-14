from smtplib import SMTP
from email.mime.text import MIMEText
import socket


#this function will try to poll ip of the host machine
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#this function will build and send a email.
def build_n_send_email():
        #what server to connect to
        #this example connects to gmails smtp
	server = SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("insert@email.here", "yourpassword")
	
        #open a text file if you need to read from it
	fp = open("textFile.txt",'rb')
	
        #two sets of emails 
        #first is the host
        #second is the recipient
	me = "host@email.com"
	you = "destination@email.com"

        #runs a command to pull the ip, if you are 
        #on a non enterprise network this will just
        #return a local ip (Ex: 192.168.1.8)
	msg = MIMEText(get_ip())
	fp.close()
	msg['Subject'] = 'Ip of the host'
	msg['From']    = me
	msg['To']      = you

        #command to send the email out
	server.sendmail(me,[you],msg.as_string())
        #cleaning up the loose ends.
        server.quit()


build_n_send_email()

