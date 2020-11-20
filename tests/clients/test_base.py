import pytest

from chronos.clients.base import Client


def test_client_init():
    """Test the client initialization."""

    with pytest.raises(NotImplementedError):

        client = Client()
