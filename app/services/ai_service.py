from groq import Groq
from config import Config

class AIServiceError(Exception):
    pass

class AIService:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.sohbet_hafizasi = [{"role": "system", "content": Config.BUSINESS_CONTEXT}]

    def yanit_uret(self, mesaj):
        self.sohbet_hafizasi.append({"role": "user", "content": mesaj})
        try:
            chat_completion = self.client.chat.completions.create(
                messages=self.sohbet_hafizasi,
                model="openai/gpt-oss-120b"
            )
            ai_cevabi = chat_completion.choices[0].message.content
            self.sohbet_hafizasi.append({"role": "assistant", "content": ai_cevabi})
            return ai_cevabi
        except Exception as e:
            raise AIServiceError("Sistemlerimizde yoğunluk var, tekrar deneyiniz.")

ai_service = AIService()

def yapay_zeka_ile_konus(kullanici_mesaji):
    try:
        return ai_service.yanit_uret(kullanici_mesaji)
    except AIServiceError as e:
        return str(e)