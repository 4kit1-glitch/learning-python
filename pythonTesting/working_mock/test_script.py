from unittest.mock import Mock

mock = Mock()

 # can take any method, and return any type and returns 
age = mock.get_age(2000)

# you can see the arg it returned with the call_args method

# its behavior can be configured
# like lets return what is returned

mock.get_user.return_value = {"bob": "male"}
print(mock.get_user("harry"))

print(mock.get_user.call_args)  # with a call()
