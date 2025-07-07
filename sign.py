import requests
import os
import json
from datetime import datetime

# 从环境变量获取账号密码
ACCOUNT = os.getenv('CG_ACCOUNT')
PASSWORD = os.getenv('CG_PASSWORD')

def login():
    """账号密码登录获取session"""
    session = requests.Session()
    login_url = "https://cg.163.com/api/v1/login"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Origin": "https://cg.163.com",
        "Referer": "https://cg.163.com/"
    }
    
    login_data = {
        "username": ACCOUNT,
        "password": PASSWORD,
        "rememberLogin": "true"
    }
    
    try:
        response = session.post(login_url, headers=headers, json=login_data)
        if response.json().get("code") == 0:
            print("登录成功")
            return session
        else:
            print(f"登录失败: {response.text}")
            return None
    except Exception as e:
        print(f"登录请求异常: {str(e)}")
        return None

def daily_sign(session):
    """执行每日签到"""
    sign_url = "https://cg.163.com/api/v1/user/sign"
    try:
        response = session.post(sign_url)
        result = response.json()
        if result.get("code") == 0:
            print(f"[{datetime.now()}] 签到成功！奖励: {result.get('data', {}).get('awardName', '未知')}")
        else:
            print(f"签到失败: {result.get('message')}")
    except Exception as e:
        print(f"签到请求异常: {str(e)}")

if __name__ == "__main__":
    client = login()
    if client:
        daily_sign(client)
