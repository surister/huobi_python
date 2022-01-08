import base64
import hashlib
import hmac


from huobi.rest.endpoints import Endpoint
from huobi.rest.url import Url


def generate_hmac256_signature(
        secret_key: str,
        params: str,
        url: Url,
        endpoint: Endpoint,
):

    msg = f"{endpoint.method.name}\n{url.netloc}\n{endpoint.path}\n" + params

    _hash = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=msg.encode('utf-8'),
        digestmod=hashlib.sha256,
    ).digest()

    return base64.b64encode(_hash).decode('utf-8')
