"""The devices the reporter knows how to announce."""

from dataclasses import dataclass

from internal.report.reporter import Event


@dataclass(frozen=True)
class Device:
    """A device known to the catalog."""

    name: str
    model: str

    def event(self) -> Event:
        """Return the catalog event for the device."""
        return Event(kind="catalog", subject=self.name + "/" + self.model)


class Catalog:
    """A catalog of devices."""

    def __init__(self, devices: list[Device]) -> None:
        """Create a Catalog holding its own copy of devices."""
        self._devices = list(devices)

    def find(self, name: str) -> Device | None:
        """Find the device by name."""
        for d in self._devices:
            if d.name == name:
                return d
        return None
