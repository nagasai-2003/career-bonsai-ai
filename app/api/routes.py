from fastapi import APIRouter, HTTPException
from app.models.user_input import UserProfile
from app.services.engine_skills import analyze_skill_gap
from app.services.engine_roadmap import generate_roadmap

router = APIRouter()

@router.post("/api/v1/navigate", summary="Generate the entire Career GPS route")
async def generate_career_gps(profile: UserProfile):
    try:
        # Convert profile to dict for the LLM
        profile_dict = profile.model_dump(exclude_none=True) # Using Pydantic V2 model_dump instead of dict
        
        # 1. Generate Skill Gap (Fast via Groq)
        skill_gap = analyze_skill_gap(profile_dict)
        
        # 2. Generate Roadmap based on that Skill Gap
        roadmap = generate_roadmap(profile_dict, skill_gap.model_dump()) # Using Pydantic V2 model_dump
        
        # 3. Compile the final payload for the frontend
        return {
            "status": "success",
            "data": {
                "profile_summary": profile.target_role,
                "skill_gap_analysis": skill_gap,
                "roadmap": roadmap
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
