# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr(( \
		Header(name,'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')
smtp_server = 'smtp.qq.com'
smtp_port = 587

msg = MIMEText('hello, send by Python...','plain','utf-8')
msg['From'] = _format_addr(u'Python Lovers <%s>' % from_addr)
msg['To'] = _format_addr(u'Admin <%s>' % to_addr)
msg['Subject'] = Header(u'Greetings from SMTP...','utf-8').encode()

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit
