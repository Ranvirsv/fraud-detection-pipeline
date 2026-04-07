import pytest
import copy

def test_schema_valid_record(valid_record):
    assert validate_schema(valid_record) == True

def test_schema_rejects_negative_amount(valid_record):
    valid_record["TransactionAmt"] = -1000.00
    assert validate_schema(valid_record) == False

def test_schema_rejects_invalid_fraud_label(valid_record):
    valid_record["isFraud"] = 2
    assert validate_schema(valid_record) == False

@pytest.mark.integration
def test_loader_output_shape(data):
    assert len(data) >= 500000

@pytest.mark.integration
def test_loader_no_duplicate_ids(data):
    assert data["TransactionID"].is_unique