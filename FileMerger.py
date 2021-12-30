#--------------------StarExoplanetDataMerger.py----------------------------#

"""
Importing modules:
-csv
-pandas (pd)
"""
import csv
import pandas as pd


#Reading and sectioning data for the exoplanets
df_exoplanets=pd.read_csv("Exoplanets.csv")
df_exoplanets=df_exoplanets[["Name","Mass (MJ)","Radius (RJ)","Distance (ly)"]]

#Creating lists for the several attributes of the exoplanet
mass_exoplanets=df_exoplanets["Mass (MJ)"].tolist()
radius_exoplanets=df_exoplanets["Radius (RJ)"].tolist()
distance_exoplanets=df_exoplanets["Distance (ly)"].tolist()
name_exoplanets=df_exoplanets["Name"].tolist()

#Defining the list to temporarily store the masses of the exoplanets
new_mass_exoplanets=[]

#Running a for loop the enumerated list of masses of exoplanets
for ind,mass_element in enumerate(mass_exoplanets):

  #Verifying whether the value of the element is not an empty string
  #Case-1~The element is not considered
  if mass_element!="":

    #Verifying whether the value of the element has any of the symbols, namely- "<",">","±","+" and "-"
    #Case-1~"<" is present
    if "<" in mass_element:
        new_mass_element=mass_element.replace("<","")
        new_mass_exoplanets.append(float(new_mass_element))

    #Case-2~">" is present    
    elif ">" in mass_element:
        new_mass_element=mass_element.replace(">","")
        new_mass_exoplanets.append(float(new_mass_element)) 

    #Case-3~"±" is present       
    elif "±" in mass_element:
      mass_element_lower,mass_element_higher=mass_element.split("±")
      mass_average=(float(mass_element_lower)+float(mass_element_higher))/2 
      new_mass_exoplanets.append(mass_average) 

    #Case-4~"+" and "-" are present 
    elif "+" in mass_element and "−" in mass_element:
      mass_element_sum_1,mass_element_sum_2=mass_element.split("+")
      mass_element_difference_1,mass_element_difference_2=mass_element_sum_2.split("−")
      mass_element_result_1=float(mass_element_sum_1)+float(mass_element_difference_1)
      mass_element_result_2=mass_element_result_1-float(mass_element_difference_2)
      new_mass_exoplanets.append(mass_element_result_2)
         
    #Case-5~None of them are present     
    else: 
      new_mass_exoplanets.append(float(mass_element)*0.000954588) 

#Defining the list to temporarily store the radii of the exoplanets
new_radius_exoplanets=[]

#Running a for loop the enumerated list of radiio f exoplanets
for ind,radius_element in enumerate(radius_exoplanets):

  #Verifying whether the value of the element is not an empty string
  #Case-1~The element is not considered
  if radius_element!="":

    #Verifying whether the value of the element has any of the symbols, namely- "<",">","±","+" and "-"
    #Case-1~"<" is present
    if "<" in radius_element:
        new_radius_element=radius_element.replace("<","")
        new_radius_exoplanets.append(float(new_radius_element))

    #Case-2~">" is present        
    elif ">" in radius_element:
        new_radius_element=radius_element.replace(">","")
        new_radius_exoplanets.append(float(new_radius_element))  

    #Case-3~"±" is present      
    elif "±" in radius_element:
      radius_element_lower,radius_element_higher=radius_element.split("±")
      radius_average=(float(radius_element_lower)+float(radius_element_higher))/2 
      new_radius_exoplanets.append(radius_average) 

    #Case-4~"+" and "-" are present 
    elif "+" in radius_element and "−" in radius_element:
      radius_element_sum_1,radius_element_sum_2=radius_element.split("+")
      radius_element_difference_1,radius_element_difference_2=radius_element_sum_2.split("−")
      radius_element_result_1=float(radius_element_sum_1)+float(radius_element_difference_1)
      radius_element_result_2=radius_element_result_1-float(radius_element_difference_2)
      new_radius_exoplanets.append(radius_element_result_2)

    #Case-5~None of them are present     
    else: 
      new_radius_exoplanets.append(float(radius_element)*0.1004) 

#Defining the list to temporarily store the distances of the exoplanets
new_distance_exoplanets=[]

#Running a for loop the enumerated list of distances of exoplanets
for ind,distance_element in enumerate(distance_exoplanets):

  #Verifying whether the value of the element is not an empty string
  #Case-1~The element is not considered
  if distance_element!="":

    #Verifying whether the value of the element has any of the symbols, namely- "<",">","±","+" and "-"
    #Case-1~"<" is present
    if "<" in str(distance_element):
        new_distance_element=distance_element.replace("<","")
        new_distance_exoplanets.append(float(new_distance_element))

    #Case-2~">" is present      
    elif ">" in str(distance_element):
        new_distance_element=distance_element.replace(">","")
        new_distance_exoplanets.append(float(new_distance_element))    

    #Case-3~"±" is present    
    elif "±" in str(distance_element):
      distance_element_lower,distance_element_higher=distance_element.split("±")
      distance_average=(float(distance_element_lower)+float(distance_element_higher))/2 
      new_distance_exoplanets.append(distance_average) 

    #Case-4~"+" and "-" are present 
    elif "+" in str(distance_element) and "−" in str(distance_element):
      distance_element_sum_1,distance_element_sum_2=distance_element.split("+")
      distance_element_difference_1,distance_element_difference_2=distance_element_sum_2.split("−")
      distance_element_result_1=float(distance_element_sum_1)+float(distance_element_difference_1)
      distance_element_result_2=distance_element_result_1-float(distance_element_difference_2)
      new_distance_exoplanets.append(distance_element_result_2)

    #Case-5~None of them are present      
    else:  
      new_distance_exoplanets.append(float(distance_element)*1) 




#Defining the list to finally store the masses,radii and distances of the exoplanets
final_exoplanet_list=[]

#Running a for loop over the range of zero to the length of the exoplanets dataset minus 1, mimicking an index system and appending elements accordingly
for i in range(0,(len(df_exoplanets)-1)):
  final_exoplanet_list.append([name_exoplanets[i],new_mass_exoplanets[i],new_radius_exoplanets[i],new_distance_exoplanets[i]])

stars_list=[]

#Reading from the file to atttain the star data and converting the data to a list type
with open("Stars.csv","r") as st:
  reader=csv.reader(st)
  reader_list=list(reader)

  #Running a in-list for loop to section off data from the converted list
  stars_list=[data[0:4] for data in reader_list]

#Ommiting the first of the list
stars_list=stars_list[1:]


    


#Defining the list to combine all the data 
final_combined_list=[]

#Running a for loop over the range of zero to the length of the exoplanets dataset minus 1, mimicking an index system appending elements accordingly
for f in range(0,(len(stars_list)-1)):
  final_combined_list.append(final_exoplanet_list[f])
  final_combined_list.append(stars_list[f])



#Providing an input for the user to decide a file name
file_input=input("Please provide the file name:")

#Verifying whether file name given by user has "." in or not
#Case-1 ~"." is removed by splitting the file name with regard to it
if "." in file_input:
    file_name,file_extension=file_input.split(".")
    file_input=file_name

#Creating a csv file with the name set according to the user's input
with open("{}.csv".format(file_input),"w") as s:
    
    #Initiating the writer and using it to write into the file
    writer=csv.writer(s)
    writer.writerow(["Name","Mass","Radius","Distance"])
    writer.writerows(final_combined_list)

#Printing the ending message
print("Thank you using StarExoplanetDataMerger.py")

#--------------------StarExoplanetDataMerger.py----------------------------#