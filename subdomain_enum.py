import requests
import dns.resolver
import sys

def get_subdomains(domain, wordlist):
    subdomains = []
    for subdomain in wordlist:
        sub = f"{subdomain}.{domain}"
        try:
            answers = dns.resolver.resolve(sub)
            for rdata in answers:
                subdomains.append(sub)
                print(f"[+] Found: {sub} -> {rdata}")
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.LifetimeTimeout:
            pass
    return subdomains

def main(domain, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.read().splitlines()
    except FileNotFoundError:
        print(f"Wordlist file {wordlist_file} not found.")
        sys.exit(1)

    print(f"Starting subdomain enumeration for {domain}")
    subdomains = get_subdomains(domain, wordlist)

    if subdomains:
        print("\nSubdomains found:")
        for sub in subdomains:
            print(sub)
    else:
        print("No subdomains found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <domain> <wordlist>")
        sys.exit(1)

    domain = sys.argv[1]
    wordlist_file = sys.argv[2]
    main(domain, wordlist_file)
