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