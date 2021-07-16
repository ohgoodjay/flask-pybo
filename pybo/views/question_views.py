from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db

from pybo.models import Question
from ..forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    '''
    질문 목록에서 <질문 등록하기> 버튼을 누르거나
    질문 등록 화면에서 <저장하기> 버튼을 누르면
    똑같이 localhost:5000/question/create/ 페이지를 요청하므로
    create 함수가 이 요청을 받는다.
    다만 create 함수에서 요청 방식을 구분해서 처리한다.
    즉, <질문 등록하기>는 GET 방식 요청이므로 그대로 질문 등록 화면을 보여 주고,
    <저장하기>는 POST 방식 요청이므로 데이터베이스에 질문 1건을 저장한 다음
    질문 목록 화면으로 이동한다.
    '''
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now()
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html', form=form)