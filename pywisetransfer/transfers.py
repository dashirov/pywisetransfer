from typing import Any

from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import JsonEndpointWithSCA


class TransfersService(Base):
    transfer = JsonEndpointWithSCA(
        path="/v3/profiles/{profile_id}/transfers/{transaction_id}",
        required_params=[],
    )


class Transfers:
    def __init__(self, client: Client):
        self.service = TransfersService(client=client)

    def transfer(
        self,
        profile_id: str,
        transaction_id: str
    ) -> Any:
        return munchify(
            self.service.transfer(
                profile_id=profile_id,
                transaction_id=transaction_id
            )
        )
