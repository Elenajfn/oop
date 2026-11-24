from dataclasses import dataclass, replace
from typing import Optional


# 1. The Product
@dataclass
class Employee:
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    department: str = ""
    position: str = ""
    salary: float = 0.0
    start_date: Optional[str] = None
    manager_id: Optional[int] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None
    has_parking: bool = False
    has_laptop: bool = False
    has_vpn_access: bool = False
    has_admin_rights: bool = False
    office_location: Optional[str] = None
    contract_type: str = "permanent"


# 2. The Builder
class EmployeeBuilder:
    def __init__(self):
        self._employee = Employee()

    def with_name(self, first_name: str, last_name: str):
        self._employee.first_name = first_name
        self._employee.last_name = last_name
        return self

    def with_email(self, email: str):
        self._employee.email = email
        return self

    def with_job(self, department: str, position: str, salary: float):
        self._employee.department = department
        self._employee.position = position
        self._employee.salary = salary
        return self

    def with_start_date(self, start_date: str):
        self._employee.start_date = start_date
        return self

    def with_manager(self, manager_id: int):
        self._employee.manager_id = manager_id
        return self

    def with_contact(self, phone=None, address=None, emergency_contact=None):
        self._employee.phone = phone
        self._employee.address = address
        self._employee.emergency_contact = emergency_contact
        return self

    def with_office(self, office_location: str):
        self._employee.office_location = office_location
        return self

    def with_contract(self, contract_type: str):
        self._employee.contract_type = contract_type
        return self

    def with_equipment(self, laptop: bool = False, parking: bool = False):
        self._employee.has_laptop = laptop
        self._employee.has_parking = parking
        return self

    def with_access(self, vpn: bool = False, admin: bool = False):
        self._employee.has_vpn_access = vpn
        self._employee.has_admin_rights = admin
        return self

    def build(self) -> Employee:
        employee = self._employee
        if not employee.first_name or not employee.last_name:
            raise ValueError("Name is required")
        if not employee.email or "@" not in employee.email:
            raise ValueError("Valid email is required")
        if employee.salary < 0:
            raise ValueError("Salary cannot be negative")
        return replace(employee)


class DeveloperBuilder(EmployeeBuilder):
    def __init__(self, first_name: str, last_name: str, email: str):
        super().__init__()
        self.with_name(first_name, last_name)
        self.with_email(email)
        self.with_job("Engineering", "Developer", 50000)
        self.with_equipment(laptop=True)
        self.with_access(vpn=True, admin=True)


if __name__ == "__main__":
    employee = (
        EmployeeBuilder()
        .with_name("John", "Doe")
        .with_email("john.doe@company.com")
        .with_job("Engineering", "Senior Developer", 75000)
        .with_equipment(laptop=True, parking=False)
        .with_access(vpn=True, admin=True)
        .build()
    )
    print(employee)

    dev = DeveloperBuilder("John", "Doe", "john.doe@company.com").build()
    print(dev)

    intern = (
        EmployeeBuilder()
        .with_name("Jane", "Smith")
        .with_email("jane.smith@company.com")
        .with_job("Marketing", "Intern", 15000)
        .with_start_date("2024-02-01")
        .with_manager(42)
        .with_office("Paris HQ")
        .with_contract("internship")
        .with_equipment(laptop=True)
        .build()
    )
    print(intern)
