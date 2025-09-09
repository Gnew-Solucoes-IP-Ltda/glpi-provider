from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.create_session()
print('teste')
provider.close_session()


