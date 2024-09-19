import os
from gemini import Gemini
from llama import Groq
from dotenv import load_dotenv
import json
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

user_prompt = ""

def create_prompt():
    prompt_description = f'''
<rules>
Sera enviado um comentario, sobre uma avaliacao de um usuario no github. segue as regras necessarias na resposta:
-Se estiver em ingles ou outra lingua traduza em portugues, 
-a resposta dever breve e curta
-a resposta deve começar assim: "École 42:"

</rules>

<specific_question>
Descreva a École 42 e seu método de ensino. Destaque os pontos principais que seriam relevantes para sua perspectiva.
</specific_question>
    '''
    return prompt_description 



if __name__ == "__main__":

    with open("roles.json", "r", encoding="utf-8") as file:
            roles = json.load(file)

    print("=== Análises usando GEMINI ===")
    for key, value in roles.items():
        print("-- Análise da perspectiva de "+key+" ---")
        response = Gemini(create_prompt(), GOOGLE_API_KEY,value).request_to_gemini()
        print(response)

    print()
    print("=== Análises usando LLAMA ===")
    for key, value in roles.items():
        print("-- Análise da perspectiva de "+key+" ---")
        response = Groq(create_prompt(), GROQ_API_KEY,value).request_to_groq()
        print(response)