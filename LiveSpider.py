#coding=utf-8
import requests
import threading
import time
import pymysql
import re
import json
import uuid
from datetime import datetime
from lxml import html

import SpiderDirs

counter_lock = threading.Lock()
ip = ''
username = ''
password = ''
database = ''

class Spider(threading.Thread):

	def __init__(self, dirs,sleepTime):
		super().__init__()    # 必须调用父类的构造方法
		self._dirs = dirs
		self._sleepTime = sleepTime
	def run(self):
		'''启动爬虫'''
		while True:
			print ("--------------------》》》》》%s爬虫线程启动"%str(self._dirs['game']))
			print ("%s开始抓取时间：%s"%(str(self._dirs['game']),str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))

			self.delete(self._dirs['index'])

			self.getHtml(self._dirs['douYuXPath'],self._dirs['douYuUrl'],self._dirs['douYuUrlHead'])
			self.getHtml(self._dirs['pandaXPath'],self._dirs['pandaUrl'],self._dirs['pandaUrlHead'])
			self.getHtml(self._dirs['huyaXPath'],self._dirs['huyaUrl'],self._dirs['huyaUrlHead'])

			self.getHtml(self._dirs['longzhuXPath'],self._dirs['longzhuUrl'],self._dirs['longzhuUrlHead'])
			self.getHtml(self._dirs['quanminXPath'],self._dirs['quanminUrl'],self._dirs['quanminUrlHead'])

			if 'douYuUrl1' in self._dirs.keys():
				self.getHtml(self._dirs['douYuXPath'],self._dirs['douYuUrl1'],self._dirs['douYuUrlHead'])
			if 'douYuUrl2' in self._dirs.keys():
				self.getHtml(self._dirs['douYuXPath'],self._dirs['douYuUrl2'],self._dirs['douYuUrlHead'])
			if 'pandaUrl1' in self._dirs.keys():
				self.getHtml(self._dirs['douYuXPath'],self._dirs['pandaUrl1'],self._dirs['douYuUrlHead'])
			if 'huyaUrl1' in self._dirs.keys():
				self.getHtml(self._dirs['douYuXPath'],self._dirs['huyaUrl1'],self._dirs['douYuUrlHead'])
			if 'longzhuUrl1' in self._dirs.keys():
				self.getHtml(self._dirs['douYuXPath'],self._dirs['longzhuUrl1'],self._dirs['douYuUrlHead'])

			self.getJson(self._dirs['huomaoUrl'],self._dirs['huomaoUrlHead'],self._dirs['huomaoJsonDir'])
			self.getJson(self._dirs['zhanqiUrl'],self._dirs['zhanqiUrlHead'],self._dirs['zhanqiJsonDir'])
			
			print ("%s结束抓取时间：%s"%(str(self._dirs['game']),str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
			time.sleep(self._sleepTime)

	def getJson(self,url,urlHead,jsonDir):
		if url != '':
		    st = requests.get(str(url))

		    hjson = json.loads(st.text)
		    jsonlist = hjson[jsonDir['json1']][jsonDir['json2']]
		    titles = []
		    imgs = []
		    nums = []
		    names = []
		    urls = []

		    for i, v in enumerate(jsonlist):
		        title = v[jsonDir['title']]
		        img = v[jsonDir['img']]
		        num = v[jsonDir['num']]
		        name = v[jsonDir['name']]
		        url = v[jsonDir['url']]
	        	titles.append(title)
	        	imgs.append(img)
	        	nums.append(num)
	        	names.append(name)
	        	urls.append(url)
		    self.format(titles,imgs,nums,names,urls,self._dirs['index'],urlHead)
		


	def getHtml(self,xpaths,url,urlHead):
		if url != '':
			try:
				st = requests.get(url, timeout=60)
				st.encoding = 'UTF-8'
				tree = html.fromstring(st.text)

				titles = tree.xpath(xpaths['titles'])
				imgs = tree.xpath(xpaths['imgs'])
				nums = tree.xpath(xpaths['nums'])
				names = tree.xpath(xpaths['names'])
				urls = tree.xpath(xpaths['urls'])
				self.format(titles,imgs,nums,names,urls,self._dirs['index'],urlHead)

			except Exception as e:
				print ("尝试连接失败")

				
	def format(self,titles,imgs,nums,names,urls,index,urlHead):

		titlezs = []
		numzs = []
		urlzs = []
		namezs = []
		for i in range(len(titles)):
			titles[i] = titles[i].replace(",","").strip()
			if titles[i] != "":
				titlezs.append(self.sqlFilter(titles[i]))

		for i in range(len(nums)):
			numzs.append(self.getNum(nums[i]))
			namezs.append(self.sqlFilter(names[i]))
			urlzs.append((str(urlHead)+urls[i]))

		self.add(titlezs,imgs,numzs,namezs,urlzs,self._dirs['index'])


	def sqlFilter(self,strs):
		strs = re.sub("[^\u4e00-\u9fa5_a-zA-Z0-9]+$", "_", strs)
		dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")", "%", "@","!"]
		for stuff in dirty_stuff:
			strs = strs.replace(stuff, "")
		return strs

	def add(self,titles,imgs,nums,names,urls,index):
		if len(nums) > 0:
			# if counter_lock.acquire():
			db = pymysql.connect(ip,username,password,database ,use_unicode=True, charset="utf8")
			cursor = db.cursor()
			dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			sql = "INSERT INTO game(game.id,game.name,game.title,game.url,game.img,game.num,game.index,game.inster_time) VALUES ('"+str(uuid.uuid1()).replace("-","")+"','"+str(names[0])+"','"+str(titles[0])+"','"+str(urls[0])+"','"+str(imgs[0])+"',"+str(nums[0])+","+str(index)+",'%s')"%(dt)
			
			for i in range(len(nums)-1):
				sql += ",('"+str(uuid.uuid1()).replace("-","")+"','"+str(names[i+1])+"','"+str(titles[i+1])+"','"+str(urls[i+1])+"','"+str(imgs[i+1])+"','"+str(nums[i+1])+"','"+str(index)+"','%s')"%(dt)
			# print (sql)
			try:
				cursor.execute(sql)
				db.commit()
			except Exception as e:
				print (e)
				db.rollback()
			finally:
				db.close()
					# counter_lock.release()


	def delete(self,index):
		if counter_lock.acquire():
			db = pymysql.connect(ip,username,password,database ,use_unicode=True, charset="utf8")

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
				counter_lock.release()


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


if __name__ == '__main__':
	dirs = SpiderDirs.getAdict()
	sleepTime = 120
	for key in dirs:
		dota = Spider(dirs[key],sleepTime)
		dota.start()
		sleepTime += 10


	

