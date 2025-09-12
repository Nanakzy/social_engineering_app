import requests
import os

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def fetch_image(query: str, save_path: str) -> str:
    url = "https://api.unsplash.com/photos/random"
    params = {
        "query": query,
        "orientation": "landscape",
        "content_filter": "high",
        "client_id": UNSPLASH_ACCESS_KEY
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()

    img_url = data["urls"]["regular"]
    img_data = requests.get(img_url).content

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(img_data)

    return save_path