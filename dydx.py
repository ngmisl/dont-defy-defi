from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict
from datetime import datetime
import requests


class QuoteAsset(Enum):
    USD = "USD"


class Status(Enum):
    CLOSE_ONLY = "CLOSE_ONLY"
    ONLINE = "ONLINE"


class TypeEnum(Enum):
    PERPETUAL = "PERPETUAL"


@dataclass
class Market:
    trades24_h: Optional[int] = None
    incremental_position_size: Optional[int] = None
    max_position_size: Optional[int] = None
    baseline_position_size: Optional[int] = None
    market: Optional[str] = None
    status: Optional[Status] = None
    base_asset: Optional[str] = None
    quote_asset: Optional[QuoteAsset] = None
    step_size: Optional[str] = None
    tick_size: Optional[str] = None
    index_price: Optional[str] = None
    oracle_price: Optional[str] = None
    price_change24_h: Optional[str] = None
    next_funding_rate: Optional[str] = None
    next_funding_at: Optional[datetime] = None
    min_order_size: Optional[str] = None
    type: Optional[TypeEnum] = None
    initial_margin_fraction: Optional[str] = None
    maintenance_margin_fraction: Optional[str] = None
    volume24_h: Optional[str] = None
    open_interest: Optional[str] = None
    incremental_initial_margin_fraction: Optional[str] = None
    asset_resolution: Optional[str] = None
    synthetic_asset_id: Optional[str] = None


@dataclass
class Dydx:
    markets: Optional[Dict[str, Market]] = None