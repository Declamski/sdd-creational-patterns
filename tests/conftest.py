import pytest
from campaign_launchpad.budget import GlobalBudget

@pytest.fixture(autouse=True)
def reset_global_budget_singleton():
    GlobalBudget._instances.clear()
    yield
    GlobalBudget._instances.clear()
