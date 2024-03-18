import argparse
import requests
from colorama import init, Fore
from art import text2art

def display_logo():
    logo_art = text2art("TextLocal", font='small')
    print(Fore.GREEN + logo_art)

def display_usage():
    usage = """
    Usage:
    python script_name.py your_api_key
    """
    print(Fore.RED + usage)

def check_textlocal_account(api_key):
    url = 'https://api.textlocal.in/balance/'
    params = {'apiKey': api_key}

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'errors' in data:
            error_message = data['errors'][0]['message']
            print(Fore.RED + f"Failed to fetch account information: {error_message}")
        else:
            print("Account information:")
            if 'balance' in data:
                print(f"SMS balance: {data['balance'].get('sms', 'N/A')}")
            else:
                print("SMS balance information not available")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama
    display_logo()

    parser = argparse.ArgumentParser(description="TextLocal Account Checker")
    parser.add_argument("api_key", help="Your TextLocal API key")
    args = parser.parse_args()

    if args.api_key:
        check_textlocal_account(args.api_key)
    else:
        display_usage()
