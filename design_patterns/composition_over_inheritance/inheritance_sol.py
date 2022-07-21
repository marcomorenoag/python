"""Inheritance approach solution"""
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


class Employee(ABC):
    """Basic representation of an employee at the company."""
    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""


@dataclass
class HourlyEmployee(Employee):
    """Employee that´s paid based on number of worked hours."""
    comission: float = field(default=100)
    contracts_landed: float = field(default=0)
    pay_rate: float = field(default=0)
    hours_worked: int = field(default=0)
    employer_cost: float = field(default=1000)

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.comission * self.contracts_landed
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that´s paid based on a fixes montly salary."""
    monthly_salary: float = field(default=0)
    percentage: float = field(default=1)

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.monthly_salary * self.percentage
        )


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that´s paid based on a fixes montly salary and that gets a commission."""
    comission: float = field(default=100)
    contracts_landed: float = field(default=0)

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            super().compute_pay()
            + self.comission * self.contracts_landed
        )


@dataclass
class Freelancer(Employee):
    """Freelancer that´s paid based on number of worked hours."""
    pay_rate: float = field(default=0)
    hours_worked: int = field(default=0)
    vat_number: str = field(default="")

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
        )


@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer that´s paid based on number of worked hours and that gets a commission."""
    comission: float = field(default=100)
    contracts_landed: float = field(default=0)

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
           super().compute_pay() + self.comission * self.contracts_landed
        )


def main() -> None:
    """Main function."""
    henry = HourlyEmployee(name="Henry", id=12346,
                           pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
