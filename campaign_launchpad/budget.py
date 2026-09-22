
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    wrapper._instances = instances
    return wrapper


@singleton
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """

    def __init__(self, initial_amount: float = 0.0):
        self._balance = initial_amount

    def allocate(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Allocation amount must be positive")
        if amount > self._balance:
            raise ValueError("You don't have enough budget for this")
        self._balance -= amount

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
