import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


# class Person:
#     def __init__(self, name: str, address: str):
#         self.name = name
#         self.address = address

#     def __str__(self) -> str:
#         return f"{self.name}, {self.address}"

# @dataclass(kw_only=True)
# @dataclass(match_args=True)
# @dataclass(slots=True)
@dataclass(frozen=False)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    # init=False block user set this value
    id: str = field(init=False, default_factory=generate_id)
    search_string: str = field(init=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="Jonh", address="123 Main St")
    print(person.__dict__["name"])
    print(person)


if __name__ == "__main__":
    main()
