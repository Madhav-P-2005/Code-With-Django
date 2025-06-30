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