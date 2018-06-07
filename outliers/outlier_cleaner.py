#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
#    print "############predictions############"
#    print predictions
#    print len(predictions)
    print "##########cleaned data#############"    
    for i in range(0, len(predictions)):
        cleaned_data.append((ages[i], net_worths[i], abs(predictions[i]-net_worths[i])))
        cleaned_data = sorted(cleaned_data, key=lambda student: student[2])
        print "Element {}: {}".format(i, cleaned_data[i])

#    print cleaned_data
#    print len(cleaned_data)
    return cleaned_data[:81]

