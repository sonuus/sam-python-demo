import json
import boto3

print('Loading function ....')

def handler(event, context):
    '''
        Provide an event that contains the following keys:

        - operation: one of the operations in the operations dict below 
        - tablename: required for operations that interact with DynamoDB
        - payload: a parameter to pass to the operation being performed

    '''
    print('Received event ' + json.dumps(event,indent =2))
    print('change done to get a version 2 of function...')

    #operation=event['operation']
    body = json.loads(event['body'])

    for x in body:
	    print("%s: %d" % (x, body[x]))
        

    dynamo=boto3.resource('dynamodb').Table('lo_students')
    # if 'tableName' in event:
    #     dynamo=boto3.resource('dynamodb').Table('lo_students')
    # else:
    #     raise ValueError('Table not found!')

    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read': lambda x: dynamo.get_item(**x),
        'update': lambda x: dynamo.update_item(**x),
        'delete': lambda x: dynamo.delete_item(**x),
        'list': lambda x: dynamo.scan(**x),
        'echo': lambda x: x,
        'ping': lambda x: 'pong'
    }

    if operation in operations:
        return operations[operation] (event.get('payload'))
    else:
        raise ValueError('Unrecognizied operation "{}"'.format(operation))