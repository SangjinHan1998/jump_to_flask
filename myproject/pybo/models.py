from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # user_id --> User와 Question 연결하기 위한 속성 / server_default --> 최조 생성한 User모델 데이터의 id값
    user = db.relationship('User', backref=db.backref('question_set'))
    # user --> Question 모델에서 User모델을 참조하기 위한 속성.
    # db.Column --> 1. data type 2. primary_key???
    modify_date = db.Column(db.DateTime(), nullable=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # connect question and answer to use db.ForeignKey
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # table name = question
    question = db.relationship('Question', backref=db.backref('answer_set'))
    # backref -> back-reference
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
