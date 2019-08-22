from flask import Flask

from app.views import load_page_view, check_task_view

app = Flask(__name__)


app.route('/tags/', methods=['post'])(load_page_view)
app.route('/tags/<task_id>', methods=['get'])(check_task_view)


if __name__ == '__main__':
    app.run()
