from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pysolr,uuid
import pandas as pd


solr = pysolr.Solr('http://localhost:8983/solr/dashboard_data', always_commit=True)


# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    return render(request,
                  'index.html')
def query(request):
	
	#getting the sentence that was typed
    query = request.GET.get('query',None)
    #initializing the dictionary to be passed to the graph
    dict3 = {
	                    'cat':[],
	                    'noncat':[]
	                }
    dict4 = {
	                    'value':[]
	                    
	                }
	#splitting the sentence to get the first two words
    starting_bit = query.split()[:2]
    #chacking if user asks for a graph
    if starting_bit[0] == "Graph":
	    query1 = query.split("of")
	    query2 = str(query1[1]).split("by")

	    non_cat = str(query2[0]).strip()
	    cat = str(query2[1]).strip()
	    print(non_cat)
	    print(cat)

	    

	    if non_cat == 'Sales':
	    	print('ytes')
	    	dict3['noncat'].append('SALES')
	    if cat == 'Product':
	    	dict3['cat'].append('PRODUCTLINE')
	    if cat == 'Product Size':
	    	dict3['cat'].append('DEALSIZE')
	    return JsonResponse(dict3,safe = False)
    print(starting_bit)
    if starting_bit[0] == "Average":
    	if starting_bit[1] == "Price":
	    	query3 = query.split("of")
	    	str(query3[1]).strip()
	    	print(str(query3[1]).strip())
	    	results = solr.search(q = [str(query3[1]).strip()],rows = 500000, start = 0)
	    	df1 = pd.DataFrame(results.docs)
	    	# print(df1['PRICEEACH'].mean())
	    	dict4['value'].append(df1['PRICEEACH'].mean())
	    	return JsonResponse(dict4,safe = False)
    	if starting_bit[1] == "Sales":
	    	query3 = query.split("of")
	    	str(query3[1]).strip()
	    	results = solr.search(q = [str(query3[1]).strip()],rows = 500000, start = 0)
	    	df1 = pd.DataFrame(results.docs)
	    	# print(df1['SALES'].mean())
	    	dict4['value'].append(df1['SALES'].mean())
	    	return JsonResponse(dict4,safe = False)
    if starting_bit[0] == "Total":
    	if starting_bit[1] == "Price":
	    	query3 = query.split("of")
	    	str(query3[1]).strip()
	    	print(str(query3[1]).strip())
	    	results = solr.search(q = [str(query3[1]).strip()],rows = 500000, start = 0)
	    	df1 = pd.DataFrame(results.docs)
	    	# print(df1['PRICEEACH'].mean())
	    	dict4['value'].append(df1['PRICEEACH'].sum())
	    	return JsonResponse(dict4,safe = False)
    	if starting_bit[1] == "Sales":
	    	query3 = query.split("of")
	    	str(query3[1]).strip()
	    	results = solr.search(q = [str(query3[1]).strip()],rows = 500000, start = 0)
	    	df1 = pd.DataFrame(results.docs)
	    	# print(df1['SALES'].mean())
	    	dict4['value'].append(df1['SALES'].sum())
	    	return JsonResponse(dict4,safe = False)

	  


        #set up solr with the required data 
        	#will require changing the managed-schema 
        	#will need you to throw the data inside
        	#can you manage it with sqlite? 
        #split the sentence to get the product name
        #search for price 
        
    print(dict3) 

    
