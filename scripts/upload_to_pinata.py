import requests
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PINATA_BASE_URL = 'https://api.pinata.cloud/'
endpoint = 'pinning/pinFileToIPFS'
# Change this to upload a different file
headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
           'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}


def upload(filepath):
    filename = filepath.split('/')[-1:][0]
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(PINATA_BASE_URL + endpoint,
                                 files={"file": (filename, image_binary)},
                                 headers=headers)
        print(response.json())
        return response.json()['IpfsHash']


def upload_binary(content, filename):
    response = requests.post(PINATA_BASE_URL + endpoint,
                             files={"file": (filename, content)},
                             headers=headers)
    print(response.json())
    return response.json()['IpfsHash']


if __name__ == "__main__":
    img_hash = upload('./img/rob.png')
    print(img_hash)
