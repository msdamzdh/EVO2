import requests
import os
from dotenv import load_dotenv
from routes.views.gen_seq import Params
import json


load_dotenv('.env-dev')

NVIDIA_URL = os.getenv("NVIDIA_URL")
BASE_URL = "http://" + str(os.getenv("URL")) + ":"+ str(os.getenv("PORT"))

def main_test():
    response = requests.get(
        url=BASE_URL
    )
    assert len(response.json()["message"])>1
    
data = Params(sequence="ACTGACTGACTGACTG",
               top_k=1,
               num_tokens=20,
               enable_sampled_probs=False)
headers = {
  'Content-Type': 'application/json'
}

payload = json.dumps(dict(data))

def genSeq():
    response = requests.post(
        url=BASE_URL+"/genSeq",
        data=payload,
        headers=headers
    )
    assert len(dict(response.json())["sequence"])>1

if __name__ == "__main__":
    main_test()
    genSeq()
    print("Everything passed")
