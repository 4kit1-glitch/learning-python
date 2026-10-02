# side effects
# making the mock raise or return different values

from unittest.mock import Mock
from requests.exceptions import ConnectionError

mock = Mock()


mock.put.side_effect = ConnectionError("no internet")

#mock.put("url") # raises connection error


mock.get.side_effect = [{"login": "alice"}, {"login": "bob"}, {"login": "carol"}, []]

print(mock.get())   # {"login": "alice"}
print(mock.get())   # {"login": "bob"}
print(mock.get())   # {"login": "carol"}
print(mock.get())   # StopIteration error is raised if the next exceeds the side effect limit


# to run a function use the lambda , very powerful cause it can make the mock dynamic

mock.get.side_effect = lambda url: {"url": url}

print(mock.get("https://api.github.com"))  # {"url": "https://api.github.com"}