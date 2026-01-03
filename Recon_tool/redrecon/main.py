"""
RedRecon-Lite - Lightweight Reconnaissance Tool
Main CLI interface for running reconnaissance scans

Author: Your Name
Version: 1.0.0
"""

import argparse
import json
import sys
from datetime import datetime

# Import core modules
from core.subdomain import get_subdomains
from core.portscan import port_scan, get_service_name
from core.dnsinfo import get_dns_records, analyze_dns
from core.techstack import fingerprint
from core.dirscan import dir_scan, categorize_findings


def print_banner():
    """Print tool banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║           RedRecon-Lite v1.0.0                       ║
    ║     Lightweight Reconnaissance Tool                   ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)


def print_section(title):
    """Print section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def scan_target(domain, limit_subdomains=20):
    """
    Run full reconnaissance scan on target domain
    
    Args:
        domain (str): Target domain
        limit_subdomains (int): Maximum subdomains to scan
    
    Returns:
        dict: Complete scan results
    """
    results = {
        "domain": domain,
        "scan_time": datetime.now().isoformat(),
        "subdomains": [],
        "hosts": {}
    }
    
    # Step 1: Subdomain Enumeration
    print_section("SUBDOMAIN ENUMERATION")
    subdomains = get_subdomains(domain)
    results["subdomains"] = subdomains
    
    if not subdomains:
        print(f"[-] No subdomains found for {domain}")
        print(f"[*] Scanning main domain only...")
        subdomains = [domain]
    else:
        print(f"[+] Total subdomains found: {len(subdomains)}")
        
        # Limit number of subdomains to scan
        if len(subdomains) > limit_subdomains:
            print(f"[*] Limiting scan to first {limit_subdomains} subdomains")
            subdomains = subdomains[:limit_subdomains]
    
    # Step 2-5: Scan each subdomain
    for idx, subdomain in enumerate(subdomains, 1):
        print_section(f"SCANNING {subdomain} ({idx}/{len(subdomains)})")
        
        host_data = {
            "subdomain": subdomain,
            "ports": [],
            "dns": {},
            "technologies": {},
            "directories": []
        }
        
        # Port Scan
        print(f"\n[*] Port Scanning...")
        open_ports = port_scan(subdomain)
        host_data["ports"] = [
            {"port": port, "service": get_service_name(port)} 
            for port in open_ports
        ]
        
        # DNS Records
        print(f"\n[*] DNS Lookup...")
        dns_records = get_dns_records(subdomain)
        host_data["dns"] = dns_records
        
        # DNS Analysis
        dns_findings = analyze_dns(dns_records)
        if dns_findings:
            print(f"[+] DNS Findings:")
            for finding in dns_findings:
                print(f"    - {finding}")
        
        # Technology Fingerprinting (only if web ports are open)
        if any(port in open_ports for port in [80, 443, 8080, 8443]):
            print(f"\n[*] Technology Fingerprinting...")
            tech_info = fingerprint(subdomain)
            host_data["technologies"] = tech_info
        else:
            print(f"[-] No web ports open, skipping tech fingerprinting")
        
        # Directory Fuzzing (only if web ports are open)
        if any(port in open_ports for port in [80, 443, 8080, 8443]):
            print(f"\n[*] Directory Fuzzing...")
            discovered_dirs = dir_scan(subdomain)
            host_data["directories"] = discovered_dirs
            
            # Categorize findings
            if discovered_dirs:
                categories = categorize_findings(discovered_dirs)
                print(f"\n[+] Risk Summary:")
                for level, items in categories.items():
                    if items:
                        print(f"    {level.upper()}: {len(items)} findings")
        else:
            print(f"[-] No web ports open, skipping directory scan")
        
        results["hosts"][subdomain] = host_data
    
    return results


def save_results(results, output_file):
    """
    Save results to JSON file
    
    Args:
        results (dict): Scan results
        output_file (str): Output file path
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n[+] Results saved to: {output_file}")
    except Exception as e:
        print(f"[-] Error saving results: {e}")


def print_summary(results):
    """
    Print scan summary
    
    Args:
        results (dict): Scan results
    """
    print_section("SCAN SUMMARY")
    
    print(f"Target Domain: {results['domain']}")
    print(f"Scan Time: {results['scan_time']}")
    print(f"Subdomains Found: {len(results['subdomains'])}")
    print(f"Hosts Scanned: {len(results['hosts'])}")
    
    # Count total findings
    total_ports = sum(len(host['ports']) for host in results['hosts'].values())
    total_dirs = sum(len(host['directories']) for host in results['hosts'].values())
    
    print(f"Total Open Ports: {total_ports}")
    print(f"Total Directories Found: {total_dirs}")
    
    print("\n" + "="*60)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="RedRecon-Lite - Lightweight Reconnaissance Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --domain example.com
  python main.py --domain example.com --output report.json
  python main.py --domain example.com --limit 10

Legal Notice:
  Only scan domains you have permission to test.
  Unauthorized scanning may be illegal in your jurisdiction.
        """
    )
    
    parser.add_argument(
        "--domain", 
        required=True, 
        help="Target domain to scan (e.g., example.com)"
    )
    
    parser.add_argument(
        "--output", 
        default="report.json",
        help="Output file for results (default: report.json)"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of subdomains to scan (default: 20)"
    )
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    print(f"[*] Target: {args.domain}")
    print(f"[*] Output: {args.output}")
    print(f"[*] Subdomain Limit: {args.limit}")
    print(f"\n[!] Legal Notice: Only scan domains you have permission to test.")
    
    try:
        # Run scan
        results = scan_target(args.domain, limit_subdomains=args.limit)
        
        # Save results
        save_results(results, args.output)
        
        # Print summary
        print_summary(results)
        
        print(f"\n[+] Scan completed successfully!")
        
    except KeyboardInterrupt:
        print(f"\n\n[-] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] Error during scan: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
