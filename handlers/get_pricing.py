'''get pricing multiple'''

import logging
import json
import os
import random
import time

# logging
log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type:ignore
_logger = logging.getLogger(__name__)


def _random_slowdown():
    '''Add a random slow down to annoy people.'''
    # random slow down.
    if random.randint(1, 10) > 8:
        _logger.info('Hit slowdown...')
        time.sleep((100 - random.randint(5, 20)) / 100)


def _get_pricing_multiple():
    '''Return pricing multiple.'''
    multiple = 1
    if random.randint(1, 10) > 8:
        multiple = _get_pricing_multiple_discount()
        _logger.info('DISCOUNT: {}'.format(multiple))
    elif random.randint(1, 10) < 3:
        multiple = _get_pricing_multiple_surge()
        _logger.info('SURGE: {}'.format(multiple))
    else:
        _logger.info('STANDARD')

    return multiple


def _get_pricing_multiple_discount():
    '''Return pricing multiple.'''
    return (100 - random.randint(5, 20)) / 100


def _get_pricing_multiple_surge():
    '''Return pricing multiple.'''
    return ((random.randint(1, 10)) / 10) + 1


def handler(event, context):
    '''Function entry'''
    _logger.info('Request: {}'.format(json.dumps(event)))

    _random_slowdown()
    pricing_multiple = _get_pricing_multiple()

    resp_body = {'PricingMultiple': pricing_multiple}

    resp = {
        'statusCode': 200,
        'body': json.dumps(resp_body)
    }
    _logger.debug('Response: {}'.format(json.dumps(resp)))

    return resp

