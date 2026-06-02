from langchain_core.prompts import ChatPromptTemplate
from app.services.llm_factory import get_groq_llm
from app.models.gps_output import Roadmap

def generate_roadmap(user_profile_dict: dict, skill_gap_dict: dict) -> Roadmap:
    llm = get_groq_llm()
    structured_llm = llm.with_structured_output(Roadmap)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI Career GPS. Based on the user's profile and their missing skills, generate a week-by-week execution roadmap and a custom bridge project to prove their skills."),
        ("human", "User Profile: {profile}\nSkill Gap: {gap}\n\nGenerate the execution roadmap.")
    ])
    
    chain = prompt | structured_llm
    
    response = chain.invoke({
        "profile": str(user_profile_dict),
        "gap": str(skill_gap_dict)
    })
    return response
