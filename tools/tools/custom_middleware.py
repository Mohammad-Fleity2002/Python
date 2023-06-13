from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("custom middleware before next middleware/view")
        if not request.user.is_authenticated:
            return redirect("/")
    # Code to be executed for each request before
    # the view (and later middleware) are called.
        response = self.get_response(request)
    # Code to be executed for each response after the view is called
        print("custom middleware after response or previous middleware")
        return response
