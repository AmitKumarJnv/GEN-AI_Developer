import pytest
from utils import get_completion

def test_get_completion():
    """
    Testing get-completion function.
    """

    prompt = "What is the capital of india?"
    response = get_completion(prompt)
    assert response is not None
    assert "Delhi" in response