import timeit
from dataclasses import dataclass
from functools import partial


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class EmployeeSlots:
    dept: str


# Slots problem: this feature doesn´t allow multiple inheritance
# class PersonEmployee(PersonSlots, EmployeeSlots):
#     pass


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    person.address
    del person.address


def main():
    person = Person("Jonh", "123 Main St", "jonh@doe.com")
    person_slots = PersonSlots("Jonh", "123 Main St", "jonh@doe.com")
    no_slots = min(timeit.repeat(
        partial(get_set_delete, person), number=1_000_000))
    slots = min(timeit.repeat(
        partial(get_set_delete, person_slots), number=1_000_000))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")
