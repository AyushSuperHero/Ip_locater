# ip_locator.py

import requests

def get_ip_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print(f"\n🔍 Details for IP: {ip}")
        print(f"📍 Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
        print(f"🌐 ISP: {data.get('org')}")
        print(f"📡 Coordinates: {data.get('loc')}")
        print(f"🕓 Timezone: {data.get('timezone')}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address (or leave blank for your own IP): ").strip()
    if not ip:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json().get("ip")
    get_ip_location(ip)
