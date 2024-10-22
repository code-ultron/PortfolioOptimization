import requests
import json

# Define the API endpoint
url = 'http://localhost:4000/optimize_portfolio'

# Provide the path to your stock CSV file
file_path = '/Users/amit/Documents/vencortex/dataset/stock_data.csv'
files = {'file': open(file_path, 'rb')}

# Set the total_fund value
data = {'total_fund': 1000}  # Change this value as needed

# Send the POST request to the API
response = requests.post(url, files=files, data=data)

# Check if the response is successful
if response.status_code == 200:
    result = response.json()
    
    # Define the path for saving the output
    output_file_path = '/Users/amit/Documents/vencortex/result/optimization_result.txt'
    
    # Save the JSON data to a text file
    with open(output_file_path, 'w') as file:
        json.dump(result, file, indent=4)
    
    print(f"Optimization result saved to {output_file_path}")
else:
    print(f"Failed to get a successful response: {response.status_code}")
    print(response.text)
