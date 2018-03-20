import socket

''' Resolves given domain to the IP address with caching '''
class Resolver:

    def __init__(self):
        self._cache = {}

    ''' Ermöglicht den Aufruf der Objektinstanz als Funktion
        resolver = Resolver()
        resolver() -> calls __call__ method
    '''

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache