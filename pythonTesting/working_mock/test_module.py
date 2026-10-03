from unittest.mock import Mock, patch
from my_module import get_user
from requests import HTTPError

import pytest

@patch("my_module.requests.get")
def test_module_correct_output(mock_get):
    mock_get.return_value.json.return_value = {
        "login": "harry",
        "followers": 100000,
        "public_repos": 100
    }
    mock_get.return_for_status = None

    result = get_user("harry")

    assert result["login"] == "harry"
    assert result["followers"] == 100000
    assert result["repo_count"] == 100

@patch("my_module.requests.get")
def test_get_user_raises_404(mock_get):
    # Make raise_for_status raise HTTPError
    mock_get.return_value.raise_for_status.side_effect = HTTPError("404")

    with pytest.raises(HTTPError):
        get_user("does-not-exist")


@patch("my_module.requests.get")
def test_get_user_calls_correct_url(mock_get):
    mock_get.return_value.json.return_value = {
        "login": "x", "followers": 0, "public_repos": 0
    }
    mock_get.return_value.raise_for_status.return_value = None

    get_user("torvalds")

    # Assert the CORRECT URL was called
    mock_get.assert_called_once_with(
        "https://api.github.com/users/torvalds",
        timeout=10,
    )