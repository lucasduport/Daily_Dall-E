def getCreds():
    creds = dict()
    creds['access_token'] = "xxxx"
    creds['client_id'] = "xxxx"
    creds['client_secret'] = "xxxx"
    creds['graph_domain'] = "https://graph.facebook.com/"
    creds['graph_version'] = "v16.0"
    creds['endpoint_base'] = creds["graph_domain"] + creds['graph_version'] + "/"
    creds['debug'] = 'no'
    creds['page_id'] = "xxxx"
    creds['instagram_business_account'] = "xxxx"
    creds['post_url'] = creds['endpoint_base'] + creds['instagram_business_account'] + "/media"
    creds['open_ai_key'] = "sk-xxxx"
    return creds