######################################  Predict Address #################################################
import csv
import requests

# Store predicted address in dictionary.
def address_resolver(json, address):
    final = {}
    final['address'] = address
    if json['results']:
        data = json['results'][0]
        final['predicted_address'] = data['formatted_address']
        for item in data['address_components']:
            for category in item['types']:
                data[category] = {}
                data[category] = item['long_name']
        
        final['housenumber'] = data.get("housenumber", None)
        if data.get("subpremise", None) is None or data.get('street_number', None) is None:
            if not (data.get("subpremise", None)) is None:
                final['street_number'] = data.get("subpremise", None)
            elif not (data.get("street_number", None)) is None:
                final['street_number'] = data.get("street_number", None)
            else:
                final['street_number'] = data.get("street_number", None)
                
            
        elif not (data.get("subpremise", None)) is None and not (data.get('street_number', None)) is None:
            final['street_number'] = data.get("subpremise", None) + str(" ") + data.get('street_number', None)
            
        else:
            final['street_number'] = data.get("street_number", None)
#        final['stree_num'] = data.get('street_number', None)
        final['street'] = data.get("route", None)
        
        if data.get("sublocality", None) is None or data.get('sublocality_level_2', None) is None:
            if not (data.get("sublocality", None)) is None:
                final['locality/colony'] = data.get("sublocality", None)
            elif not (data.get("sublocality_level_2", None)) is None:
                final['locality/colony'] = data.get("sublocality_level_2", None)
            
        elif not (data.get("sublocality", None)) is None and not (data.get('sublocality_level_2', None)) is None:
            final['locality/colony'] = data.get("sublocality", None) + str(" ") + data.get('sublocality_level_2', None)
            
        else:
            final['locality/colony'] = "nan"
 
        final['area'] = data.get("administrative_area_level_2", None)
        final['city'] = data.get("locality", None)

        final['postal_code'] = data.get("postal_code", None)
        
        
    return final

# Get the predicted address using google API.
def get_address_details(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?components=country:&language=&region=&bounds=&key=' 
    url = url + '&address='+ address.replace(" ","+")
    response = requests.get(url)
    data  = address_resolver(response.json(), address)
    return data



data = []

# Open the test_address.csv and predict address given in each row.
with open('test_address.csv', "rt") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    ii = 0
    for row in csvreader:
        data.append([])

        address_to_search  = row[0]
        data[ii].append(get_address_details(address_to_search))
        
        ii += 1

# Write result stored in data list to csv file.
with open("predicted_address_data.csv",'w') as csvfile:
    row = 0
    for info in data:
        csvwriter = csv.DictWriter(csvfile, fieldnames=info[0].keys(), quoting= csv.QUOTE_ALL)
        if row == 0:
            csvwriter.writeheader()
            
        csvwriter.writerows(info)
        
        
        row += 1
        
        