from django.conf import settings

MAIN_ACCOUNT = getattr(
    settings, 
    "BITCOIND_MAIN_ACCOUNT", 
    "somerandomstring14aqqwd")
CONNECTION_STRING = getattr(
    settings, 
    "BITCOIND_CONNECTION_STRING", 
    "")
PAYMENT_BUFFER_SIZE = getattr(
    settings, 
    "DBITCOIN_PAYMENT_BUFFER_SIZE",
    5)
PAYMENT_VALID_HOURS = getattr(
    settings, 
    "BITCOIND_PAYMENT_VALID_HOURS", 
    128)
REUSE_ADDRESSES = getattr(
    settings, 
    "BITCOIND_REUSE_ADDRESSES", 
    True)
ESCROW_PAYMENT_TIME_HOURS = getattr(
    settings, 
    "BITCOIND_ESCROW_PAYMENT_TIME_HOURS", 
    4)
ESCROW_RELEASE_TIME_DAYS = getattr(
    settings, 
    "BITCOIND_ESCROW_RELEASE_TIME_DAYS", 
    14)

BITCOIN_CURRENCIES = getattr(
    settings, 
    "BITCOIN_CURRENCIES",
    [
        "django_bitcoin.currency.BitcoinCurrency",
        "django_bitcoin.currency.EURCurrency",
        "django_bitcoin.currency.USDCurrency"
        ])
