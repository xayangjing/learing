#-*- coding:utf8 -*-
import smtplib
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host= "LasSMTPInt.active.local"  #设置服务器

#covert text to html

line_break="\n"

data=file("result.txt","r").read()
out=data.replace(line_break,"<br/>")

file("result.html","w").write(out)
with open('result2.html','rb') as f:
    content = f.read()

sender = 'soi_admins@activenetwork.com'
receivers = ['john.yang@activenetwork.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_message = """
<html>
<header>
    <meta http-equiv="Content-Type" content="text/html; charset=us-ascii">
    <style>
TABLE {border-width: 1px;border-style: solid;border-color: black;border-collapse: collapse;}
TH {border-width: 1px;padding: 3px;border-style: solid;border-color: black;background-color: #6495ED;}
TD {border-width: 1px;padding: 3px;border-style: solid;border-color: black;}
.odd  { background-color:#ffffff; }
.even { background-color:#dddddd; }
</style>
<img src="cid:image1">
</header>

<body> 
    <H1><p>Notification:</p></H1>
   %s 
 </body>
 <footer> <img src="cid:image2"> </footer>
</html>
""" % content

message = MIMEMultipart('related')
message.attach(MIMEText(mail_message, 'Html', 'utf-8'))

image1 =MIMEImage(open(r'D:\Python Scritps\git\learing\top.jpg','rb').read())
image2 =MIMEImage(open(r'D:\Python Scritps\git\learing\bottom.jpg','rb').read())


image1.add_header('Content-ID','<image1>')
image2.add_header('Content-ID','<image2>')

message.attach(image1)
message.attach(image2)



#message['From'] = Header("菜鸟教程", 'utf-8')
message['to'] =  ";".join(receivers)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP(mail_host)
    #smtpObj.starttls() 
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"