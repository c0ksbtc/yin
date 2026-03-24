"""Binance-specific adapter helpers for funding rate and ticker fetching.
This module normalizes different ccxt Binance variants (binance, binanceusdm, binancecoinm).
"""
from typing import Optional, Any

def fetch_funding_rate(exchange: Any, symbol: str) -> Optional[float]:
    """Try common ccxt methods / endpoints to obtain funding rate for a symbol.
    Returns funding rate as a float (e.g. 0.0001) or None.
    """
    try:
        # common method name
        if hasattr(exchange, "fetch_funding_rate"):
            fr = exchange.fetch_funding_rate(symbol)
            if isinstance(fr, dict):
                for key in ("fundingRate", "funding_rate", "rate", "value"):
                    if key in fr and fr[key] is not None:
                        return float(fr[key])
                # sometimes nested in info
                info = fr.get("info") if isinstance(fr.get("info"), dict) else None
                if info:
                    for k in ("fundingRate", "funding_rate"):
                        if k in info and info[k] is not None:
                            return float(info[k])
        # some binance variants expose fetchFundingRates / fetch_funding_rates
        if hasattr(exchange, "fetch_funding_rates"):
            all_fr = exchange.fetch_funding_rates()
            if isinstance(all_fr, list):
                for entry in all_fr:
                    if entry.get("symbol") == symbol:
                        for key in ("fundingRate", "funding_rate", "rate"):
                            if key in entry and entry[key] is not None:
                                return float(entry[key])
        # fallback: some exchanges have public API endpoints accessible via exchange.publicGet... (best effort)
    except Exception:
        pass
    return None

def fetch_price(exchange: Any, symbol: str) -> Optional[float]:
    try:
        if hasattr(exchange, "fetch_ticker"):
            t = exchange.fetch_ticker(symbol)
            if isinstance(t, dict):
                for k in ("last", "close", "price"):
                    if k in t and t[k] is not None:
                        return float(t[k])
    except Exception:
        pass
    return None