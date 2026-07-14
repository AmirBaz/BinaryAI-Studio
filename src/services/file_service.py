from __future__ import annotations

from pathlib import Path
from typing import Optional

from src.core.binary_file import BinaryFile
from src.core.file_information import FileInformation


class FileService:
    """
    Central service responsible for opening,
    closing and saving binary files.
    """

    def __init__(self) -> None:

        self._current_file: Optional[BinaryFile] = None

    @property
    def current_file(self) -> Optional[BinaryFile]:
        return self._current_file

    @property
    def has_file(self) -> bool:
        return self._current_file is not None

    def open(self, filename: str) -> BinaryFile:

        binary = BinaryFile.open(filename)

        self._current_file = binary

        return binary

    def close(self):

        self._current_file = None

    def save(self):

        if not self.has_file:
            raise RuntimeError("No opened file.")

        self._current_file.save()

    def save_as(self, filename: str):

        if not self.has_file:
            raise RuntimeError("No opened file.")

        self._current_file.save_as(filename)

    def information(self) -> FileInformation:

        if not self.has_file:
            raise RuntimeError("No opened file.")

        return FileInformation(self._current_file)

    def filename(self):

        if not self.has_file:
            return ""

        return self._current_file.filename

    def extension(self):

        if not self.has_file:
            return ""

        return self._current_file.extension

    def filesize(self):

        if not self.has_file:
            return 0

        return self._current_file.size

    def bytes(self):

        if not self.has_file:
            return bytearray()

        return self._current_file.data

    def read(self, offset: int):

        return self._current_file.read_byte(offset)

    def write(self, offset: int, value: int):

        self._current_file.write_byte(offset, value)

    def exists(self):

        if not self.has_file:
            return False

        return self._current_file.exists

    def path(self):

        if not self.has_file:
            return ""

        return str(self._current_file.path)

    def __repr__(self):

        if not self.has_file:
            return "<FileService No File>"

        return f"<FileService {self.filename()}>"