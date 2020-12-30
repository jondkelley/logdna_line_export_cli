# -*- coding: utf-8 -*-
import click
from requests import get as get_url
import re
import json
import dateutil.parser
from time import time as now
from time import mktime
import datetime


def get_batch_recursively(query, tfrom, tto, hostname, service_key):
    """
    recursively fetch the log export batches
    """
    if tfrom >= tto:
        return 1
    else:
        ###print(f'get {tfrom} {tto}')
        payload = {
            'from': tfrom,
            'to': tto,
            'query': query,
            'prefer': 'head'
        }
        r = get_url(f'https://{hostname}/v1/export',
                    params=payload,
                    auth=(service_key, ''))
        if r.text is not None:
            for line in r.text.split('\n'):
                if not (re.match(r'^\s*$', line)):
                    json_line = json.loads(line)
                    print(json_line)
                    tfrom = json_line['_ts'] + 1
        get_batch_recursively(query, tfrom, tto, hostname, service_key)


@click.command()
@click.option('-q', '--query', 'query',
              help='The log query you wish to perform',
              required=True)
@click.option('-k', '--service-key', 'service_key',
              help='Your LogDNA service key found in your settings',
              required=True)
@click.option('-f', '--fromtime', 'from_time',
              help='From date, must be any ISO-8601 compatible date [i.e. 2020-12-01T10:05:45-06:00] or UNIX Epoch in seconds',
              required=True)
@click.option('-t', '--totime', 'to_time',
              help='Optional from date, must be any ISO-8601 compatible date [i.e. 2020-12-01T10:05:45-06:00] or UNIX Epoch in seconds',
              default=int(round(now())),
              required=False)
@click.option('-h', '--host', 'hostname',
              help='Optional change the default LogDNA API host endpoint [default: api.logdna.com]',
              default='api.logdna.com',
              required=False)
@click.option('-p', '--print-date', 'print_date',
              help='Print the date conversions, useful for troubleshooting iso8601 conversion',
              default=False,
              is_flag=True)
def entry(query, service_key, from_time, to_time, hostname, print_date):
    """
    This command will recursively fetch all logs from the logdna export API.

    This is useful to get logs beyond the 10,000 line limit as the API does
    not natively provide pagination.

    Authors: jonathan.kelley@logdna.com
    """
    if not str(from_time).isnumeric():
        try:
            from_time = int(
                round(mktime(dateutil.parser.isoparse(from_time).timetuple())))
        except Exception as e:
            print(f'error : cannot convert fromtime to unix epoch, {e}')
            exit(1)
    if not str(to_time).isnumeric():
        try:
            to_time = int(
                round(mktime(dateutil.parser.isoparse(to_time).timetuple())))
        except Exception as e:
            print(f'error : cannot convert totime to unix epoch, {e}')
            exit(1)
    if print_date:
        if str(from_time).isnumeric():
            print(f'from: {from_time} (UNIX EPOCH)')
        else:
            from_time = dateutil.parser.isoparse(from_time)
            print(f'from: {from_time} (ISO-8601)')
        if str(to_time).isnumeric():
            print(f'to: {to_time} (UNIX EPOCH)')
        else:
            to_time = dateutil.parser.isoparse(to_time)
            print(f'to: {to_time} (ISO-8601)')
    else:
        get_batch_recursively(query, from_time, to_time, hostname, service_key)
