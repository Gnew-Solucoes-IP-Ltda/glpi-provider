from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.service._verify_ssl=False
provider.create_session()
response = provider.get_ticket(10867)
# print(response)
# response = provider.service.get_ticket_users(10867)
# print(response)
response = provider.service.get_ticket_groups(10867)
print(response)
provider.close_session()


