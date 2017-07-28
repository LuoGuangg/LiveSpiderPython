import requests

class Spider():

	def __init__(self):


	def run(self):
		html = requests.get(self._url)
		print (html)


if __name__ == '__main__':

	url = "https://www.douyu.com/directory/game/DOTA2"
	spider = new Spider()
		