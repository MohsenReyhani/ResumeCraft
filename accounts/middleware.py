from django.shortcuts import redirect
from django.urls import reverse

class SessionExpiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # List of paths to exclude from the redirect
        self.exclude_paths = [
            '/app/accounts/login/',
            '/app/accounts/send-code/',
            '/app/accounts/verify-sms-code/',
            '/app/accounts/logout/',
            '/app/admin/logout/',
            '/app/logout/',
            # Add other paths you want to exclude
        ]

    def __call__(self, request):
        response = self.get_response(request)

        # if request.path.startswith('/app/static/'):  # Bypass middleware for static files
        #     return response

        # # Check if the user is not authenticated and the path is not in the exclude list
        # if not request.user.is_authenticated:
        #     # Special handling for '/app/'
        #     if request.path == '/app/':
        #         return redirect('/app/accounts/login/')  # No 'next' parameter
        #     # General handling for other paths
        #     elif not any(exclude_path in request.path for exclude_path in self.exclude_paths):
        #         return redirect('/app/accounts/login/?next=' + request.path)

        return response