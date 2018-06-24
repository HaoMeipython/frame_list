from zspider.core.spider import Spider
from zspider.http.request import Request
from zspider.item import Item

class Tiebaspider(Spider):
    start_url="https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn={}"

    def start_request(self):
        urls=[self.start_url.format(i*50) for i in range(10)]
        headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36"}

        for url in urls:
            yield Request(url,headers=headers)

    def parse(self,response):
        # print(response.body.decode())
        # // *[ @ id = "frslistcontent"]
        # print(111111)
        li_list=response.xpath("//ul[@id='frslistcontent']/li[@class='tl_shadow tl_shadow_new']")
        # print(li_list)
        for li in  li_list:
            item={}
            item["title"]=li.xpath(".//div[@class='ti_title']/span/text()")
            item["href"]="https://tieba.baidu.com"+li.xpath("./a/@href")[0] if len(li.xpath("./a/@href"))>0 else None
            # print(item)
            if item["href"] is not None:
                yield Request(
                    item["href"],
                    callback='parse_detail',
                    meta={"item":item}
                )
    def parse_detail(self,response):
        item=response.meta["item"]

        item["img"]=response.xpath("//img[@class='BDE_Image']/@src")

        print(item)
        yield item
