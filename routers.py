from fastapi import APIRouter
from pydantic import BaseModel
import re

router = APIRouter(prefix='/user')


# Простой список навыков
SKILLS = ["python", "java", "c++", "sql", "fastapi", "docker", "aws", "linux", "git"]

class UserResume(BaseModel):
    text: str


def extract_skills(txt: str):
    txt = txt.lower()
    found_skills = set()
    for skill in SKILLS:
        if skill in txt.split():
            print(skill)
            found_skills.add(skill)

    return found_skills


@router.post('/get_skills')
async def get_skills(data: UserResume):
    skills = extract_skills(data.text)
    return {"skills": list(skills)}