from scraping import Scraping
import json


if __name__ == '__main__':
    scrap = Scraping()
    scrap.open_page()

    mynet_dict = scrap.mynet_dict
    with open("mynet.json","w", encoding="utf-8") as f:
        json.dump(mynet_dict, f, ensure_ascii=False, indent=4)



