from providers.glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.create_session()
tickets = provider.get_open_tickets()
provider.close_session()

print(tickets)
