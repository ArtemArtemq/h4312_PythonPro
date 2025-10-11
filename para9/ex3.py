import requests

response = requests.post("http://httpbin.org/post",
                         data="Test data",
                         headers={"h1": "Test title for Artem"})

print(response.text)