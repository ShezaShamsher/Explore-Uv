import requests 

def main():
    response = requests.get("https://fakestoreapi.com/products/1")
    print(response.json())

if __name__ == "__main__":
    main()
