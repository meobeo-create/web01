from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from app.models import Team, TeamCreate, TeamPublic, HeroPublic
from app.database import SessionDep

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("", response_model=TeamPublic, status_code=status.HTTP_201_CREATED, summary="Create a team")
def create_team(team_in: TeamCreate, session: SessionDep):
    team = Team.model_validate(team_in)
    session.add(team)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="Team name already exists")
    session.refresh(team)
    return team

@router.get("/{team_id}/heroes", response_model=list[HeroPublic], summary="List the heroes of a team")
def list_team_heroes(team_id: int, session: SessionDep):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.heroes

@router.get("", response_model=list[TeamPublic])
def list_teams(session: SessionDep):
    return session.exec(select(Team)).all()