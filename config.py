import os

DATABASE_NAME = 'nextform'



EXCLUDED_ENDPOINTS = [
    '/api/v1/auth',
    '/docs',
    '/health',
    '/openapi.json'


]

JWT = {
    'secrets': os.environ.get('JWT_SECECT_KEY'),
    'algorithm': 'HS256',
    'expires_delta': 3600 * 24 * 28
}