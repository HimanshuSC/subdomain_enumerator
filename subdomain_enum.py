import argparse
import dns.resolver
import concurrent.futures

def resolve_subdomain(subdomain, domain):
    try:
        full_domain = f"{subdomain}.{domain}"
        answers = dns.resolver.resolve(full_domain, 'A')
        return full_domain
    except dns.resolver.NXDOMAIN:
        return None
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.Timeout:
        return None
    except dns.exception.DNSException:
        return None

def main(file, domain):
    with open(file, 'r') as f:
        subdomains = [line.strip() for line in f]

    print(f"Enumerating subdomains for {domain}...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_subdomain = {executor.submit(resolve_subdomain, subdomain, domain): subdomain for subdomain in subdomains}
        
        for future in concurrent.futures.as_completed(future_to_subdomain):
            result = future.result()
            if result:
                print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumerator Tool")
    parser.add_argument('-f', '--file', required=True, help="File containing subdomains")
    parser.add_argument('-d', '--domain', required=True, help="Target domain name")
    args = parser.parse_args()
    
    main(args.file, args.domain)
