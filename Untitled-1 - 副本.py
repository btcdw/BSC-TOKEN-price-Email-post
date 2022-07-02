'''
HASH数据来源：https://dex.guru/
headers一键生成地址：https://curlconverter.com/#python

'''


import requests
import smtplib
from email.mime.text import MIMEText
import time


while True:
    # 以下为请求价格
    headers = {
        'authority': 'api.dex.guru',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://dex.guru',
        'referer': 'https://dex.guru/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'traceparent': '00-06a4160e1318e57f3def9c45be00bd8c-66e32ce5556125f7-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-session-id': 'c508474d41fc4196898624d215ff3305',
    }

    data = '{"ids":["0x555d8355a31d62c68e13074bae90dc548ab6faf9-bsc"],"network":"eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche"}'

    a = requests.post('https://api.dex.guru/v3/tokens', headers=headers, data=data)
    b = a.json()
    c = b["data"][0]['priceUSD']
    # print(c)


    # 以下为发送邮箱
    msg_from = 'xxxxxxxxxx@qq.com'  # 发送方邮箱地址。
    password = 'xxxxxxxxxx'  # 发送方QQ邮箱授权码，不是QQ邮箱密码。
    msg_to = 'xxxxxxxx@163.com'  # 收件人邮箱地址。
    
    subject = "HASH价格:{}".format(str(c))  # 主题。
    content = "无正文"  # 邮件正文内容。
    msg = MIMEText(content, 'plain', 'utf-8')
    
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    
    try:
        client = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        # print("连接到邮件服务器成功")
    
        client.login(msg_from, password)
        # print("登录成功")
    
        client.sendmail(msg_from, msg_to, msg.as_string())
        # print("发送成功")
    except smtplib.SMTPException as e:
        print("发送邮件异常")
    finally:
        client.quit()

    time.sleep(60)
    # 60秒后再次发送