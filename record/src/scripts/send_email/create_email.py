import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from load_config.load_file import load_time

time = load_time()
month = time["month"]


def create_email(email_subject, content, annex_path, annex_name):
    textApart = MIMEText(content)
    excelFile = annex_path
    excelApart = MIMEApplication(open(excelFile, 'rb').read())
    excelApart.add_header('Content-Disposition', 'attachment', filename=annex_name)
    message = MIMEMultipart()
    message['From'] = "quanhai.cheng@jnyl-tech.com"
    message['To'] = "yaping.shen@jnyl-tech.com"
    message.attach(textApart)
    message.attach(excelApart)
    message['Subject'] = email_subject
    return message


def send_email(sender, password, receiver, msg):
    try:
        # 找到你的发送邮箱的服务器地址，已加密的形式发送
        server = smtplib.SMTP("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        # 登录你的账号
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号（是一个列表）、邮件内容
        print("邮件发送成功")
        server.quit()  # 关闭连接
    except smtplib.SMTPException as e:
        print("error:", e)
