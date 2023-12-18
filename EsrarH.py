import requests

print("""
███████╗░██████╗██████╗░░█████╗░██████╗░██╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
█████╗░░╚█████╗░██████╔╝███████║██████╔╝███████║
██╔══╝░░░╚═══██╗██╔══██╗██╔══██║██╔══██╗██╔══██║
███████╗██████╔╝██║░░██║██║░░██║██║░░██║██║░░██║
╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
""")

def shorten_url(long_url, custom_domain=None):
    api_url = "https://is.gd/create.php"
    
    params = {
        "format": "json",
        "url": long_url,
        "shorturl": custom_domain if custom_domain else "",
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "shorturl" in data:
            return data["shorturl"]
        else:
            return "Error!!!"
    else:
        return f"Error: {response.status_code} - {response.text}"

long_url = input("URL name: >>")
custom_domain = input("Give ur Url a name: >>")

short_url = shorten_url(long_url, custom_domain)
print(f"Ur URL :)): {short_url}")