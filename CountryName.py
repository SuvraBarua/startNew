import urllib.request
import urllib.error
import json
from urllib.parse import quote

def get_country_info(country_name):
    encoded_name = quote(country_name)
    url = f"https://countries.dev/name/{encoded_name}"

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

            if not isinstance(data, list) or len(data) == 0:
                print("No country found.")
                return None

            # 1. Try to find exact match (case-insensitive)
            for country in data:
                if country.get("name", "").lower() == country_name.lower():
                    return country

            # 2. No exact match → show options
            print(f"\nFound {len(data)} possible matches:")
            for i, country in enumerate(data, start=1):
                print(f"{i}. {country.get('name')} ({country.get('alpha2Code')})")

            choice = input("\nEnter the number of the country you want: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(data):
                    return data[index]
                else:
                    print("Invalid choice.")
                    return None
            except ValueError:
                print("Please enter a number.")
                return None

    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
    except Exception as e:
        print("Error:", e)

    return None


# ========== Main program ==========
name = input("Enter country name: ").strip()
country = get_country_info(name)

if country:
    print("\n=== Country Information ===")
    print(f"Name       : {country.get('name')}")
    print(f"Capital    : {country.get('capital')}")
    print(f"Region     : {country.get('region')}")
    print(f"Population : {country.get('population'):,}")
    print(f"Languages  : {[lang['name'] for lang in country.get('languages', [])]}")
    print(f"Flag       : {country.get('flag')}")
