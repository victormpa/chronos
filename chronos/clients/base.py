import requests


class Client:
    """Base client."""

    def __init__(self):
        """Create a base client."""

        raise NotImplementedError

    def request(self):
        """Request the API endpoint."""

        raise NotImplementedError

    def ping(self):
        """Ping the server."""

        raise NotImplementedError

    def time(self):
        """Get the server time."""

        raise NotImplementedError
