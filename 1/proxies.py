#!/usr/bin/python
import sys
import re 

class FreeProxyHttps():
	dataUrl = 'https://free-proxy-list.net/uk-proxy.html'

	def parse(self, content):
		pattern = r'<tr><td>(.*?)<\/td><td>(.*?)<.*?<td class=\'hx\'>(.*?)<\/td>'
		matches = re.findall(pattern, content)
		matches2 = []
		for match in matches:
			if str(match[2]) == u'yes':
				matches2.append( [ match[0], match[1] ] )
		return matches2

class FreeProxyHttp():
	dataUrl = 'https://free-proxy-list.net/uk-proxy.html'

	def parse(self, content):
		pattern = r'<tr><td>(.*?)<\/td><td>(.*?)<'
		matches = re.findall(pattern, content)
		matches2 = []
		for match in matches:
			matches2.append( [ match[0], match[1] ] )
		return matches2

class GatherProxyHttp():
	dataUrl = 'http://www.gatherproxy.com/proxylist/country/?c=United%20Kingdom'

	def parse(self, content):
		pattern = r'PROXY_IP\":\"(.*?)\"[\s\S]*?PROXY_PORT\":\"(.*?)\"'
		matches = re.findall(pattern, content)
		matches2 = []
		for match in matches:
			matches2.append( [ match[0], str(int(match[1], 16)) ] )
		return matches2

class NovaProxyHttp():
	dataUrl = 'https://www.proxynova.com/proxy-server-list/country-gb/'

	def parse(self, content):
		pattern = r'<script>document.write\(\'(.*?)\'.*?\'(.*?)\'[\s\S]*?port-(.*?)\/'
		matches = re.findall(pattern, content)
		matches2 = []
		for match in matches:
			matches2.append( [ str(match[0])[8:]+str(match[1]), str(match[2]) ] )
		return matches2

class SpysProxyHttp():
	dataUrl = 'http://spys.one/free-proxy-list/GB/'

	def parse(self, content):
		pattern = r'<script>document.write\(\'(.*?)\'.*?\'(.*?)\'[\s\S]*?port-(.*?)\/'
		matches = re.findall(pattern, content)
		matches2 = []
		for match in matches:
			matches2.append( [ str(match[0])[8:]+str(match[1]), str(match[2]) ] )
		return matches2
