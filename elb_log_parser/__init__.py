#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/leandrosouza/elb-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Leandro Souza <lsouzarj@gmail.com>

import csv
from datetime import datetime
import logging
import urlparse

try:
    from cStringIO import StringIO
except ImportError:
    try:
        from six import StringIO
    except ImportError:
        logging.warning("Error importing dependencies, probably setup.py reading package. Ignoring...")

try:
    import six
    from user_agents import parse as user_agent_parse
except ImportError:
    logging.warning("Error importing dependencies, probably setup.py reading package. Ignoring...")

from elb_log_parser.version import __version__  # NOQA


def parse(reader):
    result = []

    if isinstance(reader, six.string_types):
        reader = StringIO(reader)

    for line in csv.reader(reader, delimiter=' '):
        if len(line) < 2:
            continue
        result.append(parse_line(line))

    return result


def parse_line(log_line):
    response = Response()
    
    response.timestamp = datetime.strptime('%s %s' % (log_line[0].split("T")[0], log_line[0].split("T")[1].split(".")[0]),'%Y-%m-%d %H:%M:%S')
    response.elb_elb = log_line[1]
    response.elb_client_ip = log_line[2].split(":")[0]
    if log_line[3] != "-":
        response.elb_backend_ip = log_line[3].split(":")[0]
        response.elb_backend_port = int(log_line[3].split(":")[1])
    response.elb_request_processing_time = float(log_line[4])
    response.elb_backend_processing_time = float(log_line[5])
    response.elb_response_processing_time = float(log_line[6])
    response.elb_elb_status_code = int(log_line[7])
    response.elb_backend_status_code = int(log_line[8])
    response.elb_received_bytes = int(log_line[9])
    response.elb_sent_bytes = int(log_line[10])
    response.elb_http_method = log_line[11].split(" ")[0]

    url = urlparse.urlsplit(log_line[11].split(" ")[1])
    response.elb_request_protocol = url.scheme
    response.elb_request_host = url.hostname
    response.elb_path = url.path
    response.elb_querystring = url.query

    parse_user_agent(response, log_line[12])

    response.elb_ssl_cipher = log_line[13]
    response.elb_ssl_protocol = log_line[14]


    return response


def parse_user_agent(response, user_agent_str):
    response.elb_user_agent = user_agent_str
    user_agent = user_agent_parse(response.elb_user_agent)
    response.elb_browser_family = user_agent.browser.family
    response.elb_browser_version = '.'.join([str(item) for item in user_agent.browser.version])
    response.elb_os_family = user_agent.os.family
    response.elb_os_version = '.'.join([str(item) for item in user_agent.os.version])
    response.elb_device = user_agent.device.family
    response.elb_is_mobile = user_agent.is_mobile
    response.elb_is_tablet = user_agent.is_tablet
    response.elb_is_pc = user_agent.is_pc
    response.elb_is_touch_capable = user_agent.is_touch_capable
    response.elb_is_bot = user_agent.is_bot


class Response:
    def __init__(self):
        self.timestamp = None
        self.elb_elb = None
        self.elb_client_ip = None
        self.elb_backend_ip = None
        self.elb_backend_port = None
        self.elb_request_processing_time = None
        self.elb_backend_processing_time = None
        self.elb_response_processing_time = None
        self.elb_status_code = None
        self.elb_backend_status_code = None
        self.elb_received_bytes = None
        self.elb_sent_bytes = None
        self.elb_http_method = None
        self.elb_request_protocol = None
        self.elb_request_host = None
        self.elb_path = None
        self.elb_querystring = None
        self.elb_user_agent = None
        self.elb_browser_family = None
        self.elb_browser_version = None
        self.elb_os_family = None
        self.elb_os_version = None
        self.elb_device = None
        self.elb_is_mobile = None
        self.elb_is_tablet = None
        self.elb_is_pc = None
        self.elb_is_touch_capable = None
        self.elb_is_bot = None
        self.elb_ssl_cipher = None
        self.elb_ssl_protocol = None
