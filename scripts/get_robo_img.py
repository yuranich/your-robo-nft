import requests
from pathlib import Path


def execute(text):
    response = requests.get("https://robohash.org/" + text + ".png?size=200x200")
    return response.content


if __name__ == "__main__":
    path = "./img/rob.png"
    content = execute("your lovely robot image indeed")
    with Path(path).open("wb") as image:
        image.write(content)
