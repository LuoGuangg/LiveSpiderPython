#coding=utf-8
import requests
import threading
import time
import pymysql
import re
from lxml import html


class Spider(threading.Thread):

	def __init__(self, url,xpaths,urlHead,index):
		super().__init__()    # 必须调用父类的构造方法
		self._url = url
		self._xpaths = xpaths
		self._index = index
		self._urlHead = urlHead

	def run(self):
		'''启动爬虫'''
		while True:
			print ("---启动爬虫---"+self._url)
			# gameAdict = {'titles':titlezs,'imgs':imgs,'nums':nums,'names':names,'urls':urls}
			# print ("%d == %d == %d"%(len(titles),len(imgs),len(names)))
			self.delete(self._index)
			self.getHtml()
			time.sleep(40)

	def getHtml(self):
		st = requests.get(self._url)
		tree = html.fromstring(st.text)

		titles = tree.xpath(self._xpaths['titles'])
		imgs = tree.xpath(self._xpaths['imgs'])
		nums = tree.xpath(self._xpaths['nums'])
		names = tree.xpath(self._xpaths['names'])
		urls = tree.xpath(self._xpaths['urls'])

		titlezs = []
		numzs = []
		urlzs = []
		namezs = []

		for i in range(len(titles)):
			titles[i] = titles[i].replace(",","").strip()
			if titles[i] != "":
				titlezs.append(re.sub("[^\u4e00-\u9fa5_a-zA-Z0-9]+$", "_", titles[i]))



		for i in range(len(nums)):
			numzs.append(self.getNum(nums[i]))
			namezs.append(re.sub("[^\u4e00-\u9fa5_a-zA-Z0-9]+$", "_", names[i]))
			urlzs.append(str(self._urlHead)+urls[i])


		self.add(titlezs,imgs,numzs,namezs,urlzs,self._index)
				


	def add(self,titlezs,imgs,nums,names,urls,index):
		if len(nums) > 0:
			db = pymysql.connect("localhost","root","lgroot","jiezouzhibo" ,use_unicode=True, charset="utf8")
			cursor = db.cursor()

			sql = "INSERT INTO game(game.name,game.title,game.url,game.img,game.num,game.index) VALUES ('"+str(names[0])+"','"+str(titlezs[0])+"','"+str(urls[0])+"','"+str(imgs[0])+"','"+str(nums[0])+"','"+str(index)+"')"
			
			for i in range(len(nums)-1):
				sql += ",('"+str(names[i+1])+"','"+str(titlezs[i+1])+"','"+str(urls[i+1])+"','"+str(imgs[i+1])+"','"+str(nums[i+1])+"','"+str(index)+"')"
			
			try:
				cursor.execute(sql)
				db.commit()
			except Exception as e:
				print (e)
				db.rollback()
			finally:
				db.close()


	def delete(self,index):

		db = pymysql.connect("localhost","root","lgroot","jiezouzhibo",use_unicode=True, charset="utf8")

		cursor = db.cursor()

		sql = "DELETE FROM game  WHERE game.index = "+str(index)
		try:
			cursor.execute(sql)
			db.commit()
		except Exception as e:
			print (e)
			db.rollback()
		finally:
			db.close()


	def getNum(self,num):

		num = num.replace("人","").replace(",","")

		if "万" in num:
			num = num.replace("万","")
			try:
				num = float(num)*10000
			except Exception as e:
				num = re.sub("\D", "0", num)
		else:
			num = re.sub("\D", "", num)

		return int(num)


def getAdict():

	douYuUrlHead = "https://www.douyu.com"
	douYuPath = {
		'titles':'//li/a[@class="play-list-link"]/div[@class="mes"]/div[@class="mes-tit"]/h3[@class="ellipsis"]/text()',
		'imgs':'//li/a[@class="play-list-link"]/span[@class="imgbox"]/img/@data-original',
		'nums':'//li/a[@class="play-list-link"]//span[@class="dy-num fr"]/text()',
		'names':'//li/a[@class="play-list-link"]/div[@class="mes"]//span[@class="dy-name ellipsis fl"]/text()',
		'urls':'//li/a[@class="play-list-link"]/@href',
		}

	pandaUrlHead = "https://www.panda.tv"
	pandaPath = {
		'titles':'//a[@class="video-list-item-wrap"]/div[@class="video-info"]/span[@class="video-title"]/text()',
        'imgs':'//a[@class="video-list-item-wrap"]/div[@class="video-cover"]/img/@data-original',
        'nums':'//a[@class="video-list-item-wrap"]/div[@class="video-info"]/span[@class="video-number"]/text()',
        'names':'//div[@class="user-info"]/div[@class="userinfo-desc"]/span[@class="userinfo-nickname"]/text() | //a[@class="video-list-item-wrap"]/div[@class="video-info"]/span[@class="video-nickname"]/text() ',
        'urls':'//a[@class="video-list-item-wrap"]/@href',
		}

	pandaDotaUrl = "https://www.panda.tv/cate/dota2"
	douYuDotaUrl = "https://www.douyu.com/directory/game/DOTA2"
	
	dotaDirs = {'douYuDotaUrl':douYuDotaUrl,'douYuPath':douYuPath,'douYuUrlHead':douYuUrlHead,'urlIndex':1}



	urlDNF = "https://www.douyu.com/directory/game/DNF"

	dirs = {'dotaDirs':dotaDirs}
	return dirs


if __name__ == '__main__':

	dirs = getAdict()

	dotaDirs = dirs['dotaDirs']
	dota = Spider(dotaDirs['douYuDotaUrl'],dotaDirs['douYuPath'],dotaDirs['douYuUrlHead'],dotaDirs['urlIndex'])
	dota.start()

	# dota = Spider(urlDOTA,douYuPath)
	# dota.start()
