import requests
import json

def getCreds():
    creds = dict()
    creds['access_token'] = "EAAIPNfWMUEYBALmQHZAYo7AjtIer2GCeg7J3ZAi7jJnUsGb82yuRF4LYqTeAZAQdmFae67aLML80edFs9LglWWXSXwBUCtRqqUHcysExBgUpCVkL6abPHyqKwfCmLByWzxMt2UAJa4oHcZBvZA5Q0KVOSD3ooeeZCvuPIRpv6gG6ABichhWZAQBTScbwi4u0uAvxikCXF4PMZAaFXwiwOaaycfRLMzZB889gZD"
    creds['client_id'] = "579674380718150"
    creds['client_secret'] = "d6bbea1040aeb7c6d2ead66b88c87f66"
    creds['graph_domain'] = "https://graph.facebook.com/"
    creds['graph_version'] = "v16.0"
    creds['endpoint_base'] = creds["graph_domain"] + creds['graph_version'] + "/"
    creds['debug'] = 'no'
    creds['page_id'] = "116913587984678"
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