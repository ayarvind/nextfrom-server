from typing import Awaitable, Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from config import EXCLUDED_ENDPOINTS
from utils.jwt_token import verify_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        

        if request.url.path in EXCLUDED_ENDPOINTS:
            return await call_next(request)
        
        token = request.headers.get('x-auth-token')
        if not token:
            return JSONResponse({"error": "Authentication token missing"}, status_code=401)
        data = verify_token(token)
        if not data:
            return JSONResponse({"error": "Invalid or expired token"}, status_code=401)
        request.state.user = data
        return await call_next(request)
