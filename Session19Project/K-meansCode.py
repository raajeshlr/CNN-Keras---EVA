#RENAME
import os
path = 'D:/MOOC/EVARepository/Session19Project/CameraDataset'
files = os.listdir(path)
i = 1

for file in files:
    if (i<10):
        os.rename(file,"img00" + str(i) +'.jpg')
    elif (i<100):
        os.rename(file,"img0" + str(i) +'.jpg')
    else:
        os.rename(file,"img" + str(i) +'.jpg')
    i = i+1    

#RESIZE    
from PIL import Image    
files = os.listdir(path)
files.remove('yolo.py')

for file in files:
    img = Image.open(file)
    img = img.resize((400,400))
    img.save(file)


#RETRIVING HEIGHT AND WIDTH VALUES FROM JSON    
import pandas as pd
data = pd.read_json("Annotation.json")
img_data = data['_via_img_metadata']
width_list = []
height_list = []

for key,value in img_data.items():
    if('img' in key):
        for i,j in value.items():
            if(isinstance(value[i],list)):
                for i in value[i]:
                    for a,b in i.items():
                        for c,d in b.items():
                            if('width' in c):
                                width_list.append(d)
                            elif('height' in c):
                                height_list.append(d)

inputlist = [{'pre_app_screen': 'LeaveApplication', 'pre_subapp_screen': 'SparshPlanApplyLeave'}, 'n', {'IncidentNumber': 'None'}, {'no_of_leaves_applied': 1}, {'leave_appliation_status': 'You can go ahead and apply leave.'}, {'email_id': 'Ramjee_R@infosys.com'}, {'leave_type_selected': 'None'}]
checklist = ['pre_app_screen','pre_subapp_screen','IncidentNumber','no_of_leaves_applied','leave_appliation_status','email_id','leave_type_selected']
outdict = {}

for iteration in inputlist:
    print(iteration)
    #print(type(iteration))
    if(isinstance(iteration,dict)):
        for key,value in iteration.items():
           for i in checklist:
               if(key == i):
                   if(value != "None"):
                       outdict[key] = value
                       
                   
                   
                   
                   
    
    
    
    
    

#CONVERTING LIST INTO DATAFRAME
hw = pd.DataFrame()
divvariable = 400
height_list = [x / divvariable for x in height_list]
width_list = [x / divvariable for x in width_list]
hw['height'] = height_list
hw['width'] = width_list

#NORMALIZING DATASET
#from sklearn.preprocessing import MinMaxScaler
#scaler = MinMaxScaler()
#scaled = scaler.fit_transform(hw)

#APPLYING K-MEANS
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(hw)

#FINDING CLUSTER CENTERS
kmeans.cluster_centers_

#FINDING INVERSE_TRANSFORM OF CLUSTER CENTROIDS
#unscaled = scaler.inverse_transform(kmeans.cluster_centers_)