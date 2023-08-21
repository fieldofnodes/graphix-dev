class NotAnIntegerException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = f"Value: '{value}' is not an integer"
        super().__init__(self.message)

def test_value_is_integer(value):
    if not isinstance(value, int):
        raise NotAnIntegerException(value)

