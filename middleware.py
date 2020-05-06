from tyk.decorators import *
from gateway import TykGateway as tyk
from time import time

@Hook
def PreHook(request, session, spec):
    tyk.log("PreHook is called", "info")
    # Inject a header:
    request.add_header("testheader", "testvalue")
    return request, session

@Hook
def PostHook(request, session, spec):
    tyk.log("PostHook is called", "info")
    return request, session

@Hook
def AuthCheck(request, session, metadata, spec):
    tyk.log("AuthCheck is called", "info")

    # request.get_header is a helper method, to get the full header list, use request.object.headers
    auth_header = request.get_header('Authorization')
    if auth_header == '47a0c79c427728b3df4af62b9228c8ae':
        tyk.log("AuthCheck is successful", "info")
        # Initialize a session object:
        session.rate = 1000.0
        session.per = 1.0
        # Set a deadline for the ID extractor, in this case we use the current UNIX timestamp + 60 seconds:
        session.id_extractor_deadline = int(time()) + 60
        # Attach the token, this is required (used internally by Tyk):
        metadata["token"] = "47a0c79c427728b3df4af62b9228c8ae"

        # Inject additional metadata:
        metadata["username"] = "testuser"
        return request, session, metadata
    tyk.log("AuthCheck failed: invalid token", "error")

    # Set a custom error:
    request.object.return_overrides.response_error = 'Invalid authentication'
    request.object.return_overrides.response_code = 403
    return request, session, metadata

@Hook
def PostKeyAuth(request, session, spec):
    tyk.log("PostKeyAuth is called", "info")

    # Log the additional metadata (set in AuthCheck):
    username = session.metadata["username"]
    tyk.log("PostKeyAuth: user '{0}' was authenticated".format(username), "info")
    return request, session

@Hook
def ResponseHook(request, response, session, metadata, spec):
    tyk.log("ResponseHook is called", "info")
    # In this hook we have access to the response object, to inspect it, uncomment the following line:
    # print(response)
    tyk.log("ResponseHook: upstream returned {0}".format(response.status_code), "info")
    return response
