import csv
import json
import codecs
import requests
import urllib2
import sys
#https://github.com/vinay20045/json-to-csv/blob/master/json_to_csv.py






fi=codecs.open("zopnow_categories.json","r",encoding="utf-8")
f=fi.read()
fi.close()
f=json.loads(f)
for val_f in f:
	xa=val_f['url']
	xa=xa.replace(".php",".json")
	url="http://www.zopnow.com/"+xa
#url = "http://www.zopnow.com/fresh-vegetables-c.json"
	req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
	con = urllib2.urlopen(req)
	#temp = urllib2.urlopen('http://www.zopnow.com/fresh-vegetables-c.json')
	temp=con.read()
	temp=json.loads(temp)
	print val_f['name']
	
	cod=codecs.open(val_f['name']+".csv",'w',encoding="utf-8")
	temp_arr=[]
	
	for xaxaxaca in temp:
		if xaxaxaca['name']=='ProductGrid':
			for i in range(1,xaxaxaca['data']['count']/20+2):
				
				url = "http://www.zopnow.com/fresh-vegetables-c.json?page="+str(i)
				req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
				con = urllib2.urlopen(req)
				temp=con.read()
				temp=json.loads(temp)
	
	
				if i==1:
					for val2 in xaxaxaca['data']['products']:
						for k in val2['variants']:
							temp_jsn={}
							temp_jsn['category_name']=val2['category']['name']
							temp_jsn['discount']=k['discount']
							temp_jsn['mrp']=k['mrp']
							temp_jsn['image']=k['images'][0]
							#print k['images'][0]
							temp_jsn['properties']=k['properties']['Quantity']
							temp_jsn['full_name']=k['full_name']
				
							temp_jsn['brand']=val2['brand']['name']
							temp_arr.append(temp_jsn)
				else:
					for val2 in temp[1]['data']['products']:
						for k in val2['variants']:
							temp_jsn={}
							temp_jsn['category_name']=val2['category']['name']
							temp_jsn['discount']=k['discount']
							temp_jsn['mrp']=k['mrp']
							temp_jsn['image']=k['images'][0]
							#print k['images'][0]
							temp_jsn['properties']=k['properties']['Quantity']
							temp_jsn['full_name']=k['full_name']
				
							temp_jsn['brand']=val2['brand']['name']
							temp_arr.append(temp_jsn)
						#print i
			cod.write("Full Name, Brand, Category Name, Properties, MRP, Discount\n")
			for xaxa in temp_arr:
				json.dumps(temp_arr)
				cod.write(xaxa['full_name']+', '+xaxa['brand']+', '+xaxa['category_name']+', '+xaxa['properties']+', '+str(xaxa['mrp'])+', '+str(xaxa['discount'])+'\n')
