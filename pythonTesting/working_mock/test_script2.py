from unittest.mock import Mock

mock = Mock()

mock.get.return_value.json.return_value = {"bob": "male"}
mock.put.return_value.status.return_value = True

response = mock.get("url", "header", "timeout")

print(response) # uncomplete walk chain


print(response.json()) # completely walk the chain 


# this simply inscribes that i can set up any behavior for the mock

response = mock.put(1000)

print(response.status())

# it seems that i can just add any method to it unless a paticular return value is given oto it