import urllib
from dataclasses import dataclass


@dataclass
class Url:
    scheme: str
    netloc: str
    path: str
    params: str
    query: str
    fragment: str

    def __init__(self, url: str):
        self._url = urllib.parse.urlparse(url)

    @property
    def scheme(self):
        return self._url.scheme

    @property
    def netloc(self):
        return self._url.netloc

    @property
    def path(self):
        return self._url.path

    @property
    def params(self):
        return self._url.path

    @property
    def query(self):
        return self._url.query

    @property
    def fragment(self):
        return self._url.fragment

    @property
    def full(self):
        return urllib.parse.urlunparse(self._url)

    def full_with_attrs(self, *, endpoint_path: str, params: str, extra_params: dict):
        return self.full + endpoint_path + '?' + params + '&' + urllib.parse.urlencode(extra_params)
