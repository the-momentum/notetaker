from typing import Optional

from pydantic import BaseModel, Field


class SOAPNote(BaseModel):
    """A representation of a SOAP note structure."""

    subjective: Optional[str] = Field(
        description="""The patient's subjective experiences, \
                    including reported symptoms and concerns"""
    )
    objective: Optional[str] = Field(
        description="""Objective observations or findings, \
                    such as vital signs or physical exam results"""
    )
    assessment: Optional[str] = Field(
        description="The clinician's assessment, including diagnoses or evaluations"
    )
    plan: Optional[str] = Field(
        description="The recommended plan, including treatments, tests, or follow-ups"
    )
