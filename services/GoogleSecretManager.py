import base64


def get_secret_from_secret_manager(client, secret_id, decode="UTF-8", project_id='742741961768', version_id=1):
    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": secret_name})
    if decode == "UTF-8":
        value = response.payload.data.decode("UTF-8")
    else:
        value = base64.b64decode(response.payload.data.decode("UTF-8"))
    return value
