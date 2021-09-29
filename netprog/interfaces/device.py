import json
import requests
import urllib3
from django.conf import settings

urllib3.disable_warnings()


def set_interface(
    interface,
    enabled,
    hostname=settings.DEVICE_HOST,
    username=settings.DEVICE_USERNAME,
    password=settings.DEVICE_PASSWORD,
):
    url = f"https://{hostname}/restconf/data/ietf-interfaces:interfaces"
    headers = headers = {
        "Accept": "application/yang-data+json",
        "Content-type": "application/yang-data+json",
    }
    payload = {
        "ietf-interfaces:interfaces": {
            "interface": {"name": interface, "enabled": enabled}
        }
    }
    try:
        response = requests.request(
            "PATCH",
            url,
            data=json.dumps(payload),
            headers=headers,
            auth=(username, password),
            verify=False,
        )

    except Exception as err:
        print(f"There was an error setting interface '{interface}': {err}")


def get_interfaces(
    hostname=settings.DEVICE_HOST,
    username=settings.DEVICE_USERNAME,
    password=settings.DEVICE_PASSWORD,
):
    interfaces = []
    url = f"https://{hostname}/restconf/data/ietf-interfaces:interfaces/interface"

    headers = headers = {"Accept": "application/yang-data+json"}
    try:
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=(username, password),
            verify=False,
        )

        if response.ok:
            interfaces = response.json().get("ietf-interfaces:interface", [])

    except Exception as err:
        print(f"There was an error getting interfaces: {err}")

    return interfaces


if __name__ == "__main__":
    print(get_interfaces())
