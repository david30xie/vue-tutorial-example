import json
import time
import bottle
from bottle import route, run, abort, request, response


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/api/comments/<comment_id>')
def comment(comment_id):
    with open('comments.json') as f:
        comments = json.loads(f.read())

    comment = None
    for i in comments:
        if str(i['id']) == str(comment_id):
            comment = i
            break
    if not comment:
        abort(404)

    response.set_header('Cache-Control', 'no-cache')
    response.set_header('Access-Control-Allow-Origin', '*')
    response.content_type = 'application/json'
    return json.dumps(comment)


@route('/api/comments', method=['OPTIONS', 'GET', 'POST'])
@enable_cors
def comments():
    with open('comments.json') as f:
        comments = json.loads(f.read())

    response.set_header('Cache-Control', 'no-cache')
    response.set_header('Access-Control-Allow-Origin', '*')
    response.content_type = 'application/json'

    if request.method == 'POST':
        if set(request.json.keys()) != set(['author', 'text', 'title']):
            abort(500)

        new_comment = dict(author=request.json['author'],
                           title=request.json['title'],
                           text=request.json['text'])
        new_comment['id'] = int(time.time() * 1000)
        
        comments.append(new_comment)
        with open('comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4, separators=(',', ': ')))

        return json.dumps(new_comment)

    return json.dumps(comments)

run(host='localhost', port=4000)
