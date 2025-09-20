class Element:
    def __init__(self, value: float, financial_type: str = "income"):
        self._type = financial_type
        if self._type == "cost":
            value = value * -1
        self._value = value

    def get_value(self) -> float:
        return self._value

    def get_type(self):
        return self._type
