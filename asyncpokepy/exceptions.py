"""
The MIT License (MIT)

Copyright (c) 2020 Raj Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class asyncpokepyExceptions(Exception):
    pass

class UnknownPokemon(asyncpokepyExceptions):
    """Raised when an unknown Pokémon is provided
    """
    def __init__(self, error='Unknown Pokémon provided, check for typos.'):
        self.error = error
    def __str__(self):
        return self.error

class UnCaughtError(asyncpokepyExceptions):
    """Raised when an uncaught code is received
    """
    def __init__(self, code, error):
        self.error = f'Received code {code} : {error}'
    def __str__(self):
        return self.error

class URLMoved(asyncpokepyExceptions):
    """Raised when requested URL has moved
    """
    def __init__(self, error='This URL has been moved temporarily or permanently. Check back later.'):
        self.error = error
    def __str__(self):
        return self.error

class AuthorisationError(asyncpokepyExceptions):
    """Raised when authorisation failed
    """
    def __init__(self, error='Your IP address is unathorised to request this URL, you may have been blocked for API abuse, or there may be an internal error.'):
        self.error = error
    def __str__(self):
        return self.error

class MethodNotAllowed(asyncpokepyExceptions):
    """Raised when wrong method is used
    """
    def __init__(self, error='This method (GET/POST) is not allowed for this URL. If you are using a client instance, contact me. If you are using ahttp.py directly, try using the other method.'):
        self.error = error
    def __str__(self):
        return self.error

class RequestTimeout(asyncpokepyExceptions):
    """Raised when authorisation failed
    """
    def __init__(self, error='The request timed out, because it took too long. Try again. If this error persists you or the API may be having connection issues.'):
        self.error = error
    def __str__(self):
        return self.error

class RateLimitation(asyncpokepyExceptions):
    """Raised when you are being ratelimited
    """
    def __init__(self, error='Your IP address is being ratelimited by the API. Try again later. Continued overworking may result in your IP being blocked.'):
        self.error = error
    def __str__(self):
        return self.error

class InternalServerError(asyncpokepyExceptions):
    """Raised when an internal server error occurs
    """
    def __init__(self, error='An internal server error occured that we cannot gather any more information on. Try again later.'):
        self.error = error
    def __str__(self):
        return self.error