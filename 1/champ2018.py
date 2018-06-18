#!/usr/bin/python
import sys
import re 

class WilliamHill():
	dataUrl = 'http://anonymouse.org/cgi-bin/anon-www_de.cgi/http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html'

	def parse(self, content):
		pattern = ur'class="eventprice">([\s\S]*?)</div>[\s\S]*?class="eventselection"> ([\s\S]*?)\n'
		matches = re.findall(pattern, content, re.M )
		matches2 = {}
		for match in matches:
			matches2[ match[1] ] = match[0].strip(' \t\n\r') 
		return {"name":self.__class__.__name__, "data":matches2}
		
class PaddyPower():
	dataUrl = 'http://strands.paddypower.com/sdspp/competition-page/v2?_ak=vsd0Rm5ph2sS2uaK&betexRegion=GBR&capiJurisdiction=intl&competitionId=5614746&currencyCode=USD&eventTypeId=1&exchangeLocale=en_GB&includeBadges=true&includeLayout=true&includePrices=true&language=ru&tabId=OUTRIGHTS'
	#method = 'get'

	def parse(self, content):
		pattern = ur'\"marketId\":\"927.1549474\"([\s\S]*?)$'
		matches = re.findall(pattern, content)
		cont = str(matches)
		pattern = ur'runnerName\":\"(.*?)\"[\s\S]*?fractionalOdds\":{\"numerator\":(.*?),\"denominator\":(.*?)}'
		matches = re.findall(pattern, cont)
		matches2 = {}
		for match in matches:
			matches2[ match[0] ] = str(match[1])+'/'+str(match[2])
		return {"name":self.__class__.__name__, "data":matches2}

class Bet365():
	dataUrl = 'https://mobile.bet365.com/V6/sport/coupon/coupon.aspx?zone=9&isocode=FR&tzi=1&key=1-172-1-26326924-2-0-0-0-2-0-0-4063-0-0-1-0-0-0-0-0-0&ip=0&gn=0&cid=1&lng=1&ctg=1&ct=70&clt=9996&ot=1&pk=1-1-13-35460473-2-4-0-0-1-0-0-4100-0-0-1-0-0-0-0-0-0'

	def parse(self, content):
		pattern = ur'<span class="opp">(.*?)&nbsp; <span class="odds">(.*?)<\/span>'
		matches = re.findall(pattern, content)
		matches2 = dict(matches)
		return {"name":self.__class__.__name__, "data":matches2}

class Skybet():
	dataUrl = 'https://m.skybet.com/football/world-cup-2018/event/16742642'

	def parse(self, content):
		pattern = ur'displayOrder\":0,\"name\":\"(.*?)\".*?,\"price\":{\"num\":(.*?),\"den\":(.*?)}'
		matches = re.findall(pattern, content)
		matches2 = {}
		for match in matches:
			matches2[ match[0] ] = str(match[1])+'/'+str(match[2])
		return {"name":self.__class__.__name__, "data":matches2}
