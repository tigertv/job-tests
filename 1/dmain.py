#!/usr/bin/python
import sys
import os
import champ2018 as md
import readers as rd
import proxies as pr
import logging 
import writers as wr

results = []

#reload(sys)
#sys.setdefaultencoding('utf8')

logging.basicConfig()
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.INFO)
#log.setLevel(logging.DEBUG)
log.setLevel(logging.WARNING)
#log.setLevel(logging.NOTSET)

# getting data
log.info("Getting information...")
sys.exit()
