import os
import requests
import pytesseract
from PIL import Image
from io import BytesIO

# 配置参数
LOGIN_URL = "https://xxcx.hljea.org.cn/JWWebCxzxNew/examType/doLogin"
CAPTCHA_URL = "https://xxcx.hljea.org.cn/JWWebCxzxNew/examType/getVerify"

# 获取登录后的 Cookie
def get_cookies(session):
    cookies = session.cookies.get_dict()
    print("登录后的 Cookies:", cookies)
    return cookies

# 获取验证码文本
def get_captcha_text(captcha_image):
    # 将图片转换为灰度图像以便 OCR 识别
    image = Image.open(BytesIO(captcha_image)).convert("L")
    return pytesseract.image_to_string(image, config="--psm 6").strip()

def login():
    session = requests.Session();
    # 首次获取验证码（可能需要携带特定参数）
    captcha_response = session.get(CAPTCHA_URL)
    captcha_code = get_captcha_text(captcha_response.content)
    print(f"识别的验证码：{captcha_code}")

session = login()
