from services.glpi_service import GlpiService
from providers.glpi_provider import GlpiProvider
from settings import BASE_URL, USER_TOKEN


service = GlpiService(BASE_URL, USER_TOKEN)
provider = GlpiProvider(service)

provider.create_session()
#tickets = provider.get_open_tickets()
tickets = provider.get_open_tickets_ids()
provider.close_session()

print(tickets)
