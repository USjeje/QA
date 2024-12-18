import requests
import json

MODEL = "qwen2.5:3b"
STREAM = True


url = "http://localhost:11434/api/"
generate_url = url + "generate"
chat_url = url + "chat"

generate_data = {
    "model": MODEL,
    "prompt": "你是谁",
    "stream": STREAM
}

chat_data = {
    "model": MODEL,
    "messages": [{
      "role": "user",
      "content": "why is the sky blue?"
    }],
    "stream": STREAM
}

multi_chat_data = {
    "model": MODEL,
    "messages": [
        {
          "role": "user",
          "content": "why is the sky blue?"
        },
        {
          "role": "assistant",
          "content": "due to rayleigh scattering."
        },
        {
          "role": "user",
          "content": "how is that different than mie scattering?"
        }
      ],
    "stream": STREAM
}

# response = requests.post(generate_url, json=generate_data, stream=STREAM)
response = requests.post(chat_url, json=chat_data, stream=STREAM)
# response = requests.post(chat_url, json=multi_chat_data, stream=STREAM)

if STREAM:
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            print(chunk.decode('utf-8'), end='')
else:
    print(json.dumps(response.json(), indent=4))
