import json, requests
from utils.url import url_transform


class GlpiServiceException(Exception):

    def __init__(self, message: str) -> None:
        self.message = message


class GlpiService:

    def __init__(self, base_url: str, user_token: str, requests_lib: requests = requests) -> None:
        self.base_url = url_transform(base_url)
        self._user_token = user_token
        self._requests = requests_lib
        self._session_token: str = None


    def get_ticket(self, ticket_id: int) -> dict:

        if not self._session_token:
            raise GlpiServiceException('Session not initialized')
        
        url = f'{self.base_url}/apirest.php/ticket/{ticket_id}'
        response = self.get(url)

        if response.status_code != 200:
            raise GlpiServiceException(f'Response status code {response.status_code}')
        
        return response.json()

    def add_comment(self, ticket_id: int, comment: str) -> dict:
        data = {
            'input': {
                "itemtype": "Ticket",
                "items_id": {ticket_id},
                'content': comment, 
                'is_private': False
            }
        }
        headers = {'Session-Token': f'{self._get_session_token()}', 'Content-Type': 'application/json'}
        url = f'{self.base_url}/apirest.php/ticket/{ticket_id}/ITILFollowup/'
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers
        )
        
        if response.status_code != 201:
            raise GlpiServiceException(f'Response status code {response.status_code}')
        
        return response.json()

    
    def get(self, url: str) -> requests.Response:

        if not self._session_token:
            raise GlpiServiceException('Session not initialized')

        headers = {'Session-Token': f'{self._get_session_token()}'}
        response = self._requests.get(url, headers=headers)       
        return response
    
    def _get_session_token(self) -> str:

        if not self._session_token:
            url = f'{self.base_url}/apirest.php/initSession/'
            headers = {'Authorization': f'user_token {self._user_token}'}
            response = self._requests.get(url, headers=headers)

            if response.status_code != 200:
                raise GlpiServiceException(f'Response status code {response.status_code}')

            self._session_token = response.json().get('session_token')
            
        return self._session_token
    

    def _kill_session_token(self) -> None:

        if self._session_token:
            url = f'{self.base_url}/apirest.php/killSession/'
            headers = {'Session-Token': f'{self._get_session_token()}'}
            response = self._requests.get(url, headers=headers)

            if response.status_code != 200:
                raise GlpiServiceException(f'Response status code {response.status_code}')

            self._session_token = None