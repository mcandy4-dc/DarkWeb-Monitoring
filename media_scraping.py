import subprocess as subp
import requests
from modules.file import choose_file
from modules.url import parse_url
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white
def main2():
    """
    Presents options for scraping from single URL or file type
    """
    choice = '0'
    while choice == '0':
        print(R + '[+] ' + G +  'Choose the File Format:-' + W)
        print(R + '[1] ' + G +  'Scrape From File'  + W)
        print(R + '[2] ' + G +  'Scrape From Single URL'  + W + '\n')
        choice = input(G + '[+]' + C + " Enter Option No. ->  " + W)

        if choice == "1":
            choose_file()
        elif choice == "2":
            parse_url()
        else:
            print('\n' + R + "[!] I don't understand your choice." + W + '\n')
            return main2()
if __name__=='__main__':
     try:
         main2()
     except KeyboardInterrupt:
         print('\n' + R + '[!]' + R + ' Keyboard Interrupt.' + W)
         exit()
