from tyk.decorators import *
from gateway import TykGateway as tyk

@Hook
def MyPreMiddleware(request, session, spec):
    print("my_middleware: MyPreMiddleware")
    request.add_header('myheader', 'myvalue')
    print(1, request.object, request)
    return request, session

@Hook
def MyPostMiddleware(request, session, spec):
    request.add_header('myheader', 'myvalue')
    print(2, request.object, request)
    return request, session
