from typing import Any

from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import JsonEndpointWithSCA
from enum import Enum


class Status(str, Enum):
    REQUIRES_ATTENTION = 'REQUIRES_ATTENTION'
    IN_PROGRESS = 'IN_PROGRESS'
    UPCOMING = 'UPCOMING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class ActivitiesType(str, Enum):
    ACQUIRING_PAYMENT = 'ACQUIRING_PAYMENT'
    AUTO_CONVERSION = 'AUTO_CONVERSION'
    BALANCE_ADJUSTMENT = 'BALANCE_ADJUSTMENT'
    BALANCE_ASSET_FEE = 'BALANCE_ASSET_FEE'
    BALANCE_CASHBACK = 'BALANCE_CASHBACK'
    BALANCE_DEPOSIT = 'BALANCE_DEPOSIT'
    BALANCE_HOLD_FEE = 'BALANCE_HOLD_FEE'
    BALANCE_INTEREST = 'BALANCE_INTEREST'
    BANK_DETAILS_ORDER = 'BANK_DETAILS_ORDER'
    BATCH_TRANSFER = 'BATCH_TRANSFER'
    CARD_CASHBACK = 'CARD_CASHBACK'
    CARD_CHECK = 'CARD_CHECK'
    CARD_ORDER = 'CARD_ORDER'
    CARD_PAYMENT = 'CARD_PAYMENT'
    CASH_WITHDRAWAL = 'CASH_WITHDRAWAL'
    CLAIMABLE_SEND_ORDER = 'CLAIMABLE_SEND_ORDER'
    DIRECT_DEBIT_TRANSACTION = 'DIRECT_DEBIT_TRANSACTION'
    EXCESS_REFUND = 'EXCESS_REFUND'
    FEE_REFUND = 'FEE_REFUND'
    INCORPORATION_ORDER = 'INCORPORATION_ORDER'
    INTERBALANCE = 'INTERBALANCE'
    PAYMENT_REQUEST = 'PAYMENT_REQUEST'
    PREFUNDING_TRANSFER = 'PREFUNDING_TRANSFER'
    REWARD = 'REWARD'
    SCHEDULED_SEND_ORDER = 'SCHEDULED_SEND_ORDER'
    TRANSFER = 'TRANSFER'


class ActivityMonetaryResourceType(str, Enum):
    ACCRUAL_CHARGE = 'ACCRUAL_CHARGE'
    ACQUIRING_PAYMENT = 'ACQUIRING_PAYMENT'
    ASSETS_WITHDRAWAL = 'ASSETS_WITHDRAWAL'
    BALANCE_CASHBACK = 'BALANCE_CASHBACK'
    BALANCE_INTEREST = 'BALANCE_INTEREST'
    BALANCE_TRANSACTION = 'BALANCE_TRANSACTION'
    BANK_DETAILS_ORDER = 'BANK_DETAILS_ORDER'
    BATCH_TRANSFER = 'BATCH_TRANSFER'
    CARD_CASHBACK = 'CARD_CASHBACK'
    CARD_ORDER = 'CARD_ORDER'
    CARD_TRANSACTION = 'CARD_TRANSACTION'
    DIRECT_DEBIT_INSTRUCTION = 'DIRECT_DEBIT_INSTRUCTION'
    DIRECT_DEBIT_TRANSACTION = 'DIRECT_DEBIT_TRANSACTION'
    FEE_REFUND = 'FEE_REFUND'
    INCIDENT_REFUND = 'INCIDENT_REFUND'
    INCORPORATION_ORDER = 'INCORPORATION_ORDER'
    OPERATIONAL_TRANSACTION = 'OPERATIONAL_TRANSACTION'
    PAYMENT_REQUEST = 'PAYMENT_REQUEST'
    REWARD = 'REWARD'
    REWARDS_REDEMPTION = 'REWARDS_REDEMPTION'
    SEND_ORDER = 'SEND_ORDER'
    SEND_ORDER_EXECUTION = 'SEND_ORDER_EXECUTION'
    TRANSFER = 'TRANSFER'


class ActivitiesService(Base):
    activity = JsonEndpointWithSCA(
        path="/v1/profiles/{profile_id}/activities",
        required_params = []
    )


class Activities:
    def __init__(self, client: Client):
        self.service = ActivitiesService(client=client)

    def activity(
            self,
            profile_id: str,
            **kwargs
    ) -> Any:
        params :dict= {}
        for param_name, param_value in kwargs.values():
            match param_name:
                case 'monetary_resource_type':
                    if param_value is not None:
                        if param_value  in ActivityMonetaryResourceType.__members__.values():
                            params['monetaryResourceType'] = param_value
                        else:
                            raise ValueError(f"Invalid monetary resource type '{param_value}'; value values are: {ActivityMonetaryResourceType.__members__.values()}")
                case 'status':
                    if param_value is not None:
                        if param_value in Status.__members__.values():
                            params['status'] = param_value
                        else:
                            raise ValueError(f"Invalid status '{param_value}'; value values are: {Status.__members__.values()}")
                case 'since':
                    params['since'] = param_value
                case 'until':
                    params['until'] = param_value
                case 'size':
                    if param_value is not None:
                        if param_value.isdigit():
                            params['size'] = param_value
                        else:
                            raise ValueError(f"size must be all digits; got {param_value}")
                case 'next_cursor':
                    params['nextCursor'] = param_value
                case _:
                    raise ValueError(f"unrecognized parameter '{param_name}")

        return munchify(
            self.service.activity(
                profile_id=profile_id,
                params=params,
            )
        )
