class User:
    """
    A user class.

    Manage print functions.
    Args:
        user_name: User name.
        password: Password.
        user_type: User type. Should be 'manager' or 'regular'
    """
    def __init__(self, user_name: str, password: int, user_type: str):
        self.user_name = user_name
        self.password = password
        self.user_type = user_type

    def __str__(self):
        return f'Name: {self.user_name} type: {self.user_type}'

    def __repr__(self):
        return self.__str__()

