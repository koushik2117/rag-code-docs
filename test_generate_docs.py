import requests
import json

# Replace with your folder path containing Python files
folder_path = r"C:\Users\saiko\rag-code-docs\app"

url = "http://127.0.0.1:8000/generate-docs-folder/"
params = {"folder_path": folder_path}

try:
    response = requests.post(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    print("✅ Response from server:")
    print(json.dumps(data, indent=4))

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Oops! Something went wrong:", err)
