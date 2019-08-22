import os

broker_url = f'pyamqp://guest:guest@{os.environ["RABBIT_HOST"]}:5672/'
result_backend = f'rpc://guest:guest@{os.environ["RABBIT_HOST"]}:5672/'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# enable_utc = True
