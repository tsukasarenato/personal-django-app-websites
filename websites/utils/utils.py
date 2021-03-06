from django.utils import timezone
from tzlocal import get_localzone
from babel.numbers import format_currency
import pytz


# https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/
def custom_datetime(datetime, tz=str(get_localzone())):
    timezone.activate(pytz.timezone(tz))
    current_tz = timezone.get_current_timezone()
    return current_tz.normalize(datetime)


def money_format(money, currency, language):
    money = float(money)
    return format_currency(money, currency, locale=language)


def smartphone_format(number):
    return f'({number[0:2]}) {number[2:]}'


def hexadecimal(value):

    for x in range(len(value)):

        if not value[x].isnumeric() and value[x].lower() not in ['a', 'b', 'c', 'd', 'e', 'f']:
            return False

    if len(value) < 6:
        n = 6 - len(value)
        value = '0'*n + value

    return value.lower()
