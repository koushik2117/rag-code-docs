import requests

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/generate-docs-folder/"

# Path to the folder containing Python files
folder_path = r"C:\Users\saiko\rag-code-docs\test_folder"

# Parameters
params = {"folder_path": folder_path}

# Make POST request
response = requests.post(url, params=params)

# Print status and response
print("Status code:", response.status_code)
print("Response JSON:", response.json())
