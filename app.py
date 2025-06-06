import json
import subprocess

subprocess.run([
    'gh',
    'alias',
    'set',
    'assign-copilot',
    'api --method POST /repos/$1/pulls/$2/requested_reviewers -f "reviewers[]=copilot-pull-request-reviewer[bot]"',
])

def handler(event, context):
    body = json.loads(event['body'])

    if 'action' in body and (body['action'] == 'opened' and not body['pull_request']['draft'] or body['action'] == 'ready_for_review'):
        subprocess.run([
            'gh',
            'assign-copilot',
            body['repository']['full_name'],
            str(body['number']),
        ])

    return {
        'statusCode': 204,
    }
