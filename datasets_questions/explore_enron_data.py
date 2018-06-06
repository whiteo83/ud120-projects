#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### General Review of data####
print len(enron_data)

#for key in enron_data:
#    print key
    
#pprint.pprint(enron_data)
    

###Counting number of Persons of interest identified in the dataset###
poi_num = 0
poi_key = 0 
for key in enron_data:    
    poi_key += 1
    if enron_data[key]["poi"] == True:
#        print "{}:POI{}".format(enron_data[key],enron_data[key]["poi"])
        poi_num += 1
    
print "POI Keys cycled:{}".format(poi_key)        
print "# of POI Identified:{}".format(poi_num)

###Pull feature of interest belonging to an individual###
name = "Fastow Andrew S"
feature_of_interest = "total_payments"
print "{}'s {}:{}".format(name, feature_of_interest, enron_data[name.upper()][feature_of_interest])


####Data Validation####

features = 0
feature_validated = "total_payments"

for key in enron_data:
    
    if enron_data[key][feature_validated] != "NaN":
        features += 1

print "{} have {}".format(features, feature_validated)


