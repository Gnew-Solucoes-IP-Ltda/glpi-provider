from glpi_provider import GlpiProvider


provider = GlpiProvider()
provider.service._verify_ssl=False
provider.create_session()
item = provider.get_last_item_history(15180)
print(item.id)
print(item.content)
print(item.date_creation)
print(item.user)
print(item.type)
provider.close_session()


