import requests

class Gemini:
    def __init__(self, prompt: str, api_key: str) -> None:
        self.prompt = prompt
        self.api_key = api_key

    def request_to_gemini(self) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        payload = {
            "contents": [{
                "parts": [{"text": self.prompt}]
            }]
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        
        return response