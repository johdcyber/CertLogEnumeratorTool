# Johndcyber's Cert Log Enumerator Tool

## Description

Johndcyber Cert Log Enumerator is a Python-based tool designed to aid security researchers, network administrators, and SSL certificate enthusiasts in enumerating SSL certificates for a specified domain via crt.sh. This script simplifies SSL exploration, providing detailed insights into subdomain structures, HTTP status codes, and IP addresses, thereby facilitating a deeper understanding of a domain's SSL certificate landscape.

## Why Johndcyber Cert Log Enumerator?

This tool stands out for its:
- Precision in **subdomain enumeration**.
- **HTTP status insights** for quick web presence evaluation.
- **IP resolution** through reverse DNS lookups.
- **Organized reporting** for clarity and ease of analysis.
- **Ease of use**, making it accessible for both novices and seasoned professionals.

It serves as a valuable asset for those looking to conduct thorough SSL certificate reconnaissance, saving time in the reconnaissance phase and assisting in URL validation.

## How It Works

The Johndcyber Cert Log Enumerator operates in several steps:
1. **Subdomain Enumeration:** Queries crt.sh for any subdomains associated with the entered domain, utilizing crt.sh's comprehensive database of SSL certificates.
2. **HTTP Status Checks:** For each subdomain found, the script attempts to access it over HTTP and records the HTTP status code of the response, which helps in identifying live URLs and their responsiveness.
3. **Reverse DNS Lookup:** For all subdomains returning a 200 OK status, the script performs a reverse DNS lookup, resolving the domain names back to their IP addresses, which are then logged.
4. **Organized Reporting:** All findings are neatly categorized into files within a directory named after the domain, ensuring organized access to the data collected.

### Basic Execution

1. **Open your terminal:** Navigate to the directory where the script is located.

2. **Run the script:** Execute the script by typing the following command and pressing Enter:

    ```bash
    python johndcyber_cert_log_enumerator.py
    ```

3. **Enter the domain name:** When prompted, input the domain you wish to enumerate (omit 'https://'). For example:

    ```
    Enter the domain you want to enumerate (without 'https://'): example.com
    ```

The script will then proceed to query crt.sh for subdomains, check their HTTP statuses, perform reverse DNS lookups where applicable, and organize the findings into respective files within a directory named after the domain.



## Outputs Explained

- `unique_domains.txt`: Lists all unique subdomains discovered during the enumeration process.
- `<status_code>_responses.txt`: Contains subdomains categorized by their HTTP response status codes, aiding in the quick identification of various HTTP statuses across subdomains.
- `ip.txt`: Stores IP addresses resolved from subdomains that successfully responded with a 200 OK status, facilitating network mapping and analysis.
- `domain_enumeration.log`: Detailed log file capturing the script's operations, useful for auditing and troubleshooting.
- `errors.txt`: Logs errors encountered during execution, particularly useful for identifying subdomains that could not be resolved or accessed.

## For Security Professionals

Johndcyber Cert Log Enumerator is an invaluable tool for security professionals engaged in reconnaissance and validation tasks. By automating the tedious process of SSL certificate enumeration and subdomain discovery, it significantly reduces the time and effort involved in these initial stages of security assessment. Additionally, by providing insights into the live status of subdomains and mapping their IP addresses, it aids in identifying potential targets for further security testing and vulnerability assessment.

## Future Development

While Johndcyber Cert Log Enumerator already provides a robust set of features, future enhancements are planned to include:
- Integration with additional SSL/TLS certificate sources for broader enumeration.
- Enhanced error handling and retry mechanisms for more resilient domain checking.
- Expansion of reporting capabilities to include more detailed analytics on the SSL/TLS landscape of enumerated domains.

## Contributions

Contributions, feedback, and feature suggestions are warmly welcomed. Feel free to fork the repository, open issues for any bugs encountered or improvements envisioned, and submit pull requests with your enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

