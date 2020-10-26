# coding: utf-8
import requests
import json

json_open = open('hoge.json', 'r', encoding="utf8")
json_load = json.load(json_open)


def main():
    for json_values in json_load.values():
        for json in json_values:
            image_url = json["image"]
            file_name = "hoge" + ".jpg"

            response = requests.get(image_url)
            image = response.content

            with open(file_name, "wb") as file:
                file.write(image)


if __name__ == "__main__":
    main()
