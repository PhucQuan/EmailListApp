"""
Technology Stack Fingerprinting Module
Identify web technologies, frameworks, and services
"""

import requests
import re
from urllib.parse import urlparse


def fingerprint_wappalyzer(domain):
    """
    Use Wappalyzer unofficial API for tech detection
    
    Args:
        domain (str): Target domain
    
    Returns:
        dict: Detected technologies
    """
    # Ensure domain has protocol
    if not domain.startswith(('http://', 'https://')):
        domain = f"https://{domain}"
    
    try:
        url = f"https://api.wappalyzer.com/lookup/v2/?urls={domain}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {}
    except Exception:
        return {}


def fingerprint_headers(domain):
    """
    Analyze HTTP headers for technology detection
    
    Args:
        domain (str): Target domain
    
    Returns:
        dict: Detected technologies from headers
    """
    # Ensure domain has protocol
    if not domain.startswith(('http://', 'https://')):
        test_url = f"https://{domain}"
    else:
        test_url = domain
    
    tech_info = {
        "server": None,
        "powered_by": None,
        "framework": None,
        "technologies": []
    }
    
    try:
        print(f"[*] Analyzing HTTP headers for {domain}...")
        response = requests.get(test_url, timeout=10, allow_redirects=True)
        headers = response.headers
        
        # Server header
        if "Server" in headers:
            tech_info["server"] = headers["Server"]
            tech_info["technologies"].append(f"Server: {headers['Server']}")
        
        # X-Powered-By header
        if "X-Powered-By" in headers:
            tech_info["powered_by"] = headers["X-Powered-By"]
            tech_info["technologies"].append(f"Powered-By: {headers['X-Powered-By']}")
        
        # Framework detection from headers
        framework_headers = {
            "X-AspNet-Version": "ASP.NET",
            "X-AspNetMvc-Version": "ASP.NET MVC",
            "X-Drupal-Cache": "Drupal",
            "X-Generator": "Generator",
        }
        
        for header, framework in framework_headers.items():
            if header in headers:
                tech_info["framework"] = framework
                tech_info["technologies"].append(f"{framework}: {headers[header]}")
        
        # Content analysis
        content = response.text[:5000]  # First 5KB
        
        # WordPress detection
        if "wp-content" in content or "wp-includes" in content:
            tech_info["technologies"].append("WordPress")
        
        # React detection
        if "react" in content.lower() or "__REACT" in content:
            tech_info["technologies"].append("React")
        
        # Vue.js detection
        if "vue" in content.lower() or "data-v-" in content:
            tech_info["technologies"].append("Vue.js")
        
        # jQuery detection
        if "jquery" in content.lower():
            tech_info["technologies"].append("jQuery")
        
        # Bootstrap detection
        if "bootstrap" in content.lower():
            tech_info["technologies"].append("Bootstrap")
        
        # Cloudflare detection
        if "cloudflare" in headers.get("Server", "").lower() or "cf-ray" in headers:
            tech_info["technologies"].append("Cloudflare CDN")
        
        print(f"[+] Found {len(tech_info['technologies'])} technologies")
        
    except requests.exceptions.SSLError:
        print(f"[-] SSL error - trying HTTP...")
        try:
            test_url = f"http://{domain.replace('https://', '').replace('http://', '')}"
            response = requests.get(test_url, timeout=10, allow_redirects=True)
            if "Server" in response.headers:
                tech_info["server"] = response.headers["Server"]
                tech_info["technologies"].append(f"Server: {response.headers['Server']}")
        except:
            pass
    except requests.exceptions.Timeout:
        print(f"[-] Request timeout")
    except Exception as e:
        print(f"[-] Error: {e}")
    
    return tech_info


def fingerprint(domain):
    """
    Main fingerprinting function combining multiple methods
    
    Args:
        domain (str): Target domain
    
    Returns:
        dict: Combined technology detection results
    """
    results = {
        "domain": domain,
        "technologies": [],
        "server": None,
        "framework": None
    }
    
    # Try header-based detection (more reliable and free)
    header_results = fingerprint_headers(domain)
    
    if header_results:
        results["server"] = header_results.get("server")
        results["framework"] = header_results.get("framework")
        results["technologies"] = header_results.get("technologies", [])
    
    # Optionally try Wappalyzer (may have rate limits)
    # wap_results = fingerprint_wappalyzer(domain)
    # if wap_results:
    #     results["wappalyzer"] = wap_results
    
    return results


if __name__ == "__main__":
    # Test the module
    test_domain = "github.com"
    results = fingerprint(test_domain)
    
    print(f"\nTechnology Stack for {test_domain}:")
    print(f"Server: {results.get('server', 'Unknown')}")
    print(f"Framework: {results.get('framework', 'Unknown')}")
    print(f"\nDetected Technologies:")
    for tech in results.get("technologies", []):
        print(f"  - {tech}")
