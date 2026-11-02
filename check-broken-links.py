#!/usr/bin/env python3
"""Check all URLs in README files for broken links."""
import os, re, sys, requests
from collections import Counter

# Regex to match URLs in markdown/text
URL_PATTERN = re.compile(r'https?://[^\s"<>]+|www\.[^\s"<>]+')

def extract_urls_from_readme(path):
    """Extract all URLs from a README file."""
    urls = []
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            urls.extend(re.findall(URL_PATTERN, text))
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
    return urls

def check_url(url):
    """Check if URL returns 200 OK."""
    try:
        # Handle common URL formats that might need www. or https://
        if 'www.' not in url and 'http' not in url:
            url = 'https://' + url
        response = requests.head(url, timeout=10, allow_redirects=True)
        return response.status_code == 200
    except Exception as e:
        return False

def main():
    print("Checking broken links in MAX-HACK-TOOLS README files...")
    broken_links = Counter()
    total_urls = 0
    
    # Check root README
    root_readme = 'README.md'
    if os.path.exists(root_readme):
        urls = extract_urls_from_readme(root_readme)
        total_urls += len(urls)
        for url in urls:
            if check_url(url):
                pass  # Good
            else:
                broken_links[url] += 1
                total_urls += 1
    
    # Check all source READMEs
    for source_dir in sorted(os.listdir('sources')):
        source_path = os.path.join('sources', source_dir)
        readme_path = os.path.join(source_path, 'README.md')
        if os.path.exists(readme_path):
            urls = extract_urls_from_readme(readme_path)
            total_urls += len(urls)
            for url in urls:
                if check_url(url):
                    pass  # Good
                else:
                    broken_links[url] += 1
                    total_urls += 1
    
    # Report results
    print(f"\nTotal URLs checked: {total_urls}")
    print(f"Broken links found: {len(broken_links)}")
    
    if broken_links:
        print("\n=== BROKEN LINKS REPORT ===")
        for url in sorted(broken_links.keys()):
            print(f"  {url}")
        print(f"\nTotal broken links: {sum(broken_links.values())}")
        return 1
    else:
        print("\nNo broken links found!")
        return 0

if __name__ == '__main__':
    exit(main())
