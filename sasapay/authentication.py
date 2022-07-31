import json
import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

def get_client_token():
    client_id= settings.CLIENT_ID
    client_secret= settings.CLIENT_SECRET
    token_url= settings.TOKEN_URL
    response= requests.get(
        token_url,
        auth=HTTPBasicAuth(client_id,client_secret),
        params={"grant_type":"client_credentials"}
    )
    response= json.loads(response.text)
    return response