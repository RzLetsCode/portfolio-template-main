# src/models.py
from pydantic import BaseModel, Field
from typing import List, Optional

class ClaimData(BaseModel):
    client_name: Optional[str] = Field(default=None)
    driver_license_id: Optional[str] = Field(default=None)
    policy_number: Optional[str] = Field(default=None)
    # Adding a default value here prevents the 'Field required' crash
    issue_description: str = Field(default="No description extracted from email.")
    missing_fields: List[str] = Field(default_factory=list)

class DamageAssessment(BaseModel):
    description: str = Field(default="No visual analysis available.")
    severity: str = Field(default="Unknown")