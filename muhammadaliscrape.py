from bs4 import BeautifulSoup
import requests


def make_request_for_page(page_url):

    """
     headers :

         Read about HTTP headers usually they dont matter but
         if you requests keep getting blocked you will want to spoof
         your user-agent info. Also if you  are making a shit to of
         requests to a site then thinking about spoofing

         You don't really have to worry about this right now,
         and it is an optional argument.

    timeout:
        Timeout is the amount of time before the request is pending
        before an exception is raised. If you don't set this field,
        an invalid request will freeze your invalid scrape indefinitely.


    Misc  Info:

         learn about cookies, this becomes important when you need authenciated sessions to access data.

         dont forget to sleep in between requests, otherwise you will ddos the webpage and get blocked
     """

    headers = {

        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'en-US,en;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'thenewinquiry.com',
        'Referer':'https://www.google.com/',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    # Response is a struct that holds a bunch of stuff look up the library

    response = requests.get(page_url, headers = headers, timeout = 200)

    return response.text

def get_body_text():

    html = make_request_for_page("http://thenewinquiry.com/muhammad-ali-we-still-love-you/")
    bs_obj = BeautifulSoup(html, 'lxml')
    ps  = bs_obj.select('#body > article > div > p')


    return ' '.join([p.text for p in ps])

def write_to_file():

    text  = get_body_text()

    with open('muhmmadalitext.txt', 'w') as outfile:
        outfile.write(text)

write_to_file()
