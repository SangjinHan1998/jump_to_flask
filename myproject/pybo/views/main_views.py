from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Pybo hello5'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    '''
    작성일시 순 
    order_by(Question.create_date.asc())
   

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
     '''
