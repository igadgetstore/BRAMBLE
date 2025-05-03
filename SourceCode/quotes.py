import requests

def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} — {data[0]['a']}"
    except:
        return "Stay focused and never give up."