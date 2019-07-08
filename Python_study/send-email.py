# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
<<<<<<< HEAD
from email.header import Header
# email 用于构建邮件内容

'''
# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '1548088010@qq.com'
password = 'djymvhodgjipgcef'

# 收信方邮箱
to_addr = '631975263@qq.com'
'''

# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')

# 收信方邮箱
to_addr = input('请输入收件邮箱：')
=======
# email 用于构建邮件内容

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '631975263@qq.com'
password = 'nqttffg'

# 收信方邮箱
to_addr = '1548088010@qq.com'
>>>>>>> 1737fca23a0a0c88465792a5df19b376851efef5

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
<<<<<<< HEAD
text = '''Hi,Baby

    我只是在睡前想了一下你
    你就出现在了我的梦里
    很真实只是寒暄几句
    心跳却感觉那么熟悉
    我只是在睡前想了一下你
    你就还原在了我的心里
    如果我们能不期而遇
    你对我一笑我就知道
'''
msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('Python sent email')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP()
server.connect(smtp_server,25)
=======
msg = MIMEText('send by python','plain','utf-8')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
>>>>>>> 1737fca23a0a0c88465792a5df19b376851efef5
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()
