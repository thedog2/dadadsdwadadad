N = int(input()) 
minutes = N//60 
hours = 0 

if minutes >= 60: 
    hours = minutes//60 
    minutes -= hours*60 
    seconds = N - (hours*60*60 + minutes*60) 
if seconds < 10: 
    if minutes < 10: 
        print(hours, ':', '0', minutes, ':', '0', seconds, sep='') 
    else: 
        print(hours, ':', minutes, ':', '0', seconds, sep='') 
else: 
    print(hours, ':',  minutes, ':', seconds, sep='')
