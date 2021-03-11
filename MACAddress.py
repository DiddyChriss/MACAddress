import requests

class GetDataByMACAddress:

    def company_name(self, mac):                                # base authentication
        url = f'https://api.macaddress.io/v1?apiKey=at_t5hMN3yyEKRCwIc9lidP1jxVSBnuN&output=json&search={mac}'
        resp = requests.get(url, )
        if resp.status_code != 200:
            raise ValueError(f'GET /tasks/ {resp.status_code}')
        print(f"company name by MAC address ({mac}) is:  {resp.json()['vendorDetails']['companyName']}")

    def company_name_headers(self, mac, key):                   # header authentication
        headers = {'X-Authentication-Token': f'{key}'}
        url = f'https://api.macaddress.io/v1?output=json&search={mac}'
        resp = requests.get(url, headers=headers)

        if resp.status_code != 200:
            raise ValueError(f'GET /tasks/ {resp.status_code}')
        print(f"company name by MAC address ({mac}) is:  {resp.json()['vendorDetails']['companyName']}")


# a = GetDataByMACAddress()
# a.company_name_headers('44:38:39:ff:ef:57', 'at_t5hMN3yyEKRCwIc9lidP1jxVSBnuN')