import requests
import argparse
from datetime import datetime

def upload_reports(args):
    headers = {
    'accept': 'application/json',
    'Authorization': args.auth_token,
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
    'X-CSRFTOKEN': args.x_csrftoken,
    }

    files = {
    'product_type_name': (None, args.product_type_name),
    'active': (None, 'true'),
    'verified': (None, 'true'),
    'engagement_name': (None, args.engagement_name),
    'minimum_severity': (None, 'Info'),
    'scan_date': (None, args.scan_date),
    'product_name': (None, args.product_name),
    'file': open(args.file_name, 'rb'),
    'auto_create_context': (None, 'true'),
    'scan_type': (None, args.scan_type),
    }

    response = requests.post('http://34.100.188.93:8080/api/v2/reimport-scan/', headers=headers, files=files)
    print("Response from defectdojo server:", response.status_code)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auth_token", type=str, required=True)
    parser.add_argument("--x_csrftoken", type=str, required=True)
    parser.add_argument("--product_type_name", type=str, required=True)
    parser.add_argument("--engagement_name", type=str, required=True)
    parser.add_argument("--scan_date", type=str, required=True)
    parser.add_argument("--product_name", type=str, required=True)
    parser.add_argument("--file_name", type=str, required=True)
    parser.add_argument("--scan_type", type=str, required=True)

    args = parser.parse_args()
    upload_reports(args)
    