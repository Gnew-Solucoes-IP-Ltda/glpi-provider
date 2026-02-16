from datetime import datetime
from unittest import TestCase
from glpi_provider.models import (
    Entity, 
    ItilFollowup, 
    Solution,
    Task,
    Ticket
)


class TicketTestCase(TestCase):

    def test_ticket_instance(self): 
        entity_data = {
            "id": 6,
            "name": "XXXXXXXX - DESENTUPIDORA LTDA - EPP",
            "address": "R MARIA XDXXXXXXXXXX, 15\r\nJD OSASCO",
            "postcode": 'XXXXXXXX',
            "town": "OSASCO",
            "state": "SP",
            "country": "BRASIL",
            "phonenumber": "11 4321-4321",
            "admin_email": "tatianno.alves@gnew.com.br",
            "admin_email_name": "Tatianno"
        }
        entity = Entity(**entity_data)
        ticket_data = {
            'id': 13123,
            'entity': entity,
            'content': '&lt;p&gt;***** RECORRENTE****&lt;/p&gt;&lt;p&gt;\xa0&lt;/p&gt;&lt;p&gt;FAVOR VERIFICAR QUEDA DE LIGAÇÕES (ESTE É O TERCEIRO CHAMADO ABERTO PELO MOTIVO)&lt;/p&gt;', 
            'date_creation': '2024-10-21 15:31:46', 
            'user': None
        }
        ticket = Ticket(**ticket_data)
        self.assertEqual(ticket.id, 13123)
        self.assertEqual(ticket.entity, entity)
        self.assertEqual(ticket.content, '&lt;p&gt;***** RECORRENTE****&lt;/p&gt;&lt;p&gt;\xa0&lt;/p&gt;&lt;p&gt;FAVOR VERIFICAR QUEDA DE LIGAÇÕES (ESTE É O TERCEIRO CHAMADO ABERTO PELO MOTIVO)&lt;/p&gt;')
        self.assertEqual(ticket.date_creation, datetime.strptime('2024-10-21 15:31:46', '%Y-%m-%d %H:%M:%S'))
        self.assertListEqual(ticket.itil_followups, [])
        itilfollowup_data = {
            'id': 1,
            'content': 'teste',
            'date_creation': datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
            'users_id': 2
        }
        itilfollowup = ItilFollowup(**itilfollowup_data)
        ticket.add_itil_followup(itilfollowup)
        self.assertListEqual(ticket.itil_followups, [itilfollowup])
        self.assertListEqual(ticket.tasks, [])
        task_data = {
            'id': 1,
            'content': 'Tarefa 1',
            'date_creation': datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
            'users_id': 2
        }
        task = Task(**task_data)
        ticket.add_task(task)
        self.assertListEqual(ticket.tasks, [task])
        self.assertListEqual(ticket.solutions, [])
        solution_data = {
            'id': 1,
            'content': 'Resolvido 1',
            'date_creation': datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
            'users_id': 2
        }
        solution = Solution(**solution_data)
        ticket.add_solution(solution)
        self.assertListEqual(ticket.solutions, [solution])
    

    def test_itilfollowup_instance(self):
        itilfollowup_data = {
            'id': 1,
            'content': 'teste',
            'date_creation': datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
            'users_id': 2
        }
        itilfollowup = ItilFollowup(**itilfollowup_data)
        self.assertEqual(itilfollowup.id, 1)
        self.assertEqual(itilfollowup.content, 'teste')
        self.assertEqual(itilfollowup.date_creation, datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'))
        self.assertEqual(itilfollowup.users_id, 2)
    
    def test_task_instance(self):
        task_data = {
            'id': 1,
            'content': 'Tarefa 1',
            'date_creation': datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
            'users_id': 2
        }
        task = Task(**task_data)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.content, 'Tarefa 1')
        self.assertEqual(task.date_creation, datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'))
        self.assertEqual(task.users_id, 2)
    
    def test_solution_instance(self):
        solution_data = {
            'id': 1,
            'content': 'Resolvido 1',
            'date_creation': datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
            'users_id': 2
        }
        solution = Solution(**solution_data)
        self.assertEqual(solution.id, 1)
        self.assertEqual(solution.content, 'Resolvido 1')
        self.assertEqual(solution.date_creation, datetime.strptime('2026-02-13 10:00:00', '%Y-%m-%d %H:%M:%S'))
        self.assertEqual(solution.users_id, 2)
        

