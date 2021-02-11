import requests 
import json
import os

from dotenv import load_dotenv, find_dotenv

# Load and get environment variables
load_dotenv(find_dotenv())

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

access_token = ACCESS_TOKEN


httpHeaders = {"Content-type": "application/json",
           "Authorization": "Bearer " + access_token}


def post_message(room_id, text):
   
    """
    This function will post a message to the
    room based on provided room ID
    """
    string=''
    message=string.join(text)
    apiUrl = "https://webexapis.com/v1/messages"
    body = {"roomId": room_id, "text": message}

    response = requests.post(url=apiUrl, json=body, headers=httpHeaders) 

    if response.status_code == 200:
        print("Your message was successfully posted to the room")
    else:
        print("Something went wrong.\n"
              "Please check the script and run it again!")
        exit()

def main():

    """
    Main function
    """
    print()
    #post_message()


if __name__ == "__main__":
    main()
