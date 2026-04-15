
import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"

payload = {
    "contents": [
        {
            "parts": [
                {"text": "Чим славний місяць березень?"}
            ]
        }
    ]
}

headers = {
    "x-goog-api-key": "" # тут необхідно вставити API-ключ
}

response = requests.post(url, headers=headers, json=payload)


if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")


