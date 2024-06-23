import requests
import os

def check_url(url):
    full_url = url.rstrip('/') + '/robots.txt'  # Menambahkan robots.txt ke URL
    try:
        response = requests.get(full_url)
        status_code = response.status_code
        if status_code == 200:
            print(f"URL: {full_url} - Status: Available (200)")
            print(f"HTML Output:\n{response.text}\n")
        else:
            print(f"URL: {full_url} - Status: Invalid ({status_code})")
    except requests.exceptions.RequestException as e:
        print(f"URL: {full_url} - Status: Invalid (Error: {e})")

def main():
    os.system('clear')
    print("""
 ___           _             _             _          _              _                    _                  
|  _`\        ( )           ( )_          ( )_       ( )_           ( )                  ( )                 
| (_) )   _   | |_      _   | ,_)  ___    | ,_)      | ,_)      ___ | |__     __     ___ | |/')    __   _ __ 
| ,  /  /'_`\ | '_`\  /'_`\ | |  /',__)   | |  (`\/')| |      /'___)|  _ `\ /'__`\ /'___)| , <   /'__`\( '__)
| |\ \ ( (_) )| |_) )( (_) )| |_ \__, \ _ | |_  >  < | |_    ( (___ | | | |(  ___/( (___ | |\`\ (  ___/| |   
(_) (_)`\___/'(_,__/'`\___/'`\__)(____/(_)`\__)(_/\_)`\__)   `\____)(_) (_)`\____)`\____)(_) (_)`\____)(_)   
by ZxPLOIT and ChatGpt
    """)
    mode = input("Do you want to check a single URL or a list of URLs? (single/list): ").strip().lower()
    
    if mode == "single":
        url = input("Enter URL: ").strip()
        check_url(url)
    elif mode == "list":
        filename = input("Enter the filename of the list (e.g., urls.txt): ").strip()
        try:
            with open(filename, "r") as file:
                urls = file.readlines()
            for url in urls:
                check_url(url.strip())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
    else:
        print("Invalid choice. Please enter 'single' or 'list'.")

if __name__ == "__main__":
    main()
