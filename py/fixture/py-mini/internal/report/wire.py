"""Wiring of the reporter for one-off announcements."""

from typing import TextIO

from internal.report.catalog import Catalog
from internal.report.reporter import Reporter, Sink


def announce(w: TextIO, catalog: Catalog, name: str) -> None:
    """Write the catalog event for name to w, if the catalog knows the device."""
    sink = Sink(w)
    rep = Reporter(sink, None, None)
    d = catalog.find(name)
    if d is not None:
        rep.record(d.event())
