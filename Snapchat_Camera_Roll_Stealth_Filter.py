import requests, config

def get_upload_URL():
    get_endpoint_URL = requests.get(url = config.snap_filter_endpoint, headers={"x-studio-auth-token":config.snap_studio_token, "User-Agent":config.snap_studio_version})
    if get_endpoint_URL.status_code == 200 :
        snap_filter_upload_URL = get_endpoint_URL.text
        return str(snap_filter_upload_URL)
    elif get_endpoint_URL.status_code == 403:
        raise Exception(f"The server returned an authorisation error. Check your x-studio-auth-token or consult the README.md for help.")
    else:
        raise Exception(f"An error occurred whilst getting the one-time upload URL. Response was: {get_endpoint_URL.status_code}. Consult the README.md for help.")

def upload_lens(response_URL):
    push_lens_headers = {"x-studio-auth-token":config.snap_studio_token, "User-Agent":config.snap_studio_version}
    with open('metadata', 'rb') as meta_file:
        file_bytes = meta_file.read()
        push_lens_metadata = file_bytes.decode()
        meta_file.close()
    with open('icon_file', 'rb') as image_file:
        file_bytes = image_file.read()
        push_lens_image = file_bytes.decode()
        image_file.close()
    push_lens_files = {
        'icon_file': (None, push_lens_image),
        'lens_resource': ("lens_resource.zip", open('lens_resource.zip', 'rb'), 'application/zip'),
        'metadata': (None, push_lens_metadata)
    }
    push_lens = requests.post(url = response_URL, files=push_lens_files, headers=push_lens_headers)
    if push_lens.status_code == 200 :
        print("Successfully pushed the lens to your snapchat. Check your device for a \"Your lens is ready to preview\" notification. You will need to re-run this every 24hr to keep the lens.")
    else:
        raise Exception(f"An error occurred whilst uploading the lens. Response was: {push_lens.status_code}. Consult the README.md for help.")

try:
    if not config.snap_filter_endpoint or not config.snap_studio_version or not config.snap_studio_token:
        raise Exception("There is a missing configuration value in the config.py file. Consult the README.md for help.")
    upload_URL = get_upload_URL()
    upload_lens(upload_URL)
    print("\r\nAll done. Remember, the \'development\' lens we just pushed has a 24hr expiry - you'll need to run this script again to acquire the lens again.")
except Exception as upload_failure:
    print(f"\r\n{upload_failure}.\r\nExiting.")





