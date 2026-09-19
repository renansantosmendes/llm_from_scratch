

import os
import requests

def fetch_data():
    if not os.path.exists("the-verdict.txt"):
        url = (
            "https://raw.githubusercontent.com/rasbt/"
            "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
            "the-verdict.txt"
        )
        file_path = "the-verdict.txt"

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        
       
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
        
    return raw_text