"""
Retrives orders from authorized site via Printful API
Printful API Docs: https://www.printful.com/docs/index
"""
import requests
import base64
from configparser import ConfigParser

def main():
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0"
    api_key_bytes = API_KEY.encode('ascii')
    api_key_enc = base64.b64encode(api_key_bytes).decode('ascii')
    api_func = 'orders'
    headers = {'user-agent': f'{user_agent}',
                'Authorization': f'Basic {api_key_enc}'}
    print(headers)
    api_data = requests.get(API_URL+api_func, headers=headers)

    print(api_data.text)

if __name__ == '__main__':
    config = ConfigParser()
    config.read('config/config.ini')

    if config.get('config', 'token') == 'false':
        print("<ERROR> You must enter your API key under the token field in config.ini")
        exit() 
    else:
        API_KEY = config.get('config', 'token')

    API_URL = "https://api.printful.com/"
    main()