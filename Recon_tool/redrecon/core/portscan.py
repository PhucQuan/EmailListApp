"""
Port Scanning Module
Fast multi-threaded port scanner for common services
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


# Common ports to scan
COMMON_PORTS = [
    21,    # FTP
    22,    # SSH
    25,    # SMTP
    53,    # DNS
    80,    # HTTP
    443,   # HTTPS
    3306,  # MySQL
    3389,  # RDP
    5432,  # PostgreSQL
    8080,  # HTTP Alt
    8443,  # HTTPS Alt
]


def scan_port(host, port, timeout=0.7):
    """
    Scan a single port on a host
    
    Args:
        host (str): Target hostname or IP
        port (int): Port number to scan
        timeout (float): Socket timeout in seconds
    
    Returns:
        int or None: Port number if open, None if closed
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            return port
        return None
    except socket.gaierror:
        # DNS resolution failed
        return None
    except socket.timeout:
        return None
    except Exception:
        return None


def port_scan(host, ports=None, max_workers=100):
    """
    Scan multiple ports on a host using threading
    
    Args:
        host (str): Target hostname or IP
        ports (list): List of ports to scan (default: COMMON_PORTS)
        max_workers (int): Number of concurrent threads
    
    Returns:
        list: List of open ports
    """
    if ports is None:
        ports = COMMON_PORTS
    
    open_ports = []
    
    print(f"[*] Scanning {len(ports)} ports on {host}...")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all port scan tasks
        future_to_port = {
            executor.submit(scan_port, host, port): port 
            for port in ports
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_port):
            result = future.result()
            if result is not None:
                open_ports.append(result)
    
    open_ports.sort()
    
    if open_ports:
        print(f"[+] Found {len(open_ports)} open ports: {open_ports}")
    else:
        print(f"[-] No open ports found")
    
    return open_ports


def get_service_name(port):
    """
    Get common service name for a port
    
    Args:
        port (int): Port number
    
    Returns:
        str: Service name
    """
    services = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP-Alt",
        8443: "HTTPS-Alt",
    }
    return services.get(port, "Unknown")


if __name__ == "__main__":
    # Test the module
    test_host = "scanme.nmap.org"  # Legal test target
    results = port_scan(test_host)
    
    print(f"\nOpen ports on {test_host}:")
    for port in results:
        print(f"  - {port} ({get_service_name(port)})")
