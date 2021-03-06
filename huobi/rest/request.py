import urllib.parse
from datetime import datetime

import requests

from huobi.rest.endpoints import Endpoint
from huobi.rest.url import Url
from huobi.rest.utils import generate_hmac256_signature


class HuobiRequest:
    default_request_params = {
        'AccessKeyId': None,
        'SignatureMethod': 'HmacSHA256',
        'SignatureVersion': '2',
        'Timestamp': None,
    }

    __slots__ = ('endpoint', 'access_key', 'secret_key', 'url', 'json')

    def __init__(self,
                 *,
                 access_key: str,
                 secret_key: str,
                 endpoint: Endpoint,
                 url: Url,
                 json: dict,
                 ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.endpoint = endpoint
        self.url: Url = url
        self.json: dict = json

    def _build_default_query_params(self):
        """
        We build the default query params
        :return:
        """
        timestamp = datetime.utcnow().isoformat(timespec='seconds')
        params = self.default_request_params
        params.update(dict(AccessKeyId=self.access_key))
        params.update(dict(Timestamp=timestamp))
        params.update(self.endpoint.prepared_query_params)
        return urllib.parse.urlencode(params)

    def _compose_request_url(self):
        params = self._build_default_query_params()
        hmac256signature = generate_hmac256_signature(
            secret_key=self.secret_key,
            url=self.url,
            params=params,
            endpoint=self.endpoint,
        )

        return self.url.full_with_attrs(
            endpoint_path=self.endpoint.path,
            params=params,
            extra_params={'Signature': hmac256signature},
        )

    def execute(self):
        request_url = self._compose_request_url()
        return requests.request(
            method=self.endpoint.method.name,
            url=request_url,
            json=self.json
        )
