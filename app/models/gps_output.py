from pydantic import BaseModel
from typing import List

class MissingSkill(BaseModel):
    skill_name: str
    importance: str # High, Medium, Low
    learning_resource: str

class SkillGapAnalysis(BaseModel):
    current_match_percentage: int
    missing_skills: List[MissingSkill]

class WeeklyAction(BaseModel):
    week_number: int
    focus: str
    tasks: List[str]

class Roadmap(BaseModel):
    estimated_weeks_to_target: int
    weekly_plan: List[WeeklyAction]
    bridge_project: str
