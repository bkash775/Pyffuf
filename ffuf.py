#!/usr/bin/python3
import requests
import sys
import cowsay
wordlists=[]
line_number=15
file_path = "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt"
with open(file_path,'r') as file:
    for current_line_number,line in enumerate(file,start=1):
        #print(line)
        #print(current_line_number)
        if current_line_number >= line_number:
                wordlists.append(line.strip())

        
def banner():
    text = '''
    A simple python tool that simulates as ffuf 
    Author : B1k4sh
    Version: 1.0
    '''
    output = cowsay.cow(text)
def crawl():
    if len(sys.argv) != 2:
        sys.exit("please provide link")
    try:
        url = sys.argv[1]
        for line in wordlists:
            payload = f"{url}/{line}"
            #print(payload)
            response = requests.get(payload)
            if response.status_code in [200,204,301,302,307,401,403,405,500]:
                print(f"{response.status_code} --> {payload}")
            else:
                continue
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    banner()
    crawl()

     
