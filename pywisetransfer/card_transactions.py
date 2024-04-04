from typing import Any

from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import JsonEndpointWithSCA


class CardTransactionsService(Base):
    card_transaction = JsonEndpointWithSCA(
        path="/v3/profiles/{profile_id}/card-transactions/{transaction_id}",
        required_params=[],
    )


class CardTransactions:
    def __init__(self, client: Client):
        self.service = CardTransactionsService(client=client)

    def card_transaction(
        self,
        profile_id: str,
        transaction_id: str
    ) -> Any:
        return munchify(
            self.service.card_transaction(
                profile_id=profile_id,
                transaction_id=transaction_id
            )
        )
