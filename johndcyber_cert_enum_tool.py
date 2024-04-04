import requests
import json
import logging
import os
import socket
from collections import Counter
import subprocess
import sys

def print_banner():
    banner = """
    ***************************************************
    * Johndcybers_cert_log_enumerator_tool                  *
    * A tool for enumerating SSL certificates         *
    ***************************************************
    """
    print(banner)

def setup_environment(domain):
    # Check and install required packages
    required_packages = ['requests']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    # Create domain directory
    domain_dir = domain.replace(".", "_")
    os.makedirs(domain_dir, exist_ok=True)
    logging.info(f"Directory {domain_dir} created.")

    # Setup logging
    logging.basicConfig(filename=os.path.join(domain_dir, 'domain_enumeration.log'), level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
    logging.info("SSL Cert Transparency Log Enumerator Initialized")

    return domain_dir

def query_crt(domain):
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            records = json.loads(response.text)
            return {record['name_value'].strip() for record in records if 'name_value' in record}
    except Exception as e:
        logging.error(f"Error querying crt.sh: {e}")
    return set()

def check_http_statuses(subdomains, domain_dir):
    status_counter = Counter()
    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}", timeout=5)
            status_counter[response.status_code] += 1
            with open(os.path.join(domain_dir, f"{response.status_code}_responses.txt"), "a") as file:
                file.write(subdomain + "\n")
        except requests.RequestException as e:
            logging.error(f"Failed to check {subdomain}: {e}")
            status_counter['errors'] += 1
    return status_counter

def reverse_dns_lookup(domains, domain_dir):
    with open(os.path.join(domain_dir, "ip.txt"), "w") as ip_file:
        for domain in domains:
            try:
                ip_address = socket.gethostbyname(domain)
                ip_file.write(f"{ip_address}\n")  # Only write the IP address
            except socket.gaierror as e:
                logging.error(f"Failed to resolve {domain}: {e}")

if __name__ == "__main__":
    print_banner()
    domain = input("Enter the domain you want to enumerate (without 'https://'): ")
    domain_dir = setup_environment(domain)

    subdomains = query_crt(domain)
    if not subdomains:
        logging.info("No subdomains found.")
        print("No subdomains found.")
        sys.exit()

    status_counter = check_http_statuses(subdomains, domain_dir)
    unique_domains = sorted(subdomains)

    # Writing all unique domains to a file
    with open(os.path.join(domain_dir, "unique_domains.txt"), "w") as f:
        for domain in unique_domains:
            f.write(f"{domain}\n")

    # Perform reverse DNS lookup on domains that returned a 200 OK status
    if 200 in status_counter:
        domains_200 = [domain.strip() for domain in open(os.path.join(domain_dir, "200_responses.txt")).readlines()]
        reverse_dns_lookup(domains_200, domain_dir)

    # Log summary
    logging.info(f"Total unique domains: {len(unique_domains)}")
    for status, count in status_counter.items():
        logging.info(f"HTTP {status}: {count} subdomains")
    print("Script execution completed. Check the domain directory for details and logs.")
