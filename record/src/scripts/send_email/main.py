import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from load_config.load_file import load_time
from extract.deal import deal

time = load_time()
month = time["month"]

if __name__ == '__main__':
    fromaddr = '430533427@qq.com'
    password = ''
    toaddrs = ['1430732229@qq.com']

    content = '申老师好：\n\t请查收 北京量码博信数据技术有限公司{}月份考勤表~'.format(month)
    textApart = MIMEText(content)

    excelFile = deal()
    excelpart = MIMEApplication(open(excelFile, 'rb').read())
    excelpart.add_header('Content-Disposition', 'attachment',
                         filename=excelFile.replace(("../../../output/"), "{}月".format(month)))

    m = MIMEMultipart()
    m["From"] = "quanhai.cheng@jnyl-tech.com"
    m["To"] = "yaping.shen@jnyl-tech.com"
    m.attach(textApart)
    m.attach(excelpart)
    m['Subject'] = '{}月考勤表'.format(month)

    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string(), rcpt_options="quanhai.cheng@jnyl-tech.com")
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误
