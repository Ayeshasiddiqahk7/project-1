import requests
import pandas as pd

# Step 1: Fetch data from the API
print("Fetching data from the API.....")
try:
    # Make the API request
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()  # Parse the JSON response
    print("Data fetched successfully!!!")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()




# Step 2: Process the data
print("Processing data.....")
# Prepare a list of dictionaries for DataFrame creation
processed_data = []
for user in data:
    processed_data.append({
        "Name": user["name"],  # User's name
        "Address": f"{user['address']['street']}, {user['address']['city']}",  # Street and city combined
        "Phone": user["phone"],  # Phone number
        "Email": user["email"]  # Email address
    })



# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(processed_data)
print("Data processed successfully!!!")



# Step 3: Export data to a CSV file
output_file = "user_data.csv"
print(f"Exporting data to {output_file}...")
try:
    # Save DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Data exported successfully to {output_file}!")
except Exception as e:
    print(f"Error exporting data to CSV: {e}")
