"""The identifier a device reports in its heartbeats."""

from typing import Self

_MAX_LEN = 64


class DeviceID(str):
    """The identifier a device reports in its heartbeats."""

    @classmethod
    def parse(cls, raw: str) -> Self:
        """Validate raw and return it as a DeviceID."""
        raw = raw.strip()
        if not raw:
            raise ValueError("device id: empty")
        if len(raw) > _MAX_LEN:
            raise ValueError(f"device id: {len(raw)} chars, want at most {_MAX_LEN}")
        return cls(raw)
