import json
from runner import Runner


def hello(event, context):
    rule = Runner(event)
    rule.load_data()
    return rule.run_rule()
