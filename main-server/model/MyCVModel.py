import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class MyCVBasicInformations:
    """
    The basic informations of the author.
    Name, contact informations, ...
    """
    name: str
    email: str
    born: datetime.date


@dataclass(frozen=True)
class MyCV:
    """
    The whole CV. Currently contains only the basic informations.
    """
    basic_info: MyCVBasicInformations