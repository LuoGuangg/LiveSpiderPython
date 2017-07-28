#coding=utf-8
import requests
import sys
import io  
from lxml import html


if __name__ == '__main__':
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

	url = "https://www.douyu.com/directory/game/DOTA2"
	st = requests.get(url)
	tree = html.fromstring(st.text)
	buyers = tree.xpath('//li/a[@class="play-list-link"]/div[@class="mes"]/div[@class="mes-tit"]/h3[@class="ellipsis"]/text()')
	
	print (buyers)

		