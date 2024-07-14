import requests

def getApi():
    try:
        response = requests.get('http://localhost:3000/sensor_data')
        response.raise_for_status()  # Raise an error for bad status codes (4xx and 5xx)
        
        # Optionally, print details for debugging
        print("Status Code:", response.status_code)
        print("Content-Type:", response.headers['content-type'])
        print("Encoding:", response.encoding)
        print("Response Text:", response.text)
        
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

response = getApi()
if response is not None:
    print(response)
