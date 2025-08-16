import requests

# Replace with your actual Gemini API key
API_KEY = "enter your API key"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def ask_gemini(message):
    prompt = f"Is the following message good or bad? Just answer 'Good' or 'Bad'. Message: \"{message}\""

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(GEMINI_API_URL, json=data)
    
    if response.status_code == 200:
        content = response.json()
        try:
            return content['candidates'][0]['content']['parts'][0]['text']
        except:
            return "Error: Unexpected response format."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main script
user_message = input("Enter a message: ")
gemini_response = ask_gemini(user_message)
print("Gemini says:", gemini_response)
