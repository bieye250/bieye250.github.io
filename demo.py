import os
import requests
import pytesseract
from PIL import Image
from io import BytesIO
import ddddocr
ocr = ddddocr.DdddOcr()

# 配置参数
LOGIN_URL = "https://xxcx.hljea.org.cn/JWWebCxzxNew/examType/edit?pid=2502242402"
CAPTCHA_URL = "https://xxcx.hljea.org.cn/JWWebCxzxNew/examType/getVerify"
POST_URL = "https://xxcx.hljea.org.cn/JWWebCxzxNew/examType/checkClassScore"
headers = {
    'Content-Type': 'application/json;charset=utf-8'
}

# 获取登录后的 Cookie
def get_cookies(session):
    cookies = session.cookies.get_dict()
    print("登录后的 Cookies:", cookies)
    return cookies

# 获取验证码文本
def get_captcha_text(img_url):
    # 通过接口请求url地址，并保存在本地
    r = requests.get(img_url)
    with open('1111.jpg', 'wb+') as f:  
        f.write(r.content)
    # 再次读取图片信息
    with open('1111.jpg', 'rb')as f2:
        img_bytes = f2.read()
    # 通过ddddocr进行识别验证码
    res = ocr.classification(img_bytes)
    return res

def login():
    session = requests.Session();
    # 首次获取验证码（可能需要携带特定参数）
    captcha_response = session.get(CAPTCHA_URL)
    captcha_code = get_captcha_text(CAPTCHA_URL)
    print(f"识别的验证码：{captcha_code}")
    # 构造登录参数（需通过浏览器抓包确认字段名）
    form_data = {
        "authCode": captcha_code,
        "exam_type_id": "2502242402",
        "ksh": "102135000002874",
        "xm": "陶家畅"
        # 可能需要其他隐藏字段如csrf token
    }
    # 发送登录请求
    response = session.post(POST_URL, headers=headers, data=form_data)
    print(response.text)

session = login()
