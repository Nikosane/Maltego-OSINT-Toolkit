import requests
import sys
from maltego_trx.entities import Domain, Website
from maltego_trx.maltego import MaltegoTransform

# Replace 'YOUR_API_KEY' with your actual VirusTotal API key
API_KEY = "YOUR_API_KEY"
VT_API_URL = "https://www.virustotal.com/api/v3/domains/"

class VirusTotalDomainTransform(MaltegoTransform):
    def __init__(self):
        super().__init__()

    def do_transform(self, request, response):
        # Extract domain from the Maltego request
        domain = request.Value
        print(f"Querying VirusTotal for domain: {domain}")
        
        # Make an API request to VirusTotal
        headers = {"x-apikey": API_KEY}
        vt_response = requests.get(VT_API_URL + domain, headers=headers)

        if vt_response.status_code == 200:
            data = vt_response.json()
            # Add a Website entity for the domain
            response.addEntity(Website, f"https://{domain}")

            # Add information about detected categories, if available
            categories = data.get("data", {}).get("attributes", {}).get("categories", {})
            for key, value in categories.items():
                response.addEntity("maltego.Phrase", f"Category: {value} ({key})")

            # Add information about popularity rank
            rank = data.get("data", {}).get("attributes", {}).get("popularity_ranks", {})
            for source, rank_info in rank.items():
                rank_value = rank_info.get("rank")
                response.addEntity("maltego.Phrase", f"Rank ({source}): {rank_value}")
        else:
            response.addUIMessage(f"Failed to fetch data from VirusTotal: {vt_response.status_code}", "PartialError")

        return response

if __name__ == "__main__":
    VirusTotalDomainTransform().run(sys.argv)

