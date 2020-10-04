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
from asyncpokepy.ahttp import ahttp
from asyncpokepy.exceptions import *
from asyncpokepy.objects import *

class pokeclient:
    """The main asyncpokepy client
    """
    def __init__(self):
        self.http = ahttp()

    async def closesession(self):
        await self.http.killsession()

    async def makesession(self):
        await self.http.makesession()

    async def getpokemon(self, pokemon:str, object:bool=True):
        """Gets information about a pokemon in either dictionary or object form

        Args:
            pokemon (str): The name of the Pokemon you would like to gather information on
            object (bool, optional): Whether or not to return the pokemon as an object. Defaults to True.

        Returns:
            dict: A dictionary of the pokemon if object is false
            Pokemon: A pokemon object if object is true
        """
        dictionary = await self.http.pokeget(pokemon)
        await self.closesession()
        if not object:
            return dictionary
        elif object:
            object = MakePokemon(dictionary)
            return object
