from typing import Annotated, Optional

from pydantic import BaseModel, Field


class TherapyAssessmentNote(BaseModel):
    """A representation of a therapy note structure."""

    alliance: Annotated[
        int, Field(ge=1, le=5, description="Therapeutic relationship (1-5)")
    ]
    communication: Annotated[
        int, Field(ge=1, le=5, description="Communication skills (1-5)")
    ]
    ethics: Annotated[
        int, Field(ge=1, le=5, description="Professionalism and ethics (1-5)")
    ]
    effectiveness: Annotated[
        int, Field(ge=1, le=5, description="Overall effectiveness (1-5)")
    ]

    strengths: Optional[str] = Field(description="Main strengths of the therapist")
    improvements: Optional[str] = Field(
        description="Suggested improvements for the therapist"
    )
