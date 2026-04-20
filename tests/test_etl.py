import pytest
from src.etl.schemas import validate_schema

def test_schema_valid_record(valid_record):
    assert validate_schema(valid_record)

def test_schema_rejects_negative_amount(valid_record):
    valid_record["TransactionAmt"] = -1000.00
    assert not validate_schema(valid_record)

def test_schema_rejects_invalid_fraud_label(valid_record):
    valid_record["isFraud"] = 2
    assert not validate_schema(valid_record)

@pytest.mark.integration
def test_loader_output_shape(data):
    assert len(data) >= 500000

@pytest.mark.integration
def test_loader_no_duplicate_ids(data):
    assert data["TransactionID"].is_unique