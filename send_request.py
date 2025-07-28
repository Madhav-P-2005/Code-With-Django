import requests      # Import the 'requests' module to send HTTP requests

# Create a file like send_request.py and run it in a second terminal before that run your server using :- python manage.py runserver  

'''
 For API Testing :- 1) Use the Python Script with the help of Terminal  
                     2) Use Postman
'''

# Send a POST request to the Django backend at the specified URL
# response = requests.post('http://localhost:8000/add-todo/', json={"task" : "Buy groceries"})

# print(response.status_code)

# print(response.json())


'''

Output :- 

201
{'id': 2, 'task': 'Buy groceries'}

'''



'''

⭐) Protecting Routes with Middleware :- 

⭐) Sending Token in Subsequent Requests :-  To send the token in subsequent requests, you can include it in the Authorization header. Here's an example of how you can send the token in a request :- 

'''

# url = 'http://127.0.0.1:8000/protected-route/' 

# Authorization token (matches your middleware)
# headers = {
#     'Authorization' : 'Token abc123'
#     }

# response = requests.get(url , headers=headers)


# Display result
# print("Status Code :-  ", response.status_code)
# print("Response :-  ", response.json())




'''

⭐) Implementing Pagination  :- 

Building the Request: Finally, we’ll demonstrate how to make requests to the paginated endpoint and render the tasks in a user-friendly manner.

For instance, checking how many pages of tasks we have would involve making requests in a loop :-

'''

import requests

url = "http://127.0.0.1:8000/get_ToDos_Pagination"

headers = {
    'Authorization': 'Token ImplementingPagination2025'
}

params = {
    'username': 'Madhav P Again for Pagination Testing',  # 👈 Use the exact username you registered
    'page': 4
}

response = requests.get(url, headers=headers, params=params)

print(f"🔹 Page {params['page']} - Status: {response.status_code}")
try:
    data = response.json()
    print("✅ Data:", data)
except Exception as e:
    print("❌ Error decoding JSON.")
    print(response.text)



'''

Output   (python send_request.py) :- 


🔹 Page 1 - Status: 200
✅ Data: {'ToDos': [{'id': 7, 'task': 'Django Task 1', 'completed': False, 'user_id': 3}, {'id': 8, 'task': 'SQL Task 2', 'completed': False, 'user_id': 3}, {'id': 9, 'task': 'MERN Task 3', 'completed': False, 'user_id': 3}]}


🔹 Page 2 - Status: 200
✅ Data: {'ToDos': [{'id': 10, 'task': 'Flask Task 4', 'completed': False, 'user_id': 3}, {'id': 11, 'task': 'AWS Task 6', 'completed': False, 'user_id': 3}, {'id': 12, 'task': 'React Native Task 7', 'completed': False, 'user_id': 3}]}


🔹 Page 3 - Status: 200
✅ Data: {'ToDos': [{'id': 13, 'task': 'Python Task 8', 'completed': False, 'user_id': 3}, {'id': 14, 'task': 'JavaScript Task 9', 'completed': False, 'user_id': 3}]}


🔹 Page 4 - Status: 200
✅ Data: {'ToDos': []}


'''