from typing import Annotated, Literal, Optional
from pydantic import BaseModel, Field, ValidationError, field_validator
from loguru import logger 
import numpy as np

class TransactionRecordModel(BaseModel):
    TransactionID: int
    TransactionAmt: Annotated[float, Field(ge=0)]
    isFraud: Annotated[int, Field(ge=0, le=1)]
    TransactionDT: Annotated[int, Field(ge=0)]
    ProductCD: Literal["W", "C", "R", "S", "H"]
    card4: Optional[Literal["visa", "mastercard", "american express", "discover"]]
    card6: Optional[Literal['debit', 'credit', 'debit or credit', 'charge card']]

    @field_validator(
        'card4', 'card6', mode='before'
    )
    @classmethod
    def process_nan(cls, value):
        if isinstance(value, float) and np.isnan(value):
            return None
        return value

def validate_schema(record: dict) -> bool:
    try:
        TransactionRecordModel(**record)
        return True
    except ValidationError as e:
        logger.error(f"Validation Error: {e}")
        return False