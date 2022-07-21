"""Very advance Employee management system"""
from dataclasses import dataclass, field


@dataclass
class HourlyEmployee:
    """Employee that´s paid based on number of worked hours."""
    name: str
    id: int
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
class SalariedEmployee:
    """Employee that´s paid based on a fixes montly salary."""
    name: str
    id: int
    comission: float = field(default=100)
    contracts_landed: float = field(default=0)
    monthly_salary: float = field(default=0)
    percentage: float = field(default=1)

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.monthly_salary * self.percentage
            + self.comission * self.contracts_landed
        )


@dataclass
class Freelancer:
    """Freelancer that´s paid based on number of worked hours."""
    name: str
    id: int
    comission: float = field(default=100)
    contracts_landed: float = field(default=0)
    pay_rate: float = field(default=0)
    hours_worked: int = field(default=0)
    vat_number: str = field(default="")

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked + self.comission * self.contracts_landed
        )


def main() -> None:
    """Main function."""
    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployee(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )
    # What will happen if requires integrate Comissions, this could be really hard with this approach


if __name__ == "__main__":
    main()