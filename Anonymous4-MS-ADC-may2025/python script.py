from shaext import shaext
import requests

# Challenge values
origtext = "count=2&lat=42.39561&user_id=2&long=-71.13051&waffle=dream"
origsig = "57e3056c2c4f0d7812db0ab0eaf81ba4b2baee66"
keylen = 14
addtext = "&waffle=liege"

# Perform SHA1 length extension attack
ext = shaext(origtext, keylen, origsig)
ext.add(addtext)
data, sig = ext.final()  # data is bytes, sig is hex string

# Forge the full raw request payload
# Add the |sig:<sig> part as bytes
payload = data + b"|sig:" + sig.encode()
print(payload)
# Send the payload to the API
url = "http://ctf.uksouth.cloudapp.azure.com:9233/orders"
headers = {
    "Content-Type": "text/plain"
}

res = requests.post(url, data=payload, headers=headers)

# Output the result
print("[+] Raw Payload Sent (truncated):")
print(payload[:120] + b"...")  # print first part to avoid long garbage

print("\n[+] Server Response:")
print(res.text)
