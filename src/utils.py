import json
import os

from src.classes import Category, Product


def read_json(path_to_json):
    full_path = os.path.abspath(path_to_json)
    with open(full_path, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


def create_objects(data):
    categories = []
    for cat in data:
        product = []
        for item in cat["products"]:
            product.append(Product(**item))
        cat["products"] = product
        categories.append(Category(**cat))

    return categories
