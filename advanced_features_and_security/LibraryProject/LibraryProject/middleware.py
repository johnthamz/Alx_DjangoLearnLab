# LibraryProject/middleware.py
class ContentSecurityPolicyMiddleware:
    """
    Adds a basic Content Security Policy (CSP) header to every response.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # adjust CSP as needed
        self.csp_policy = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; object-src 'none'; frame-ancestors 'none';"

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = self.csp_policy
        return response
