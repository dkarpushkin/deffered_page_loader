import json
from collections import defaultdict
from flask import make_response, request
from lxml import html

from app.tasks import async_load_page, async_result


def json_response(data: dict):
    resp = make_response(json.dumps(data))
    resp.headers['Content-Type'] = 'application/json'

    return resp


def count_tags(html_content):
    doc = html.fromstring(html_content)
    tags = defaultdict(lambda: 0)

    for element in doc.iter():
        tags[element.tag] += 1

    return tags


def load_page_view():
    url = request.args.get('url')
    if url:
        async_result = async_load_page(url)
        return json_response({
            'status': 0,
            'async_task_id': async_result
        })
    else:
        return json_response({
            'status': 1,
            'error': 'Url is necessary'
        })


def check_task_view(task_id):
    result, is_ready = async_result(task_id)

    if not is_ready:
        return json_response({
            'status': 1,
            'result': result
        })

    if result and isinstance(result, (str, bytes)):
        message = count_tags(result)
    else:
        print(result)
        message = None

    return json_response({
        'status': 0,
        'result': message
    })