from collections import namedtuple

Rule = namedtuple('Rule', 'doc', 'description', 'runbook')

rule = {
    'RULE_NAME': Rule('RULE_NAME', 'docuemntation-link', 'rule descrption')
}

runbook = {'runbook_name': 'https:link'}

def get_doc(ruleName: str):
    return rule[ruleName].doc

def get_description(ruleName: str):
    return rule[ruleName].description

def get_runbook(ruleName: str):
    return rule[ruleName].runbook