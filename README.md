### To predict address

########### Files
Assignment Instructions.pdf: Contains detail of the assignment (Assignment is done in python).
test_address.csv: Contains address to be predicted.
predicted_address_data.py: Contains code to predict address.
predicted_address_data.csv: Contains predicted address and False Discovery Rate	and False Omission Rates.


Google API used to predict address:
address = "address_to_search"
url = 'https://maps.googleapis.com/maps/api/geocode/json?components=country:&language=&region=&bounds=&key=' 
url = url + '&address='+ address.replace(" ","+")



########### Result
False Discovery Rate: 0.026178010471204
False Omission Rates: 0.923076923076923
Precision: 0.076923076923077
Accuracy: 0.916666666666667

Further,
Both Precision (i.e., Probability of relevant prediction) and Accuracy is high.
Also, False Discovery Rate (i.e., Rate of Type 1 error) is low.

Hence, prediction of addresses by the code (given in predicted_address_data.py) is good.













