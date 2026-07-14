from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from src.core.binary_file import BinaryFile


MAGIC_SIGNATURES = {
    b"MZ": "Windows Executable",
    b"\x7fELF": "ELF Executable",
    b"\x89PNG": "PNG Image",
    b"\xff\xd8\xff": "JPEG Image",
    b"GIF87a": "GIF Image",
    b"GIF89a": "GIF Image",
    b"%PDF": "PDF Document",
    b"PK\x03\x04": "ZIP Archive",
    b"7z\xbc\xaf\x27\x1c": "7-Zip Archive",
    b"Rar!\x1a\x07": "RAR Archive",
    b"SQLite format 3": "SQLite Database",
}


@dataclass
class FileInformation:
    """
    Metadata extracted from a binary file.
    """

    binary: BinaryFile

    @property
    def filename(self) -> str:
        return self.binary.filename

    @property
    def extension(self) -> str:
        return self.binary.extension

    @property
    def directory(self) -> str:
        return self.binary.directory

    @property
    def size(self) -> int:
        return self.binary.size

    @property
    def exists(self) -> bool:
        return self.binary.exists

    @property
    def magic(self) -> str:

        data = bytes(self.binary.data[:32])

        for signature, description in MAGIC_SIGNATURES.items():

            if data.startswith(signature):
                return description

        return "Unknown"

    @property
    def size_human(self) -> str:

        size = self.size

        units = ["B", "KB", "MB", "GB", "TB"]

        index = 0

        while size >= 1024 and index < len(units) - 1:
            size /= 1024
            index += 1

        return f"{size:.2f} {units[index]}"

    @property
    def path(self) -> str:
        return str(self.binary.path)

    @property
    def suffix(self) -> str:
        return Path(self.binary.path).suffix

    def as_dict(self) -> dict:

        return {

            "Filename": self.filename,
            "Extension": self.extension,
            "Type": self.magic,
            "Directory": self.directory,
            "Size": self.size,
            "Readable Size": self.size_human,
            "Exists": self.exists,
            "Path": self.path

        }

    def __repr__(self):

        return (
            f"<FileInformation "
            f"{self.filename} "
            f"{self.magic} "
            f"{self.size_human}>"
        )