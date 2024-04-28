import requests 
import json

# Make the API call
url = "https://swe-endangered-animals.appspot.com/single_animal_data?animal_name=Semi-collared Hawk"
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    print(f"Status code: {r.status_code}")

    try:
        response_dict = r.json()
        response_string = json.dumps(response_dict, indent=4)
        print(response_string)
    except json.decoder.JSONDecodeError:
        print("Error: Response is not valid JSON.")
else:
    print(f"Error: {r.status_code}")
