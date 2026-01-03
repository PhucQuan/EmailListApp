"""
Subdomain Enumeration Module
Uses crt.sh Certificate Transparency logs to discover subdomains
"""

import requests
import re


def get_subdomains(domain):
    """
    Enumerate subdomains using crt.sh API
    
    Args:
        domain (str): Target domain (e.g., 'example.com')
    
    Returns:
        list: List of discovered subdomains
    """
    url = f"https://crt.sh/?q={domain}&output=json"
    subdomains = set()
    
    try:
        print(f"[*] Querying crt.sh for {domain}...")
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            
            for item in data:
                name_value = item.get("name_value", "")
                
                # Split by newline (crt.sh sometimes returns multiple domains)
                for subdomain in name_value.split("\n"):
                    subdomain = subdomain.strip().lower()
                    
                    # Filter out wildcards and invalid entries
                    if "*" not in subdomain and subdomain:
                        subdomains.add(subdomain)
            
            print(f"[+] Found {len(subdomains)} unique subdomains")
            return sorted(list(subdomains))
        else:
            print(f"[-] Error: HTTP {response.status_code}")
            return []
            
    except requests.exceptions.Timeout:
        print("[-] Request timeout - crt.sh may be slow")
        return []
    except requests.exceptions.RequestException as e:
        print(f"[-] Request error: {e}")
        return []
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
        return []


if __name__ == "__main__":
    # Test the module
    test_domain = "tesla.com"
    results = get_subdomains(test_domain)
    print(f"\nSubdomains for {test_domain}:")
    for sub in results[:10]:  # Show first 10
        print(f"  - {sub}")
