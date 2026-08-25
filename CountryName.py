import urllib.request
import urllib.error
import json
from urllib.parse import quote

def get_country_info(country_name):
    encoded_name = quote(country_name)
    url = f"https://countries.dev/name/{encoded_name}"

    # Create a request and add a User-Agent header
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    )

    print(f"Requesting: {url}")

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

            if isinstance(data, list) and len(data) > 0:
                return data[0]
            else:
                print("No country found")
                return None

    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
    except json.JSONDecodeError:
        print("Invalid JSON received")
    except Exception as e:
        print("Unexpected error:", e)

    return None


# Test
country = get_country_info("Bangladesh")

if country:
    print("\n=== Country Information ===")
    print(f"Name       : {country.get('name')}")
    print(f"Capital    : {country.get('capital')}")
    print(f"Region     : {country.get('region')}")
    print(f"Population : {country.get('population'):,}")
    print(f"Languages  : {[lang['name'] for lang in country.get('languages', [])]}")
    print(f"Flag       : {country.get('flag')}")
