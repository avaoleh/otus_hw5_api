import requests
from requests import Response


def test_addition(actual, expected):
    response: Response = requests.get(actual)
    assert response.status_code == expected
