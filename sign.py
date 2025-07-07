   import requests
import os
from datetime import datetime

# 从GitHub Secrets获取账号信息
username = os.getenv('WYY_USERNAME')
password = os.getenv('WYY_PASSWORD')

def login():
    """模拟登录网易云游戏平台"""
    login_url = 'https://cg.163.com/login'
    session = requests.Session()
    
    login_data = {
        'username': username,
        'password': password,
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = session.post(login_url, data=login_data, headers=headers)
    if '登录成功' in response.text:
        print("登录成功")
        return session
    else:
        print("登录失败")
        return None

def sign_in(session):
    """执行签到操作"""
    sign_url = 'https://game.163.com/api/signin'
    
    response = session.post(sign_url)
    if response.json().get('code') == 200:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 签到成功")
    else:
        print(f"签到失败: {response.text}")

if __name__ == '__main__':
    client = login()
    if client:
        sign_in(client)
