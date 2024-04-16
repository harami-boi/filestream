import requests
shrt_url = "https://atglinks.com/api?api=99ebb69ac0cfdc42674ba2f27c8de6976ee60020&url="
urls = []
def shorten_url(url_list):
  if stream_url is not None and download_url is not None:
    for url in url_list:
      res = requests.get(f'{shrt_url}{url}')
      if res.status_code == 200:
        data = res.json()
        url = data['shortenedUrl']
        urls.append(url)
    return urls
        
      
  
