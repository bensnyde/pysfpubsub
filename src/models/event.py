from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):

    CreatedDate: int
    CreatedById: str
    Agent_Master_Id__c: str | None
    Certification_Number__c: str
    Effective_Date__c: datetime | None
    FFM_Id__c: str
    Novasys_Primary_Id__c: int | None
    SalesforceId__c: str
    State__c: str
    Status__c: str
    Tech_Awaiting_Novasys_Receipt__c: bool
    Termination_Date__c: datetime | None

    @staticmethod
    def get_example():
        return Event(**{
            "CreatedDate": int(datetime.now().timestamp()),
            "CreatedById": "005R0000000cw06IAA",
            "Agent_Master_Id__c": None,
            "Certification_Number__c": "",
            "Effective_Date__c": None,
            "FFM_Id__c": "",
            "Novasys_Primary_Id__c": None,
            "SalesforceId__c": "005R0000000cw06IAA",
            "State__c": "",
            "Status__c": "Active",
            "Tech_Awaiting_Novasys_Receipt__c": True,
            "Termination_Date__c": None,
        })