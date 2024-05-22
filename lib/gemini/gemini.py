import google.generativeai as genai
from config.gemini import GEMINI_API_KEY

from lib.analysis.analysis import Analysis
from lib.vulnerabilites.vulnerability import Vulnerability

class Gemini:
    def __init__(self) -> None:
        genai.configure(api_key=GEMINI_API_KEY)

        safety_settings = [
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        self.model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)

    def prompt(self, text: str) -> str:
        res = self.model.generate_content(text)

        return res.text
