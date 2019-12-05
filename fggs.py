from googlesearch import search

    
def fine_garined_search(query, stop=None, func):
    #candidate urls
    url_list=[]
    for url in search(query, stop=stop):
        url_list.append(url)
    #filtered urls    
    res_url=[]
    for url in url_list:
        if func(url):
            res_url.append(url)
        else:
            continue
    return res_url
    
#example func
def zhihu_search(url):
  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
  r  = requests.get(url, headers=headers)
  data = r.text
  soup = BeautifulSoup(data)
  tmp=soup.find_all("div", {"class": "ProfileHeader-infoItem"})
  try:
    txt=tmp[0].text
    if "互联网" in txt and "头条" in txt and ("字节" not in txt):
      return True
    else:
      False
  except:
    return False
