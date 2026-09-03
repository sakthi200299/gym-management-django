# Equivalent to Spring Boot's SecurityConfig
# Only job: check public routes and inject JwtAuthFilter for protected routes

from accounts.security.jwt_auth_filter import JwtAuthFilter

PUBLIC_ROUTES = {
    "/api/gym/users/": ["POST"],
    "/api/gym/users/login/": ["POST"],
    "/health/": ["GET"],
}


class SecurityConfig:

    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_filter = JwtAuthFilter(get_response)  # addFilterBefore equivalent

    def __call__(self, request):
        request.csrf_processing_done = True  # csrf.disable() equivalent
        if self._is_public_route(request.path, request.method):
            return self.get_response(request)   # permitAll — skip JwtAuthFilter
        return self.jwt_filter(request)         # protected — inject JwtAuthFilter

    def _is_public_route(self, path, method):
        path = path if path.endswith("/") else f"{path}/"
        allowed_methods = PUBLIC_ROUTES.get(path)
        return allowed_methods and method in allowed_methods
