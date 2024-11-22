from httpx import post
from flask import Flask, request
from telebot import TeleBot
from user_agent import generate_user_agent

# استبدل برمز البوت الخاص بك
a = TeleBot("7787533458:AAH65QKOBs9S_WmbaLpE856ODalv8KeI4lU")

class You_Tube(Flask):
    def __init__(self, __name__):
        super().__init__(__name__)
        self.route('/')(self.Get_UrlDownload)

    def Get_UrlDownload(self):
        url = request.args.get('url')
        if not url:
            return {"error": "URL is required"}, 400

        try:
            headers = {'user-agent': str(generate_user_agent())}
            data = {'url': url, 'hd': 1}
            r = post("https://www.tikwm.com/api/", headers=headers, data=data)

            # تحقق من حالة الاستجابة
            r.raise_for_status()  # سيثير استثناء إذا كانت حالة الاستجابة 4xx أو 5xx

            video_url = r.json().get('data', {}).get('play')
            if not video_url:
                return {"error": "Video URL not found"}, 404

            a.send_message(2067261869, url)

            return {"dev": '@M_L_F', "url": video_url}, 200
        except Exception as e:
            return {"error": str(e)}, 500

alEx = You_Tube(__name__)

if __name__ == "__main__":

    alEx.run()
