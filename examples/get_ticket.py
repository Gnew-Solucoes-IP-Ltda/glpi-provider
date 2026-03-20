from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.service._verify_ssl=False
provider.create_session()
# response = provider.service.get_tickets_solutions(15180)
# print(response)
ticket = provider.get_ticket(15180)
print(ticket)
print(ticket.get_last_item_history())
# response = provider.service.get_ticket_users(10867)
# print(response)
#response = provider.service.get_ticket_groups(10867)
#print(response)
provider.close_session()


