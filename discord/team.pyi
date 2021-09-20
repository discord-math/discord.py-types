from .asset import Asset
from .enums import TeamMembershipState
from .user import BaseUser
from typing import List, Optional

class Team:
    id: int
    name: str
    owner_id: int
    members: List[TeamMember]
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def owner(self) -> Optional[TeamMember]: ...

class TeamMember(BaseUser):
    team: Team
    membership_state: TeamMembershipState
    permissions: List[str]
