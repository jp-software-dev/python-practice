import requests

def shorter_url():
    long_url = input("Enter the full link you want to shorten (include http:// or https://):").strip()

    try:
        print("\nProcessing... ")

        api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
        response = requests.get(api_url)

        if response.status_code == 200:
            shorter_url = response.text
            print("\n¡Success! Here is your shortened link:")
            print(f"{shorter_url}\n")
        else:
            print(f"\nError: The server returned status code {response.status_code}")

    except Exception as e:
        print("\nAn error occurred while trying to shorten the link.")
        print("Make sure the URL is correct and you have an active internet connection.")
        print(f"Technical detail: {e}") 

if __name__ == "__main__":
    shorter_url()