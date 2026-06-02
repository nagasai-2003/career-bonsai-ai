from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Skill(BaseModel):
    name: str
    rating: int = Field(..., ge=1, le=5) # 1 to 5 scale

class UserProfile(BaseModel):
    current_state: str = Field(..., description="Student, Unemployed, or Employee")
    age: int
    skills: List[Skill]
    interests: List[str]
    target_role: str
    
    # Conditional fields based on current_state
    course: Optional[str] = None
    year_semester: Optional[str] = None
    career_gap_months: Optional[int] = None
    gap_activities: Optional[str] = None
    current_role: Optional[str] = None
    
    # Optional Resume Text
    resume_text: Optional[str] = None
