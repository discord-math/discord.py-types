from .asset import Asset
from .enums import TeamMembershipState
from .state import ConnectionState
from .types.team import Team as TeamPayload, TeamMember as TeamMemberPayload
from .user import BaseUser
from typing import List, Optional

class Team:
    id: int
    name: str
    owner_id: Optional[int]
    members: List[TeamMember]
    def __init__(self, state: ConnectionState, data: TeamPayload) -> None: ...
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def owner(self) -> Optional[TeamMember]: ...

class TeamMember(BaseUser):
    team: Team
    membership_state: TeamMembershipState
    permissions: List[str]
    def __init__(self, team: Team, state: ConnectionState, data: TeamMemberPayload) -> None: ...
