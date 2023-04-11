from bs4 import BeautifulSoup as soup
import requests

ignore_texts = ["with ani inputs", "With PTI inputs", "sponsored by"]

url="https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
html = requests.get(url)
bsobj = soup(html.content,'html.parser')

newslist = bsobj.find("div", class_="lisingNews")
heading_elements = newslist.find_all("h2", class_="newsHdng")

data = {(heading.find("a", href=True))["href"]: heading.text.strip() for heading in heading_elements}

for key in data.keys():
    post_data = requests.get(key)
    post_bsobj = soup(post_data.content,'html.parser')
    wrapper = post_bsobj.find("div", class_="story__content")
    if(wrapper is not None):
        main_wrapper = wrapper.find("div", recursive=False)
        if(main_wrapper is not None):
            for para in main_wrapper:
                if( para is not None ):

                    for div in para.find_all("div"):
                        div.decompose()
                    for script in para.find_all("script"):
                        script.decompose()
                    
                    ig = para.find(lambda string: (string.get_text()).lower() in ignore_texts )

                    if ig:
                        ig.decompose()

                    print(para.text)
            




