# Predict address

## Files
Assignment Instructions.pdf: Contains detail of the assignment (Assignment is done in python). <br/>
test_address.csv: Contains address to be predicted. <br/>
predicted_address_data.py: Contains code to predict address. <br/>
predicted_address_data.csv: Contains predicted address and False Discovery Rate	and False Omission Rates.
<br/>
<br/>
## API used
Google API used to predict address:  <br/>
address = "address_to_search" <br/>
url = 'https://maps.googleapis.com/maps/api/geocode/json?components=country:&language=&region=&bounds=&key=' <br/>
url = url + '&address='+ address.replace(" ","+") <br/>



## Result
False Discovery Rate: 0.026178010471204 <br/>
False Omission Rates: 0.923076923076923 <br/>
Precision: 0.076923076923077 <br/>
Accuracy: 0.916666666666667 <br/>
<br/>
Further, <br/>
Both Precision (i.e., Probability of relevant prediction) and Accuracy is high. <br/>
Also, False Discovery Rate (i.e., Rate of Type 1 error) is low. <br/>
<br/>
Hence, prediction of addresses by the code (given in predicted_address_data.py) is good.













