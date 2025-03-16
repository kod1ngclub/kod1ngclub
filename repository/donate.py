from model.donate.plan import DonatePlan

from abc import ABC, abstractmethod

class DonateRepository(ABC):
    @abstractmethod
    def ReadDonatePlans() -> list[DonatePlan]:
        pass

