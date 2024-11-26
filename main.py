import openai
import requests
import sys
import json

# Carregar os parâmetros do webhook
if len(sys.argv) > 1:
    input_data = json.loads(sys.argv[1])
else:
    input_data = {"task": "generate_text", "prompt": "Texto padrão"}

# Configurar chave da OpenAI
openai.api_key = "SUA_API_KEY_AQUI"

# Configurar URL do Webhook do Make
MAKE_WEBHOOK_URL = "SUA_WEBHOOK_URL_AQUI"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

# Executar a tarefa solicitada
if input_data["task"] == "generate_text":
    result = generate_text(input_data["prompt"])
    payload = {"text": result}

elif input_data["task"] == "generate_image":
    result = generate_image(input_data["prompt"])
    payload = {"image_url": result}

else:
    payload = {"error": "Tarefa desconhecida"}

# Enviar o resultado para o Webhook do Make
requests.post(MAKE_WEBHOOK_URL, json=payload)
