from gemini import Gemini
from dotenv import load_dotenv
import os
import json

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def yield_calculator(Object_Cal):
    for x in Object_Cal:
        yield x

def create_prompt(specific_question):
    prompt_description = f'''
<rules>
Sera enviado um comentario, sobre uma avaliacao de um usuario no github. segue as regras necessarias na resposta:
-Se estiver em ingles ou outra lingua traduza em portugues, 
-a unica resposta que devera ser retornarda e o sentimento do comentario. Exemplo: Positivo ou Negativo
-retornar somente Positivo ou Negativo
</rules>

<specific_question>
{specific_question}
</specific_question>
    '''
    return prompt_description 

def call_llm(text):
    prompt = create_prompt(text)
    response = Gemini(prompt, GOOGLE_API_KEY).request_to_gemini()
    return response

def analyze_sentiments(comments):
    for comment in yield_calculator(comments):
        llm_response = call_llm(comment['text'])
        sentiment = parse_llm_response(llm_response)
        comment['sentiment'] = sentiment

def parse_llm_response(response):
    try:
        data = response.json()
        if 'candidates' in data and len(data['candidates']) > 0:
            sentiment = data['candidates'][0]['content']['parts'][0]['text'].strip()
            if sentiment.lower() in ['positivo', 'negativo']:
                return sentiment.capitalize()
            else:
                return 'Desconhecido'
    except ValueError:
        print("Erro ao processar a resposta JSON.")
        return 'Desconhecido'

if __name__ == "__main__":

    with open("comments.json", "r", encoding="utf-8") as file:
        github_comments = json.load(file)


    analyze_sentiments(github_comments)
    print()

    for comment in github_comments:
        print(f"Texto: {comment['text']}")
        print(f"Sentimento: {comment['sentiment']}")
        print("-" * 50)


