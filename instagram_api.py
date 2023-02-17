import requests
import json

def getCreds():
    creds = dict()
    creds['access_token'] = "xxxxxxxxxxxxxxxxxx"
    creds['client_id'] = "xxxxxxxxxxxxxxxxxxxxxxx"
    creds['client_secret'] = "xxxxxxxxxxxxxxxxxxxxxxx"
    creds['graph_domain'] = "https://graph.facebook.com/"
    creds['graph_version'] = "v16.0"
    creds['endpoint_base'] = creds["graph_domain"] + creds['graph_version'] + "/"
    creds['page_id'] = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
    creds['instagram_business_account'] = "17841458001179434"
    creds['post_url'] = creds['endpoint_base'] + creds['instagram_business_account'] + "/media"
    return creds

def getPostUrl():
    return getCreds()['post_url']

def getAccessToken():
    return getCreds()['access_token']

def getInstagramID():
    return getCreds()['instagram_business_account']

def getFacebookPageID():
    return getCreds()['page_id']

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
        return
    
    creation_id = result["id"]
    print("Creation ID: " + creation_id)

    second_request_url = getPostUrl() + "_publish"
    second_payload = payload_two_creator(creation_id)
    r = requests.post(second_request_url, data=second_payload)

    print("Image posted successfully.")
