from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.service._verify_ssl=False
provider.create_session()
print('Teste de sessao criada')
ticket = provider.get_ticket(15180)
print(ticket)
provider.close_session()


