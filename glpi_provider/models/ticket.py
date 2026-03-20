from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass, field
from .entity import Entity
from .user import User


class ItemHistoryAbstract(ABC):
    id: int
    content: str
    date_creation: datetime
    users_id: int

    @abstractmethod
    def type(self) -> str:
        pass


class ItemHistory:

    def __init__(self, id: int, content: str, date_creation: datetime, user: User, type: str):
        self.id = id
        self.content = content
        self.date_creation = date_creation
        self.user = user
        self.type = type


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
    
    @property
    def type(self) -> str:
        return 'ItilFollowup'


@dataclass
class Task:
    id: int
    content: str
    date_creation: datetime
    users_id: int
    
    @property
    def type(self) -> str:
        return 'Task'


@dataclass
class Solution:
    id: int
    content: str
    date_creation: datetime
    users_id: int

    @property
    def type(self) -> str:
        return 'Solution'

    
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
    
    def get_last_item_history(self) -> ItemHistoryAbstract:
        item_history = None

        if len(self.itil_followups) != 0:
            item_history = self.itil_followups[-1]
        
        if len(self.tasks) != 0:
            last_task = self.tasks[-1]

            if not item_history:
                item_history = last_task
            else:
                if item_history.date_creation < last_task.date_creation:
                    item_history = last_task
        
        if len(self.solutions) != 0:
            last_solution = self.solutions[-1]

            if not item_history:
                item_history = last_solution
            else:
                if item_history.date_creation < last_solution.date_creation:
                    item_history = last_solution
        
        return item_history
    
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
    
    
