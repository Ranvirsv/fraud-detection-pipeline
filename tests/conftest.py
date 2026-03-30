import pytest
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50],
        'col3': [100, 200, 300, 400, 500]
    }
    return pd.DataFrame(data)