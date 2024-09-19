import requests
import json

class Groq:
    def __init__(self, prompt: str, api_key: str,role_act:str) -> None:
        self.prompt = prompt
        self.api_key = api_key
        self.role_act=role_act

    def treatment_request(self, response: requests.Response) -> str:
        text = "No text found"
        try:
            data = response.json()
            if 'choices' in data and len(data['choices']) > 0:
                text = data['choices'][0]['message']['content']
        except ValueError:
            print("Erro ao processar a resposta JSON.")
        return text

    def request_to_groq(self) -> str:
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = {
            "messages": [
                {"role":self.role_act, "content": self.prompt}
            ],
            "model": "llama3-8b-8192"
        }
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        
        return self.treatment_request(response)