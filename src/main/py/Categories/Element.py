class Element:
    """An element containing an amount of money; either income, saving or cost. """

    def __init__(self, name: str, value: float):
        self._name = name
        self._value = value

    def get_value(self) -> float:
        return self._value

    def get_name(self):
        return self._name
