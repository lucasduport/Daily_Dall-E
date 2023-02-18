import requests
import json
import creds

def getLongLivedToken():
    url = "https://graph.facebook.com/v16.0/oauth/access_token?"
    url += "grant_type=fb_exchange_token&client_id=" + creds.getCreds()['client_id'] + "&client_secret=" + creds.getCreds()['client_secret'] + "&fb_exchange_token=" + getAccessToken()
    print(url)

def getPostUrl():
    return creds.getCreds()['post_url']

def getAccessToken():
    return creds.getCreds()['access_token']

def getInstagramID():
    return creds.getCreds()['instagram_business_account']

def getFacebookPageID():
    return creds.getCreds()['page_id']

def payload_one_creator(image_url, caption):
    payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": getAccessToken()
    }
    return payload

def payload_two_creator(creation_id):
    payload = {
        "creation_id": creation_id,
        "access_token": getAccessToken()
    }
    return payload


def postImage(image_url, caption):
    r = requests.post(getPostUrl(), data=payload_one_creator(image_url, caption))
    result = json.loads(r.text)
    if not "id" in result:
        print("There was an error posting the image.")
        print("Result : " + str(result))
        return
    
    creation_id = result["id"]
    print("Creation ID: " + creation_id)

    second_request_url = getPostUrl() + "_publish"
    second_payload = payload_two_creator(creation_id)
    r = requests.post(second_request_url, data=second_payload)

    print("Image posted successfully.")

#print(getLongLivedToken(getAccessToken(), getCreds()['client_id'], getCreds()['client_secret']))