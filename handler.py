import json
from runner import Runner


def run_validation_rule(event, context):
    rule = Runner(event)
    rule.load_data()
    return rule.run_rule()
