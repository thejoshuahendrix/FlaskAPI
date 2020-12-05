import requests

BASE = "http://127.0.0.1:5000/"


#Patch request

#response = requests.patch(BASE + "video/2", {"views":99, "likes":101})
#print(response.json())
#input()


#data = [{"likes": 76, "name": "Josh", "views": 1000},
#        {"likes": 216, "name": "New video", "views": 4000},
#        {"likes": 23236, "name": "Amigo", "views": 1000}]


#Put request for above commented data

#for i in range(len(data)):
 #   response = requests.put(BASE + "video/" +str(i), data[i]) 
 #   print(response.json())
#input()

#Get request
#response = requests.get(BASE + "video/2")
#print(response.json())


#Delete request
response = requests.delete(BASE + "video/2")
print(response)