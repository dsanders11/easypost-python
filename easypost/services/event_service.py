from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from easypost.easypost_object import convert_to_easypost_object
from easypost.models.event import Event
from easypost.models.payload import Payload
from easypost.requestor import (
    RequestMethod,
    Requestor,
)
from easypost.services.base_service import BaseService


class EventService(BaseService):
    def __init__(self, client):
        self._client = client
        self._model_class = Event.__name__

    def create(self, **params) -> Event:
        """Create an Event."""
        return self._create_resource(self._model_class, **params)

    def all(self, **params) -> List[Event]:
        """Retrieve a list of Events."""
        return self._all_resources(self._model_class, **params)

    def retrieve(self, id) -> Event:
        """Retrieve an Event."""
        return self._retrieve_resource(self._model_class, id)

    def retrieve_all_payloads(self, event_id: str, api_key: Optional[str] = None, **params) -> List[Payload]:
        """Retrieve a list of Payloads for an Event."""
        url = f"{self._class_url(self._model_class)}/{event_id}/payloads"

        response, api_key = Requestor(self._client).request(method=RequestMethod.GET, url=url, params=params)

        return convert_to_easypost_object(response=response, api_key=api_key)

    def retrieve_payload(self, event_id: str, payload_id: str, api_key: Optional[str] = None, **params) -> Payload:
        """Retrieve a Payload of an Event."""
        url = f"{self._class_url(self._model_class)}/{event_id}/payloads/{payload_id}"

        response, api_key = Requestor(self._client).request(method=RequestMethod.GET, url=url, params=params)

        return convert_to_easypost_object(response=response, api_key=api_key)

    def get_next_page(
        self,
        events: Dict[str, Any],
        page_size: int,
        optional_params: Optional[Dict[str, Any]] = None,
    ) -> List[Any]:
        """Retrieve the next page of the List Events response."""
        return self._get_next_page_resources(self._model_class, events, page_size, optional_params)
