# subdomain_enumerator:

This powerful tool, crafted in Python, is designed to discover subdomains associated with your domain. By utilizing this tool, you can proactively safeguard your online presence by thoroughly enumerating all potential subdomains, ensuring no vulnerabilities go unnoticed.


Usage :

This tool requires a custom list of subdomains which can be found online.

Prerequisite:

$ sudo apt install python3 -y 

$ pip install requests dnspython

$ wget https://github.com/HimanshuSC/subdomain_enumerator/blob/main/subdomain_enum.py

$ Create or download a file containing subdomains.

Example 

$ python subdomain_enum.py -d example.com -f subdomains.txt


python subdomain_enum.py zoom.com sub.txt

Starting subdomain enumeration for zoom.com


Subdomains found:

www.zoom.com

www.zoom.com

mail.zoom.com

api.zoom.com

test.zoom.com

support.zoom.com


# Disclaimer:

This tool should not be used for unethical purpose.
