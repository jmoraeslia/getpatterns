import re

def find_urls_and_endpoints(file_path):
    url_pattern = re.compile(r'https?://[^\s"]+')
    endpoint_pattern = re.compile(r'(?<!\w)(/[a-zA-Z0-9/_-]+)')

    with open(file_path, 'r') as file:
        content = file.read()
        urls = url_pattern.findall(content)
        endpoints = endpoint_pattern.findall(content)
        
    unique_endpoints = set(endpoints)
    
    for url in urls:
        for endpoint in endpoints:
            if endpoint in url:
                unique_endpoints.discard(endpoint)
    
    return urls, list(unique_endpoints)

def main():
    file_path = input("\n\nenter path to the file: ")
    urls, endpoints = find_urls_and_endpoints(file_path)
    
    print("\n\n\n\nfound urls:")
    for url in urls:
        print(url)
    
    print("\n\n\n\nfound endpoints:")
    for endpoint in endpoints:
        print(endpoint)

if __name__ == "__main__":
    main()
