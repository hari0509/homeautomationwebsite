import pymongo
import webbrowser
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["hariboss"]
h=[]
colle=[]
for y in mycol.find ( {} , {"_id":0} ):
   h.append(y)

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>THREE NINJAS</title>
</head>
<body>
<h1>Home Automation Database</h1>
<p>Database for Image Processing Collections....</p>
<table>
<tr><td>STATUS</td><td>TIMING</td></tr>
<tr><td>%s</td><td>%s</td>
<tr><td>%s</td><td>%s</td>
<tr><td>%s</td><td>%s</td>
</table>
</body>
</html>
'''%(list(h[0].keys())[0],list(h[0].values())[0],list(h[1].keys())[0],list(h[1].values())[0],list(h[2].keys())[0],list(h[2].values())[0])

filename = 'index.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)