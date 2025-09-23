from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.service._verify_ssl=False
provider.create_session()
response = provider.find_entity_by_tag_inventory('123456')
print(response)
provider.close_session()


