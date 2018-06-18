#!/usr/bin/python
import sys
import re 
import requests
import logging as log 

class WebReader():
	userAgent = 'Mozilla/5.0'
	proxies = None
	currentProxyIndex = 0
	dataSource = None
	proxyReader = None
	timeout = 60

	def setTimeout(self, seconds):
		timeout = seconds

	def setDataSource(self, dataSource):
		self.dataSource = dataSource

	def setUserAgent(self, agent):
		self.userAgent = agent

	def setProxies(self, proxies):
		self.proxies = proxies
		self.currentProxyIndex = 0

	def setProxyReader(self, reader):
		self.proxyReader = reader

	def nextProxy(self):
		self.currentProxyIndex += 1
		log.debug('self.currentProxyIndex='+str(self.currentProxyIndex))
		if self.currentProxyIndex < len(self.proxies):
			site = self.proxies[self.currentProxyIndex][0]+':'+self.proxies[self.currentProxyIndex][1]
			log.debug("proxy server changed")
			return 1
		log.debug('where are no proxies anymore, get a new list')
		return 0

	def getData(self):
		content = ''
		dataUrl = self.dataSource.dataUrl

		if hasattr(self.dataSource, 'headers'):
			headers = self.dataSource.headers
		else:
			headers = {'User-Agent' : self.userAgent}

		results = None

		if self.proxies is None:
			try:
				if hasattr(self.dataSource, 'method'):
					if self.dataSource.method == "post":
						log.debug('post without proxy')
						resp = requests.post(dataUrl, headers=self.dataSource.headers, timeout=self.timeout, data=self.dataSource.data)
					elif self.dataSource.method == "get":
						log.debug('get without proxy')
						#resp = requests.get(dataUrl, headers=headers, timeout=self.timeout, verify=False)
						resp = requests.get(dataUrl, headers=headers, timeout=self.timeout)
					log.debug( 'headers input='+str(self.dataSource.headers) )
				else:
					log.debug('get')
					#resp = requests.get(dataUrl, headers=headers, timeout=self.timeout, verify=False)
					resp = requests.get(dataUrl, headers=headers, timeout=self.timeout)
				content = resp.text
				log.debug('headers output without proxy ='+str(resp.headers))
				results = self.dataSource.parse(content)

			except requests.exceptions.ConnectionError:
				log.debug('no proxy and a request error')
		else:
			for i in range(self.currentProxyIndex, len(self.proxies)):
				try:
					proxy = self.proxies[i]
					site = proxy[0]+':'+proxy[1]
					log.info('Current proxy: '+site)
					if hasattr(self.dataSource, 'method'):
						if self.dataSource.method == "post":
	 						log.debug('post with proxy')
							log.debug( 'headers input='+str(self.dataSource.headers) )
							#resp = requests.post(dataUrl, proxies=dict(http='https://'+site, https='https://'+site), headers=headers, timeout=self.timeout, data=self.dataSource.data)
							resp = requests.post(dataUrl, proxies=dict(http='https://'+site, https='https://'+site), headers=self.dataSource.headers, timeout=self.timeout, data=self.dataSource.data)
						elif self.dataSource.method == "get":
							log.debug('get')
							#resp = requests.get(dataUrl, proxies=dict(http='https://'+site, https='https://'+site), headers=headers, timeout=self.timeout, verify=False)
							resp = requests.get(dataUrl, proxies=dict(http='https://'+site, https='https://'+site), headers=headers, timeout=self.timeout)
					else:
						log.debug('get')
						#resp = requests.get(dataUrl, proxies=dict(http='https://'+site, https='https://'+site), headers=headers, timeout=self.timeout, verify=False)
						resp = requests.get(dataUrl, proxies=dict(http='https://'+site, https='https://'+site), headers=headers, timeout=self.timeout)
					content = resp.text
					results = self.dataSource.parse(content)
					log.debug('headers output with proxies='+str(resp.headers))
					if results['data']:
						log.debug('Results exist')
						log.debug(str(results))
						break
					else:
						ret = self.nextProxy()
						log.debug('ret='+str(ret))
						if ret == 1:
							continue
					break
				except requests.exceptions.ConnectionError, e:
					log.debug('Exception connectionError='+str(e))
					ret = self.nextProxy()
					if ret == 1:
						continue
					break # end if no other proxies

		if not content:
			log.debug('no content')
		return results 

class FileReader():
	parser = 0
	fileName = ''

	def __init__(self, parser, fileName):
		self.fileName = fileName
		self.parser = parser

	def setParser(self, parser):
		self.parser = parser

	def setDataSource(self, dataSource):
		self.parser = dataSource
		self.fileName = dataSource.fileName

	def setFileName(self, fileName):
		self.fileName = fileName

	def getData(self):
		try:
			file = open(self.fileName, 'r') 
			content = file.read() 
			file.close()
		except IOError:
			sys.exit("Error: Can't open and read the file")

		if not content:
			sys.exit("Error: There is no information.")

		return self.parse(content)
	
	def parse(self, content):
		return self.parser.parse(content)
