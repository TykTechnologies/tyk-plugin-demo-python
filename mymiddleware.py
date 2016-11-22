from tyk.decorators import *
from gateway import TykGateway as tyk

@Hook
def MyPreMiddleware(request, session, spec):
    request.add_header('myheader', 'myvalue')
    return request, session
