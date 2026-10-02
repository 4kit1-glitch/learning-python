from unittest.mock import Mock

mock = Mock()

mock.get.return_value.json.return_value = {"bob": "male"}

response = mock.get("url", "header", "timeout")

print(response) # uncomplete walk chain


print(response.json()) # completely walk the chain 


# this simply inscribes that i can set up any behavior for the mock