import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, object):
        # if passed in object is instance of Decimal
        # convert it to a string, otherwise use the,
        # default behavior
        return (
            str(object)
            if isinstance(object, Decimal)
            else json.JSONEncoder.default(self, object)
        )
