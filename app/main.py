# main.py
from fastapi import FastAPI, HTTPException, Query
from app.parser import extract_functions_from_folder
from app.generator import generate_doc
import os
import json

app = FastAPI()

@app.post("/generate-docs-folder/")
def generate_docs_folder(folder_path: str = Query(..., description="Path to the folder containing Python files")):
    # 1. Check if path exists and is a folder
    if not os.path.exists(folder_path):
        raise HTTPException(status_code=400, detail="Folder path does not exist")
    if not os.path.isdir(folder_path):
        raise HTTPException(status_code=400, detail="Provided path is not a folder")

    all_docs = []

    # 2. Iterate over all Python files in folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            functions = extract_functions_from_folder(file_path)  # extract functions
            for func in functions:
                doc = generate_doc(func["code"])
                all_docs.append({
                    "file": filename,
                    "function": func["name"],
                    "documentation": doc
                })

    # 3. Write all docs to a single JSON file
    output_file = os.path.join(folder_path, "docs.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_docs, f, indent=4)

    return {"message": f"Documentation generated successfully!", "output_file": output_file}