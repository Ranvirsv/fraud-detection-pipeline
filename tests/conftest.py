import pytest
import pandas as pd

@pytest.fixture
def valid_record():
    return {
        "TransactionID": 2987000, 
        "TransactionAmt": 1000.00,
        "isFraud": 0,
        "TransactionDT": 1000,
        "ProductCD": "W",
        "card4": "visa",
        "card6": "debit",
        "P_emaildomain": "gmail.com",
        "id_01": 0,
        "id_03": None, 
        "id_07": None
    }

@pytest.fixture
def sample_data():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50],
        'col3': [100, 200, 300, 400, 500]
    }
    return pd.DataFrame(data)