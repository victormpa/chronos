from .base import Client


class BinanceClient(Client):
    """Binance client."""

    def __init__(self, key, secret):
        """
        Create a Binance client.

        :param key: The API key or the OS variable environment containing the
        key value
        :type key: str

        :param secret: The API secret or the OS variable environment containing
        the secret value
        :type secret: str
        """
        pass

    def ping(self):
        """Check the server connection."""

        request = {
            'endpoint': 'exchangeInfo',
        }

        self.request()
