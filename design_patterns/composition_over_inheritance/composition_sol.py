"""Inheritance approach solution"""
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional


class Commission(ABC):
    """Represents a generic commission."""
    @abstractmethod
    def get_payment(self) -> float:
        """Computes the commission to be paid out."""


@dataclass
class ContractCommission(Commission):
    """Represents a commission."""
    commission: float = field(default=100)
    contracts_landed: float = field(default=0)

    def get_payment(self) -> float:
        return self.commission * self.contracts_landed


class Contract(ABC):
    """Represents a contract and payment process for a particular employee."""
    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""


@dataclass
class Employee:
    """Basic representation of an employee at the company."""
    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee that´s paid based on number of worked hours."""
    pay_rate: float = field(default=0)
    hours_worked: int = field(default=0)
    employer_cost: float = field(default=1000)

    def get_payment(self) -> float:
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
        )


@dataclass
class SalariedContract(Contract):
    """Contract type for an employee that´s paid based on a fixed monthly salary."""
    monthly_salary: float = field(default=0)
    percentage: float = field(default=1)

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """Contract type for an employee that´s paid based on freelancer basis."""
    pay_rate: float = field(default=0)
    hours_worked: int = field(default=0)
    vat_number: str = field(default="")

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission)
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
