from bs4 import BeautifulSoup as soup
import requests


ignore_texts = ["with ani inputs", "With PTI inputs", "sponsored by"]


post_data = requests.get("https://sports.ndtv.com/ipl-2023/there-are-two-pcs-one-is-priyanka-chopra-other-is-ravi-shastris-hilarious-comment-during-ipl-2023-game-3939668")
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