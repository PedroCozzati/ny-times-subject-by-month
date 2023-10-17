import json
import pandas as p
import requests 
import time
from collections import Counter
from datetime import datetime
from flask import Flask, render_template, request

request_http = requests
api_key="Insira a sua api key aqui, você pode obtê-la no site:  https://developer.nytimes.com/docs/archive-product/1/overview" 


def getDataFromNYT(month,year):
    url = "https://api.nytimes.com/svc/archive/v1/"+ year +"/" + month +".json?api-key="+api_key

    getDataFromNYT = request_http.get(url) 
    jsonData = getDataFromNYT.json()
    return jsonData


def filterData(data,count):
    test=[]
    keywords=[]
    
    for object in data['response']['docs']:
        
        keywords = object['keywords']
        test.append(keywords)

    return test

def read_all():
    
    args = request.args
    year = args.get('year')
    month = args.get('month')
    
    count = 0
    kw = []
    data={}
    dict=[]
    final_json={}
    year_keyword_list = []
    f_json={}
    
    
    count=count+1
    
    data = getDataFromNYT(month,year)  
  
    #Apenas para evitar rate limit da api que fornece os dados
    time.sleep(1)
    
    obj = filterData(data,month)
    
    o = []
    o.append({
        month:obj           
    })
    
    for keyword in  obj:
        kw.append(keyword)
    for k in kw:
        for word in k:
            if word['name']=='subject' and word['value'] != 'internal-sub-only-nl':
                if 'value' in word:
                    year_keyword_list.append(word['value'])
    
    c = Counter(year_keyword_list)
    most_frequent_subjects = c.most_common(20)
    i = 0
    
    for item in most_frequent_subjects:
        dict.append({
            "subject":item[0],
            "amount":item[1]
        })
        i=i+1
        
    final_json={
        month:dict
    }
    f_json = final_json

    return list(f_json.values())

    
    