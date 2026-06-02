from langchain_core.prompts import ChatPromptTemplate
from app.services.llm_factory import get_groq_llm
from app.models.gps_output import SkillGapAnalysis

def analyze_skill_gap(user_profile_dict: dict) -> SkillGapAnalysis:
    llm = get_groq_llm()
    structured_llm = llm.with_structured_output(SkillGapAnalysis)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an elite Career Tech GPS. Analyze the user's current skills vs their target role. Be highly specific and realistic. Output ONLY valid JSON matching the schema."),
        ("human", "Here is the user profile: {profile}\n\nGenerate a precise skill gap analysis.")
    ])
    
    chain = prompt | structured_llm
    
    response = chain.invoke({"profile": str(user_profile_dict)})
    return response
