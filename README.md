# GLPI API Abstraction Layer

This project provides an abstraction layer to simplify the use of the GLPI REST API, making it easier to interact with entities, tickets, and users. It offers a Python interface to streamline communication with the GLPI API in an organized and reusable way.

## Repository

Github: https://github.com/Gnew-Solucoes-IP-Ltda/glpi-provider

## Requirements
  - Python 3.10 +
  - Library for GLPI API communication

## Structure

The project includes the `GlpiProvider` class in `glpi_provider`, which encapsulates various methods to interact with the GLPI API:

- **Authentication**:
  - `create_session()`: Creates an authentication session with the API.
  - `close_session()`: Ends the authentication session.

- **Entities**:
  - `get_entity(entity_id: int)`: Retrieves a specific entity by its ID.
  - `get_entities()`: Retrieves all entities.

- **Tickets**:
  - `get_ticket(ticket_id: int)`: Retrieves a specific ticket by its ID.
  - `get_tickets()`: Retrieves all tickets.
  - `get_open_tickets()`: Retrieves only open tickets.

- **Users**:
  - `get_user(user_id: int)`: Retrieves a specific user by their ID.
  - `get_users()`: Retrieves all users.

## Environment Variables

To configure the connection to the GLPI API, create a `.env` file in the project root directory with the following variables:

```env
GLPI_BASE_URL='GLPI_BASE_URL'
GLPI_USER_TOKEN='GLPI_USER_TOKEN'
GLPI_TICKET_STATUS=[1, 2, 3, 4]
```
  - `GLPI_BASE_URL`: The base URL for the GLPI API.
  - `GLPI_USER_TOKEN`: The user token for authenticating API requests.
  - `GLPI_TICKET_STATUS`: A list of ticket statuses to filter tickets when calling methods like get_open_tickets().

## Usage Example

Below is an example of how to use the abstraction layer to retrieve open tickets:

```python
from glpi_provider import GlpiProvider

# Initialize the GLPI provider and create a session
provider = GlpiProvider()
provider.create_session()

# Retrieve and print the list of open tickets
tickets = provider.get_open_tickets()
print(tickets)

# Close the session with the API
provider.close_session()
```
