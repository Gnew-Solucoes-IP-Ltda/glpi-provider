from datetime import datetime
from dataclasses import dataclass, field
from .entity import Entity
from .user import User


@dataclass
class TicketStatus:
    id: int
    name: str


@dataclass
class ItilFollowup:
    id: int
    content: str
    date_creation: datetime
    users_id: int


@dataclass
class Task:
    id: int
    content: str
    date_creation: datetime
    users_id: int


@dataclass
class Solution:
    id: int
    content: str
    date_creation: datetime
    users_id: int
    

@dataclass
class Ticket: 
    id: int
    entity: Entity
    content: str
    user: User
    date_creation: datetime
    status: TicketStatus
    itil_followups: list[ItilFollowup] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)
    solutions: list[Solution] = field(default_factory=list)

    def __post_init__(self):
        self.date_creation = datetime.strptime(self.date_creation, '%Y-%m-%d %H:%M:%S')
        self.status = self._create_ticket_status(self.status)
    
    def add_itil_followup(self, itil_followup: ItilFollowup):
        self.itil_followups.append(itil_followup)
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def add_solution(self, solution: Solution):
        self.solutions.append(solution)
    
    def _create_ticket_status(self, id: int) -> TicketStatus:
        status_dict = {
            1: 'Aberto',
            2: 'Atribuído',
            3: 'Planejado',
            4: 'Pendente',
            5: 'Solucionado',
            6: 'Fechado',
        }

        if id in status_dict:
            return TicketStatus(id, status_dict[id])
    
    
