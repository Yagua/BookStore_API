import requests
from json import dumps
from random import uniform, randint

GB_BASE_API_URL = " https://www.googleapis.com/books/v1/volumes?maxResults=40&q=subject:"
OPTIONAL_SECTION = "&startIndex=%d"
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

# relevant information
# {
#   "items": [
#     {
#       "volumeInfo": {
#         "title": "",
#         "authors": [],
#         "description": "",
#         "publisher": "",
#         "categories": [],
#         "pageCount": 0,
#         "averageRating": 2,
#         "imageLinks": {
#           "thumbnail": ""
#         },
#         "language": "en"
#       },
#       "saleInfo": {
#         "listPrice": {
#           "amount": 34916,
#           "currencyCode": "COP"
#         }
#       }
#     }
#   ]
# }

# cut the url of cover thumbnail until '&img=x' to get full size image

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
      "cover": None
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
      "cover": None,
    }
    result = dumps(template)
    return result


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

    for category in CATEGORIES:
        print(category.upper())
        response = requests.get(f'{GB_BASE_API_URL}{category}')
        items = response.json()
        for item in items.get("items"):

            book_info = item.get("volumeInfo")

            payload = create_payload(
                book_info,
                dup={
                    "category": category
                }
            )
            bresponse = requests.post(
                f"{BASE_BOOKSTORE_API_URL}/books/",
                data=payload,
                headers = {
                    "Content-type": "application/json",
                    "Authorization": f"JWT {tokens['access']}",
                }
            )
            print(bresponse.json())
