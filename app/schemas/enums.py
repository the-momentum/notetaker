from enum import Enum


class NoteFormat(str, Enum):
    TEXT = "Text"
    SOAP = "SOAP"
    PKI_HL7_CDA = "PKI HL7 CDA"
