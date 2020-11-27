#!/usr/bin/env python3

import argparse
import sys

from flask import Flask, request, jsonify
from flask_cors import CORS

from ..scanned_detectors import ALL_SCANNED_DETECTORS
from ..document import Document


SERVER_VERSION = "0.1.0"
APP = Flask(__name__)
CORS(APP)


# Parse arguments. If the --detectors flag is used, then only use the detectors
# that are requested.

detectors = ALL_SCANNED_DETECTORS.values()


@APP.route("/")
def route_home():
    """
    A "heartbeat" route for the homepage.

    Returns:
        str

    """
    return "genderbias server v{}".format(SERVER_VERSION)


@APP.route("/check", methods=["POST"])
def route_check():
    """
    Check POSTed text for gender bias.

    POST an application/json body with a "text" key and string value; results
    will be returned in the form:

    {
        reports: List[dict]
    }

    Where each report has zero or more flags.

    """
    text = request.json["text"]
    doc = Document(text)

    reports = []
    for detector in detectors:
        reports.append(detector().get_report(doc))

    reports_data = [report.to_dict() for report in reports]
    return jsonify({"issues": reports_data, "text": request.json["text"]})


# Run the server.
def run_server(*args, **kwargs):
    APP.run(*args, **kwargs)
