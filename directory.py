import union as union

import files


class Directory:
    """
    Manage directory. Directory can contain Directories or Files.
    """
    def __init__(self):
        self.content = []

    def add_to_directory(self, file: files.File) -> None:
        """
        :param file: Something to insert to the directory.
        """
        self.content.append(file)

    def remove_from_directory(self, file: files.File) -> None:
        """
        :param file: Something to remove from the directory.
        """
        self.content.remove(file)
