#!/usr/bin/python
import sys
import os
import logging as log
import champ2018 as md
import readers as rd
import proxies as pr
import writers as wr

results = []

reload(sys)
sys.setdefaultencoding('utf8')

#log.basicConfig()
#log.basicConfig(filename='myapp.log', level=log.INFO)
log.basicConfig(level=log.DEBUG)
#log = log.getLogger(__name__)
#log.addHandler(log.StreamHandler())
#log.setLevel(log.DEBUG)
#log.setLevel(log.INFO)
#log.setLevel(log.NOTSET)

# getting data
log.info("Getting information...")

#sys.exit('exit')
# getting data from internet
client = rd.WebReader()
client.setTimeout(15)

# getting proxies

source = pr.FreeProxyHttp()
client.setProxyReader(source)
client.setDataSource(source)
proxies = client.getData()

source = pr.GatherProxyHttp()
client.setProxyReader(source)
client.setDataSource(source)
proxies += client.getData()

source = pr.NovaProxyHttp()
client.setProxyReader(source)
client.setDataSource(source)
proxies += client.getData()

client.setProxies(proxies)
#client.setProxies([ ['163.172.27.213', '3128'] ])

log.info('proxies='+str(proxies))
#client.nextProxy()
source = md.Bet365()
client.setDataSource(source)
data = client.getData()
results.append(data)

source = md.Skybet()
client.setDataSource(source)
data = client.getData()
results.append(data)

client.setProxies(None)

source = md.WilliamHill()
client.setDataSource(source)
data = client.getData()
results.append(data)

source = md.PaddyPower()
client.setDataSource(source)
data = client.getData()
results.append(data)
'''
'''

if results:
	log.debug( 'results='+str(results) ) 
	writer = wr.CsvFileWriter('results.csv')
	writer.write(results)

	writer2 = wr.CsvScreenWriter()
	writer2.write(results)
