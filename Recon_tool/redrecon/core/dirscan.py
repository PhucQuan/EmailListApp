"""
Directory Fuzzing Module
Discover exposed directories and files
"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


# Common directories and files to check
WORDLIST = [
    # Admin panels
    "admin",
    "administrator",
    "admin.php",
    "admin/login",
    "wp-admin",
    
    # Login pages
    "login",
    "signin",
    "auth",
    "login.php",
    
    # Backup files
    "backup",
    "backups",
    "backup.zip",
    "backup.sql",
    "db.sql",
    
    # Config files
    "config",
    "config.php",
    ".env",
    "settings",
    
    # Upload directories
    "uploads",
    "upload",
    "files",
    "media",
    
    # API endpoints
    "api",
    "api/v1",
    "api/v2",
    "graphql",
    
    # Development files
    "test",
    "dev",
    "debug",
    "phpinfo.php",
    
    # Version control
    ".git",
    ".svn",
    ".git/config",
    
    # Common files
    "robots.txt",
    "sitemap.xml",
    ".htaccess",
    "web.config",
]


def check_path(domain, path, timeout=4):
    """
    Check if a path exists on the domain
    
    Args:
        domain (str): Target domain
        path (str): Path to check
        timeout (int): Request timeout
    
    Returns:
        dict or None: Path info if found, None otherwise
    """
    # Try HTTPS first
    for protocol in ["https", "http"]:
        url = f"{protocol}://{domain}/{path}"
        
        try:
            response = requests.get(
                url, 
                timeout=timeout, 
                allow_redirects=False,
                verify=False  # Ignore SSL warnings
            )
            
            # Consider these status codes as "found"
            if response.status_code in [200, 201, 301, 302, 401, 403]:
                return {
                    "url": url,
                    "status": response.status_code,
                    "size": len(response.content),
                    "path": path
                }
        except requests.exceptions.SSLError:
            # Try HTTP if HTTPS fails
            continue
        except requests.exceptions.Timeout:
            return None
        except requests.exceptions.RequestException:
            return None
        except Exception:
            return None
    
    return None


def dir_scan(domain, wordlist=None, max_workers=10):
    """
    Scan for exposed directories and files
    
    Args:
        domain (str): Target domain
        wordlist (list): Custom wordlist (default: WORDLIST)
        max_workers (int): Number of concurrent requests
    
    Returns:
        list: List of discovered paths
    """
    if wordlist is None:
        wordlist = WORDLIST
    
    # Remove protocol if present
    domain = domain.replace("https://", "").replace("http://", "")
    
    discovered = []
    
    print(f"[*] Scanning {len(wordlist)} paths on {domain}...")
    
    # Disable SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all path checks
        future_to_path = {
            executor.submit(check_path, domain, path): path 
            for path in wordlist
        }
        
        # Collect results
        for future in as_completed(future_to_path):
            result = future.result()
            if result:
                discovered.append(result)
                status = result["status"]
                url = result["url"]
                
                # Color code based on status
                if status == 200:
                    print(f"[+] Found: {url} (Status: {status})")
                elif status in [401, 403]:
                    print(f"[!] Restricted: {url} (Status: {status})")
                elif status in [301, 302]:
                    print(f"[~] Redirect: {url} (Status: {status})")
    
    if discovered:
        print(f"[+] Discovered {len(discovered)} paths")
    else:
        print(f"[-] No paths discovered")
    
    return discovered


def categorize_findings(discovered):
    """
    Categorize discovered paths by risk level
    
    Args:
        discovered (list): List of discovered paths
    
    Returns:
        dict: Categorized findings
    """
    categories = {
        "critical": [],
        "high": [],
        "medium": [],
        "low": []
    }
    
    critical_keywords = [".env", "backup.sql", "db.sql", ".git/config", "config.php"]
    high_keywords = ["admin", "backup", ".git", ".svn", "phpinfo"]
    medium_keywords = ["login", "api", "upload", "test", "dev"]
    
    for item in discovered:
        path = item["path"].lower()
        
        if any(keyword in path for keyword in critical_keywords):
            categories["critical"].append(item)
        elif any(keyword in path for keyword in high_keywords):
            categories["high"].append(item)
        elif any(keyword in path for keyword in medium_keywords):
            categories["medium"].append(item)
        else:
            categories["low"].append(item)
    
    return categories


if __name__ == "__main__":
    # Test the module
    test_domain = "example.com"
    results = dir_scan(test_domain, wordlist=["robots.txt", "sitemap.xml", "admin"])
    
    print(f"\nDiscovered paths on {test_domain}:")
    for item in results:
        print(f"  - {item['url']} (Status: {item['status']})")
    
    if results:
        categories = categorize_findings(results)
        print(f"\nRisk Analysis:")
        for level, items in categories.items():
            if items:
                print(f"  {level.upper()}: {len(items)} findings")
