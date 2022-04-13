from builtins import any
import directory
import user


class File:
    """
    A file class.

    Args:
        file_name: File name.
        size: Size in KB.
        file_body: Everything you want to enter to file.
        owner: Who create the file.
    """
    def __init__(self, file_name: str, size: int, file_body: any, owner: user.User):
        self.file_name = file_name
        self.size = size
        self.file_body = file_body
        self.owner = owner

    def read(self, user: user.User):
        """
        :param user: Who wants to read the file.
        :return: If user can read the file - file, else error message.
        """
        if self.owner is user or user.user_type == "manager":
            return self
        else:
            return "You don't have permission to read this file."

    def __str__(self):
        return f'File name: {self.file_name}\n' \
               f'File body: {self.file_body}\n' \
               f'Size {self.size} KB'


class BinaryFile(File):
    """
    Implement binary file.
    Inherit from File and __init__ is same File.
    """
    pass


class PictureBinaryFile(BinaryFile):
    """
    Implement Picture binary file.
    Inherit from BinaryFile and __init__ is same File.
    """
    def get_dimensions(self):
        """
        :return: The dimensions of picture.
        """
        pass


class TextFile(File):
    """
    Implement text file.
    Inherit from File and __init__ is same File.
    """
    def count(self, substring: str) -> int:
        """
        :param substring: Substring to looking for.
        :return: How many times substring in file
        """
        return self.file_body.count(substring)

    def __str__(self):
        return super().__str__() + f'{self.file_body}'


if __name__ == '__main__':
    yinon = user.User("Yinon", 123, "manager")
    tzomi = user.User("Tzomi", 123, "regular")
    another_user = user.User("Another", 123, "regular")

    text1 = TextFile("My text1", 10, "body text1", yinon)
    text2 = TextFile("My text2", 10, "body text2", tzomi)
    text3 = TextFile("My text3", 10, "body text3", another_user)

    # Test if user can read his files.
    should_be_work1 = text1.read(yinon)

    # Test if manager can read any files.
    should_be_work2 = text2.read(yinon)

    # Test if regular user can read any files.
    error_msg = text2.read(another_user)

    print(should_be_work1)
    print(should_be_work2)
    print(error_msg)

    my_dir = directory.Directory()
    my_dir.add_to_directory(text1)
    my_dir.add_to_directory(text2)
    my_dir.add_to_directory(text3)

    # Check if directory can take another directory
    another_dir = directory.Directory()
    another_dir.add_to_directory(my_dir)
