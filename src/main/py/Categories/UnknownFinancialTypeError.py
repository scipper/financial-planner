class UnknownFinancialTypeError(Exception):
    def __init__(self, message):
        self.message = "Unknown financial type '" + message + "'"

    def __str__(self):
        return self.message
