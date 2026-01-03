"""
DNS Information Module
Gather DNS records for reconnaissance
"""

import dns.resolver
import dns.exception


def get_dns_records(domain):
    """
    Query DNS records for a domain
    
    Args:
        domain (str): Target domain
    
    Returns:
        dict: Dictionary of DNS record types and their values
    """
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]
    dns_data = {}
    
    print(f"[*] Querying DNS records for {domain}...")
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            dns_data[record_type] = [str(rdata) for rdata in answers]
            print(f"[+] {record_type}: {len(dns_data[record_type])} records")
        except dns.resolver.NoAnswer:
            dns_data[record_type] = []
        except dns.resolver.NXDOMAIN:
            print(f"[-] Domain {domain} does not exist")
            dns_data[record_type] = []
            break
        except dns.resolver.Timeout:
            print(f"[-] DNS query timeout for {record_type}")
            dns_data[record_type] = []
        except dns.exception.DNSException as e:
            dns_data[record_type] = []
        except Exception as e:
            dns_data[record_type] = []
    
    return dns_data


def analyze_dns(dns_data):
    """
    Analyze DNS records for interesting findings
    
    Args:
        dns_data (dict): DNS records from get_dns_records()
    
    Returns:
        list: List of findings/observations
    """
    findings = []
    
    # Check for mail servers
    if dns_data.get("MX"):
        findings.append(f"Mail servers configured: {len(dns_data['MX'])}")
    
    # Check for SPF records
    txt_records = dns_data.get("TXT", [])
    spf_records = [r for r in txt_records if "v=spf1" in r]
    if spf_records:
        findings.append("SPF record found (email security)")
    
    # Check for DMARC
    dmarc_records = [r for r in txt_records if "v=DMARC1" in r]
    if dmarc_records:
        findings.append("DMARC record found (email security)")
    
    # Check for multiple A records (load balancing)
    if len(dns_data.get("A", [])) > 1:
        findings.append(f"Multiple A records ({len(dns_data['A'])}) - possible load balancing")
    
    # Check for IPv6 support
    if dns_data.get("AAAA"):
        findings.append("IPv6 supported")
    
    return findings


if __name__ == "__main__":
    # Test the module
    test_domain = "google.com"
    results = get_dns_records(test_domain)
    
    print(f"\nDNS Records for {test_domain}:")
    for record_type, values in results.items():
        if values:
            print(f"\n{record_type}:")
            for value in values[:3]:  # Show first 3
                print(f"  - {value}")
    
    print("\nAnalysis:")
    findings = analyze_dns(results)
    for finding in findings:
        print(f"  - {finding}")
