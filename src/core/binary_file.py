from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryFile:
    """
    Represents a binary file loaded in memory.
    """

    path: Path
    data: bytearray

    @classmethod
    def open(cls, filename: str) -> "BinaryFile":
        """
        Load a binary file from disk.
        """

        path = Path(filename)

        with path.open("rb") as f:
            content = bytearray(f.read())

        return cls(path=path, data=content)

    @property
    def filename(self) -> str:
        return self.path.name

    @property
    def extension(self) -> str:
        return self.path.suffix.lower()

    @property
    def directory(self) -> str:
        return str(self.path.parent)

    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def exists(self) -> bool:
        return self.path.exists()

    def save(self) -> None:
        """
        Save current data to disk.
        """
        with self.path.open("wb") as f:
            f.write(self.data)

    def save_as(self, filename: str) -> None:
        """
        Save under another filename.
        """
        destination = Path(filename)

        with destination.open("wb") as f:
            f.write(self.data)

        self.path = destination

    def read_byte(self, offset: int) -> int:
        return self.data[offset]

    def write_byte(self, offset: int, value: int) -> None:
        if not 0 <= value <= 255:
            raise ValueError("Byte value must be between 0 and 255.")

        self.data[offset] = value

    def slice(self, start: int, end: int) -> bytes:
        return bytes(self.data[start:end])

    def insert(self, offset: int, value: bytes) -> None:
        self.data[offset:offset] = value

    def delete(self, start: int, length: int) -> None:
        del self.data[start:start + length]

    def checksum(self) -> int:
        return sum(self.data) & 0xFFFFFFFF

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return (
            f"BinaryFile("
            f"filename='{self.filename}', "
            f"size={self.size} bytes)"
        )