# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:30:20 2017

@author: sudar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:39:11 2017

"""

from bs4 import BeautifulSoup
import urllib.request
import requests



url_list = ['http://foodpro.unh.edu/shortmenu.asp?sName=University%20Of%20New%20Hampshire%20Hospitality%20Services&locationNum=80&locationName=Holloway%20Dining%20Hall&naFlag=1',
            'http://foodpro.unh.edu/shortmenu.asp?sName=University%20Of%20New%20Hampshire%20Hospitality%20Services&locationNum=10&locationName=Stillings%20Dining%20Hall&naFlag=1',
            'http://foodpro.unh.edu/shortmenu.asp?sName=University%20Of%20New%20Hampshire%20Hospitality%20Services&locationNum=30&locationName=Philbrook%20Dining%20Hall&naFlag=1']

for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("td")
    list = []
    for date in table.find_all("span", {"class":"shortmenutitledate"}):
        list.append(date)
        for menu in table.find_all("div", {"class":"shortmenuheader"}):
            list.append(menu)
            for recipes in table.find_all("div", {"class":"shortmenurecipes"}):
                list.append(recipes)
                print(list)


               
                
            

    #list.append(menu) 
    #print(menu.text)
       
        
#    for recipes in record:
#        recipes.find_all("div", {"class":"shortmenurecipes"})
#        
#    

            
            
            
    
    
    
    
#    for table in record.find_all("t"):
#        for building_name in table.find_all("div", {"class":"shortmenuheader"}):
#            print(building_name)
            
#        for meals in building_name.find_all("div", {"class":"shortmenumeals"}):
#            for day in meals.find_all("div", {"class":"shortmenucats"}):
#                for food in day.find_all("div", {"class":"shortmenurecipes"}):
#                    
#    
#    
#        
       
        


 #       list_of_hours.append(getdata)
 #   mylist.append(list_of_hours)
#print(mylist, "\n")

        
        
    
 
            
        
 
    
            
                
                
            
            
            
            
            
           
            
       
      
       
       
       
       
        #hoursdata =hoursdata+","+data.text
        
        #hoursdatasave = hoursdatasave + "\n" + hoursdata[1:]

    

    
        
    
    