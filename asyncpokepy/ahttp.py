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

import aiohttp
from asyncpokepy.exceptions import *

class ahttp:
    """HTTP function class

    Args:
        session (aiohttp.client.ClientSession, optional): Custom client session if one is needed. Defaults to None.
    """
    def __init__(self):
        self.session=None
        self.baseurl = 'https://pokeapi.co/api/v2/'
        self.codes = {
            301:URLMoved,
            302:URLMoved,
            401:AuthorisationError,
            404:UnknownPokemon,
            405:MethodNotAllowed,
            408:RequestTimeout,
            429:RateLimitation,
            500:InternalServerError
        }

    async def makesession(self):
        """Creates a client session
        """
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def killsession(self):
        """Kills a client session
        """
        if self.session:
            await self.session.close()
            self.session = None

    async def pokeget(self, poke: str):
        """Base get request

        Args:
            poke (str): The pokéapi endpoint
        """
        await self.makesession()
        url = self.baseurl + 'pokemon/' + poke
        async with self.session.get(url) as cs:
            if cs.status == 200:
                try:
                    return await cs.json()
                except aiohttp.ContentTypeError:
                    return await cs.text()
            if cs.status in self.codes:
                exception = self.codes[cs.status]
                raise exception()
            else:
                raise UnCaughtError(code=cs.status, error=cs.reason)
