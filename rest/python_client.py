import requests


def add_numbers(a, b):
    url = 'http://localhost:5000/add'
    payload = {'num1': a, 'num2': b}
    try:
        response = requests.get(url, params=payload)
        result = response.json()
        return result['result']
    except requests.exceptions.RequestException as e:
        print("Error: ", e)


if __name__ == '__main__':
    result = add_numbers(5, 3)
    print(result)
