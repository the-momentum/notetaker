from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class VisitTypeEnum(str, Enum):
    """Enumeration of visit types."""

    INITIAL = "Initial Visit"
    FOLLOW_UP = "Follow-up Visit"
    SPECIALIST = "Specialist Consultation"


class VisitDateAndLocation(BaseModel):
    date: Optional[datetime] = Field(description="The date of the visit.")
    location: Optional[str] = Field(description="The location of the visit.")


class NextVisit(BaseModel):
    date: Optional[datetime] = Field(description="Suggested date for the next visit.")
    type: Optional[VisitTypeEnum] = Field(
        description="The type of the next visit, as defined in the enumeration."
    )


class ContextOfVisit(BaseModel):
    chief_complaint: Optional[str] = Field(
        description="The main reason for the patient's visit."
    )
    visit_type: Optional[VisitTypeEnum] = Field(
        description="The type of visit, as defined in the enumeration."
    )
    visit_date_and_location: Optional[VisitDateAndLocation] = Field(
        description="The date and location of the visit."
    )


class SubjectiveHistory(BaseModel):
    current_illness_history: Optional[str] = Field(
        description="Detailed description of current complaints, their duration, and circumstances."  # noqa
    )
    past_medical_history: Optional[str] = Field(
        description="Previous diagnoses, hospitalizations, and surgeries."
    )
    chronic_conditions: Optional[str] = Field(
        description="Information about chronic illnesses (e.g., diabetes, hypertension)."  # noqa
    )
    family_history: Optional[str] = Field(
        description="Information on hereditary diseases, cancers, or cardiac conditions in the family."  # noqa
    )
    social_history: Optional[str] = Field(
        description="Lifestyle factors (e.g., substance use, diet, physical activity, environmental factors)."  # noqa
    )
    allergies: Optional[str] = Field(
        description="List of confirmed allergies (e.g., food, drug-related)."
    )


class PhysicalExamination(BaseModel):
    general_state: Optional[str] = Field(
        description="General appearance, nutritional status, posture."
    )
    vital_signs: Optional[str] = Field(
        description="Vital signs such as blood pressure, heart rate, temperature, and oxygen saturation."  # noqa
    )
    system_examinations: Optional[str] = Field(
        description="Findings from examinations of various systems (e.g., cardiovascular, respiratory, gastrointestinal)."  # noqa
    )


class DiagnosesAndProblems(BaseModel):
    provisional_and_final_diagnoses: Optional[str] = Field(
        description="Preliminary and final diagnoses, including ICD-10 codes if applicable."  # noqa
    )
    problem_list: Optional[str] = Field(
        description="Health problems requiring observation, even if no ICD-10 code is assigned."  # noqa
    )


class OrderedDiagnostics(BaseModel):
    laboratory_tests: Optional[str] = Field(
        description="List of ordered lab tests with their purposes."
    )
    imaging_and_other_tests: Optional[str] = Field(
        description="Imaging or other diagnostic tests (e.g., X-ray, CT, MRI)."
    )


class TreatmentAndRecommendations(BaseModel):
    pharmacological_treatment: Optional[str] = Field(
        description="Prescribed medications, dosages, and treatment durations."
    )
    non_pharmacological_recommendations: Optional[str] = Field(
        description="Recommendations regarding diet, physical activity, and physiotherapy."  # noqa
    )
    referrals: Optional[str] = Field(
        description="Referrals to specialists, diagnostics, or rehabilitation."
    )
    prescriptions: Optional[str] = Field(
        description="Generated prescriptions, including e-prescription numbers and validity dates."  # noqa
    )


class FollowUpAndObservationPlan(BaseModel):
    next_visit: Optional[NextVisit] = Field(
        description="Details about the suggested next visit."
    )
    monitoring: Optional[str] = Field(
        description="Symptoms to monitor, including alarm signals requiring intervention."  # noqa
    )


class VisitSummary(BaseModel):
    key_findings_summary: Optional[str] = Field(
        description="Brief summary of diagnoses, therapeutic decisions, and next steps."
    )
    physician_notes: Optional[str] = Field(
        description="Additional comments, including patient cooperation and risk assessments."  # noqa
    )


class PKIHL7CDANote(BaseModel):
    context_of_visit: Optional[ContextOfVisit] = Field(
        description="Information about the context of the visit."
    )
    subjective_history: Optional[SubjectiveHistory] = Field(
        description="Patient's subjective history and reported symptoms."
    )
    physical_examination: Optional[PhysicalExamination] = Field(
        description="Objective findings from the physical examination."
    )
    diagnoses_and_problems: Optional[DiagnosesAndProblems] = Field(
        description="Diagnoses and identified health problems."
    )
    ordered_diagnostics: Optional[OrderedDiagnostics] = Field(
        description="Ordered diagnostic tests and their purposes."
    )
    treatment_and_recommendations: Optional[TreatmentAndRecommendations] = Field(
        description="Treatment plans and recommendations for the patient."
    )
    follow_up_and_observation_plan: Optional[FollowUpAndObservationPlan] = Field(
        description="Plans for follow-up visits and patient monitoring."
    )
    visit_summary: Optional[VisitSummary] = Field(
        description="Summary of the visit, including key findings and physician notes."
    )
