import requests
from cv_app_example.settings import BASE_URL

def get(param):
    # Define the API endpoint URL
    url = BASE_URL

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url+param, headers = {'accept': 'application/json'}, verify=False)

        # Check if the request waµs successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            
            print('Error:', response.status_code)
            return None
            
    except Exception as e:
        print(e)
