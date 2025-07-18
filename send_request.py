import requests      # Import the 'requests' module to send HTTP requests

# Create a file like send_request.py and run it in a second terminal before that run your server using :- python manage.py runserver  

'''
 For API Testing :- 1) Use the Python Script with the help of Terminal  
                     2) Use Postman
'''

# Send a POST request to the Django backend at the specified URL
response = requests.post('http://localhost:8000/add-todo/', json={"task" : "Buy groceries"})

print(response.status_code)

print(response.json())


'''

Output :- 

201
{'id': 2, 'task': 'Buy groceries'}

'''



'''

⭐) Protecting Routes with Middleware :- 

⭐) Sending Token in Subsequent Requests :-  To send the token in subsequent requests, you can include it in the Authorization header. Here's an example of how you can send the token in a request :- 

'''

url = 'http://127.0.0.1:8000/protected-route/' 

# Authorization token (matches your middleware)
headers = {
    'Authorization' : 'Token abc123'
    }

response = requests.get(url , headers=headers)


# Display result
print("Status Code :-  ", response.status_code)
print("Response :-  ", response.json())