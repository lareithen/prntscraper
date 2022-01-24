from bs4 import BeautifulSoup
import cloudscraper, random, string

def gorsel():
    rastgele = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
    scraper = cloudscraper.create_scraper()
    html = scraper.get(f'http://prnt.sc/{rastgele}').text
    soup = BeautifulSoup(html, "html.parser")
    resim_html = soup.find_all('img', {'class': 'no-click screenshot-image'})[0]['src']
    s = "prntscr.com"
    if s in resim_html:
      return gorsel()
    else:
      return resim_html

# larei was here.
