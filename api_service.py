import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

    except requests.exceptions.Timeout:
        print("Request Timed Out.")

    except requests.exceptions.HTTPError:
        print("HTTP Error.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return []