import json
import urllib
import os
import time

dir_out= '/home/GA13/data/yahoo_finance_data'
if not os.path.exists(dir_out):
	os.mkdir(dir_out)
	print 'crated directory %s' % dir_out

threshold = 25
symbols = ['AAPL']
tmp =[]

for symbol in symbols:
	time.sleep(.5)
	data_out = {}
    	threshold_l = 'less than %s' % threshold
    	threshold_h = 'more than %s' % threshold
	try:
        	if threshold_l not in data_out:
            		data_out[threshold_l]=0
        	if threshold_h not in data_out:
            		data_out[threshold_h]=0
        	url = 'http://ichart.finance.yahoo.com/table.csv?s=%s&d=6&e=24&f=2013&g=d&a=4&b=18&c=2012&ignore=.csv' % (symbol)
        	data = urllib.urlopen(url).read()
        	print data
		file = '%/%s_data.cvs' % (dir_out,symbol)
		print 'savingfile %s' % file
		f = open(file,'w')
		f.write('%s' % str(data))
		f.close()
		data=data.split('\n')
		for d in data[1:-1]:
			try:
				d=d.split(',')
				close =d[6]
				tmp.append(close)
				if float(close)>=float(threshold):
					data_out[threshold_h]+=1
				elif float(close)<float(threshold):
					data_out[threshold_l]+=1
			except Exception as e:
				print e
	except Exception as e:
		print e
	print json.dumps(data_out)
			

