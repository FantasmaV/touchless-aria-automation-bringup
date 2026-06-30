"""
Aria Automation ABX example: reserve the next available IP address from phpIPAM.

All values are examples. Use Aria secrets or an enterprise secrets manager for tokens.
"""

import os
import requests


PHPIPAM_URL = os.getenv("PHPIPAM_URL", "https://phpipam.example.local/api/aria")
PHPIPAM_TOKEN = os.getenv("PHPIPAM_TOKEN", "REDACTED_TOKEN")


def handler(context, inputs):
    subnet_id = inputs.get("subnet_id", "101")
    hostname = inputs.get("hostname", "vks-demo-01")
    description = inputs.get("description", "Reserved by Aria Automation ABX")

    headers = {
        "token": PHPIPAM_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "hostname": hostname,
        "description": description,
        "owner": inputs.get("requester", "platform-team"),
        "note": "Touchless VCF automation reference example"
    }

    url = f"{PHPIPAM_URL}/addresses/first_free/{subnet_id}/"
    response = requests.post(url, headers=headers, json=payload, timeout=30, verify=True)
    response.raise_for_status()

    data = response.json()

    return {
        "hostname": hostname,
        "ip_address": data.get("data"),
        "subnet_id": subnet_id,
        "source": "phpIPAM"
    }
