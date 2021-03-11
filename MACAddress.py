import requests

class GetDataByMACAddress:

    def company_name(self, mac):
        url = f'https://api.macaddress.io/v1?apiKey=at_t5hMN3yyEKRCwIc9lidP1jxVSBnuN&output=json&search={mac}'
        resp = requests.get(url, )
        if resp.status_code != 200:
            raise ValueError(f'GET /tasks/ {resp.status_code}')
        print(f"company name by MAC address ({mac}) is:  {resp.json()['vendorDetails']['companyName']}")

