#!/usr/bin/env python3

import json
import requests


def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse the response JSON
        data = response.json()
        
        # Extract joke components
        joke = f"{data['setup']}\n{data['punchline']}"
    except requests.exceptions.RequestException as e:
        print("Error fetching joke:", e)
        joke = 'No jokes'

    return joke

if __name__ == '__main__':
    print(get_joke())
