from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo'

@bp.route('/')
def index():
    # url_for 함수 : 라우트가 설정된 함수명으로 url을 역으로 찾아준다.
    # question = 블루프린트 이름
    # _list = 블루프린트에 등록된 함수명
    return redirect(url_for('question._list'))

