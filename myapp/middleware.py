# Django-Learning/myapp/middleware.py

# Creating and Using Middleware


class LoggingMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        print(f"Hey I got {request.method} request for '{request.path}'")       

        '''
        
        Output :- 

        Hey I got GET request for '/json/'   
        [21/Jun/2025 08:19:21] "GET /json/ HTTP/1.1" 200 29
        
        '''


        # Get client IP address from request.META dictionary
        Client_IP = request.META.get('REMOTE_ADDR', 'unknown')  # fallback to 'unknown' if key is missing
        
        # Info about the client's browser/device
        HTTP_USER_AGENT = request.META.get('HTTP_USER_AGENT' , 'unknown')
        
        # URL of the page that linked to the current request
        HTTP_REFERER = request.META.get('HTTP_REFERER' , 'unknown')
        
        # Host header sent by the client (e.g., localhost:8000)
        HTTP_HOST = request.META.get('HTTP_HOST' , 'unknown')


        print(f"Hey I got {request.method} request for request from IP Client :-  {Client_IP}")            
           
        '''
        
        Output :- 

        Hey I got GET request for request from IP Client :-  127.0.0.1
        [21/Jun/2025 08:42:24] "GET /json/ HTTP/1.1" 200 29
        
        '''


        print(f"Hey I got {request.method} request from IP User Agent :-  {HTTP_USER_AGENT}")
        

        '''
        
        Output :- 
        
        Hey I got GET request from IP User Agent :-  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
        
        '''


        print(f"Hey I got {request.method} request from IP Http Referer :-  {HTTP_REFERER}")


        '''
        
        Output :- 

        Hey I got GET request from IP Http Referer :-  unknown
        
        '''
        
        print(f"Hey I got {request.method} request from IP Http Host :-  {HTTP_HOST}")


        '''
        
        Output :- 

        Hey I got GET request from IP Http Host :-  127.0.0.1:8000
        
        '''

        response = self.get_response(request)
        return response
    




'''

⭐) Protecting Routes with Middleware :- 

⭐) The AuthMiddleware class checks if the current route is in the unprotected_routes list. If it is, the middleware allows the request to proceed. This is useful for routes like login, register, and logout, which should be accessible to all users regardless of authentication status. Notice, that we use the resolve function to get the current route name.


⭐) If the route is not in the unprotected_routes list, the middleware checks if the request has a valid Authorization header. If not, it returns a 401 Unauthorized response. Notice that the token 'abc123' is hardcoded here for demonstration purposes. In a real-world scenario, you would validate the token against a database.


=> These are two different systems in real life :- 

       a) Session-based auth (uses cookies and Django sessions)

       b) Token-based auth (used in APIs)

       
🔑 You are manually simulating token-based auth :- 

    1) You return a fixed token on login (abc123)

    2) You check that token manually in middleware

    3) If the header is missing or wrong → Access Denied

'''

from django.http import JsonResponse
from django.urls import resolve

class AuthMiddleware:
     
     def __init__(self , get_response):
          self.get_response = get_response


     def __call__(self, request):
        print("🚀 AuthMiddleware triggered")
          
        try:

             # The line returns the view function for the current route , for example, 'www.example.com/login' resolves to 'login'
            current_route = resolve(request.path_info).url_name

            print(f"🔍 Current route: {current_route}")    # Output :- protected_route

        except Exception as e:

            print(f"❌ Failed to resolve route: {e}")

            current_route = None

        # Skip token check for these routes
        unprotected_routes = ['login' , 'register' , 'logout']


        # Only apply authentication for routes NOT in the unprotected list
        if current_route not in unprotected_routes:
            auth_header = request.headers.get('Authorization') #   # 'Authorization' is not user-defined — it's a standard/predefined HTTP header used for sending authentication credentials like tokens, API keys, or basic auth details.

            print(f"🔐 Authorization Header: {auth_header}")

            # if auth_header != 'Token abc123':
            #     print("❌ Access Denied!")
            #     return JsonResponse({'message': 'Access Denied'}, status=401)
            
            if auth_header != 'Token ImplementingPagination2025':
                print("❌ Access Denied!")
                return JsonResponse({'message': 'Access Denied'}, status=401)


        print("✅ Access Granted")

        # return self.get_response(request)

        response = self.get_response(request)
        print("Response :- " , response)   # Output :- Response :-  <JsonResponse status_code=200, "application/json">
        return response 




'''

Input :-  Path :- http://127.0.0.1:8000/protected_route/


Output :-  (Without Headers)

{
    "message": "Access Denied"
}


'''



'''

With Headers :-   Path :- http://127.0.0.1:8000/protected_route/

Input :- 

Key: Authorization
Value: Token abc123



Output :- 

{
    "message": "This is Protected Route !"
}



Way 2 :-   Path :- http://127.0.0.1:8000/protected_route/


Input :- 

Key: Authorization
Value: q4w534523


Output :- 

🚀 AuthMiddleware triggered
🔍 Current route :-  protected_view
🔐 Authorization Header :-  q4w534523
❌ Access Denied!


{
    "message": "Access Denied"
}

'''



'''

Output :-  ⭐) Implementing Pagination


"GET /get_ToDos_Pagination?username=Madhav+P+Again+for+Pagination+Testing&page=3 HTTP/1.1" 200 157
🚀 AuthMiddleware triggered
🔍 Current route: get_ToDos_Pagination
🔐 Authorization Header: Token ImplementingPagination2025
✅ Access Granted
Hey I got GET request for '/get_ToDos_Pagination'
Hey I got GET request for request from IP Client :-  127.0.0.1
Hey I got GET request from IP User Agent :-  python-requests/2.32.4
Hey I got GET request from IP Http Referer :-  unknown
Hey I got GET request from IP Http Host :-  127.0.0.1:8000
Response :-  <JsonResponse status_code=200, "application/json">




Way 2 :- Using Postman :- 

🚀 AuthMiddleware triggered
🔍 Current route: get_ToDos_Pagination
🔐 Authorization Header: Token ImplementingPagination2025
✅ Access Granted
Hey I got GET request for '/get_ToDos_Pagination'
Hey I got GET request for request from IP Client :-  127.0.0.1
Hey I got GET request from IP User Agent :-  PostmanRuntime/7.44.1
Hey I got GET request from IP Http Referer :-  unknown
Hey I got GET request from IP Http Host :-  127.0.0.1:8000
Response :-  <JsonResponse status_code=200, "application/json">
[27/Jul/2025 14:39:22] "GET /get_ToDos_Pagination?username=Madhav%20P%20Again%20for%20Pagination%20Testing&page=1%0A HTTP/1.1" 200 216

'''