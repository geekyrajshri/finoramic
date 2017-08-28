#Python3.0 code
import os
import subprocess
import json

with open('data.json') as data_file:    
    data = json.load(data_file)
for d in (data[list(data.keys())[0]]):   
	print(data[list(data.keys())[0]][d]) #printing each installing dependency
	k=data[list(data.keys())[0]][d]   #accessing each dependency using dictionary key:value format
	subprocess.call(['sudo','pip','-q','install',k])
else:
	print("Success")	
