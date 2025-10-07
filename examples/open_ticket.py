from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.service._verify_ssl=False
provider.create_session()
response = provider.open_ticket(
    name='Chamado de teste',
    content='Conteudo do chamado',
    requester_id=538,
    entity_id=0,
    location_id=33,
    group_assign_id=2,
)
print(response)
provider.close_session()


