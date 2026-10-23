#!/usr/bin/env python3
"""My own query on gutenberg.books."""

import json
import logging
import os

from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Atlas settings from your environment variables, as in Lab 05
MONGODB_ATLAS_URL = os.environ["MONGODB_ATLAS_URL"]
MONGODB_ATLAS_USER = os.environ["MONGODB_ATLAS_USER"]
MONGODB_ATLAS_PWD = os.environ["MONGODB_ATLAS_PWD"]

logger = logging.getLogger(__name__)


def main():
    """Print the result of my query as JSON."""
    client = MongoClient(MONGODB_ATLAS_URL, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD)
    try:
        books = client["gutenberg"]["books"]
        result = []  # TODO: replace [] with a call of your query function
        print(json.dumps(result, indent=2, default=str))
    except PyMongoError as e:
        logger.error("Cannot query MongoDB: %s", e)
        raise
    finally:
        client.close()  # closes the connections to Atlas, also after an error


if __name__ == "__main__":
    main()
