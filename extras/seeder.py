import requests
from random import uniform, randint
import tempfile
from urllib.request import urlretrieve
import re
from json import dumps


GB_BASE_API_URL = " https://www.googleapis.com/books/v1/volumes?maxResults=40&q=subject:"
BASE_BOOKSTORE_API_URL = "http://localhost:80/api/v1"
CATEGORIES = [
    "fiction",
    "programming",
    "mathematics",
    "romance",
    "comedy",
    "science",
    "horror",
    "philosophy",
    "adventure",
    "music",
]

def resolve_img(image_url, file_name, file_extension, tmp_dir):
    image_name = re.sub(
        r"[^\w|\d]", "",
        file_name[:20] if len(file_name) > 20 else file_name
    ).strip()
    temp_img, _ = urlretrieve(
        url=image_url,
        filename=f"{tmp_dir.name}/{image_name}.{file_extension}"
    )
    data = None
    with open(temp_img, "rb") as content:
        data = content.read()

    result = {
        "img-name": f"{image_name}.{file_extension}",
        "content": data,
        "file-extension": file_extension
    }
    return result


def random_float(min, max):
    result = uniform(min, max)
    return round(result, 2)


def author_resolver(authors=None):
    if authors is None: return []
    result = []

    for author in authors:
        author_info = author.split(" ")
        if len(author_info) < 2:
            author_info.append(author_info[0][::-1])
        result.append({
            "first_name": author_info[0],
            "paternal_last_name": author_info[1],
            "picture": None
        })
    return result


def category_resolver(categories=None):
    if categories is None: return []
    result = []
    for category in categories:
        result.append({
            "name": category
        })
    return result


def create_payload(json, dup):
    fallback = {
      "title": "untitle",
      "description": "Synopsis coming soon.......",
      "edition": "Standard",
      "language": "en",
      "page_number": randint(500, 1200),
      "publishier": "Unknown",
      "rating": random_float(1.2, 9.9),
      "available": True,
      "categories": [dup["category"]],
      "authors": ["Petter Galahat"],
    }

    template = {
      "title": json.get("title", fallback["title"]),
      "description": json.get("description", fallback["description"]),
      "edition": json.get("edition", fallback["edition"]),
      "language": json.get("language", fallback["language"]),
      "page_number": json.get("pageCount", fallback["page_number"]),
      "publishier": json.get("publisher", fallback["publishier"]),
      "rating": json.get("averageRating", fallback["rating"]),
      "available": True,
      "categories": category_resolver(json.get("categories", fallback["categories"])),
      "authors": author_resolver(json.get("authors", fallback["authors"])),
      "price": random_float(3.5, 20.4),
    }
    return template


def generate_jwt_tokens(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(
        f"{BASE_BOOKSTORE_API_URL}/auth/jwt/create/",
        data=payload
    )
    response_json = response.json()
    if response.status_code == 401:
        raise Exception(response_json.get("detail", "Something went wrong"))
    return response_json


if __name__ == "__main__":
    tokens = generate_jwt_tokens(username="yagua", password="root")
    book_img_temp_dir = tempfile.TemporaryDirectory()

    for category in CATEGORIES:
        print(category.upper())
        response = requests.get(f'{GB_BASE_API_URL}{category}')
        items = response.json()
        for item in items.get("items"):

            book_info = item.get("volumeInfo")

            # skip books without cover
            book_cover = book_info.get("imageLinks", None)
            if not book_cover:
                continue

            payload = create_payload(
                book_info,
                dup={
                    "category": category
                }
            )

            # create new book
            new_book_response = requests.post(
                f"{BASE_BOOKSTORE_API_URL}/books/",
                data=dumps(payload),
                headers = {
                    "Content-type": "application/json",
                    "Authorization": f"JWT {tokens['access']}",
                },
            )

            new_book_id = new_book_response.json().get("id", None)

            # add cover to new book
            cover = resolve_img(
                image_url=book_cover["thumbnail"],
                file_name=payload["title"],
                file_extension="jpeg",
                tmp_dir=book_img_temp_dir
            )

            response = requests.patch(
                f"{BASE_BOOKSTORE_API_URL}/books/{new_book_id}/",
                files={
                    "cover": (
                        cover["img-name"],
                        cover["content"],
                        cover["file-extension"]
                    )
                },
                headers = {
                    "Authorization": f"JWT {tokens['access']}",
                },
            )
            print(response.json())

    book_img_temp_dir.cleanup()
