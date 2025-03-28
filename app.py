from flask import Flask

try:
    from config.database import db, init_db
    from Controller.memo_controller import memo_bp
    from Controller.memo_views_controller import memo_views_bp

except ImportError:
    from .config.database import db, init_db
    from .Controller.memo_controller import memo_bp
    from .Controller.memo_views_controller import memo_views_bp

app = Flask(__name__)

# 데이터베이스 설정 적용
init_db(app)

# 애플리케이션 시작 시 DB 초기화
with app.app_context():
    db.create_all()

# 블루프린트 등록
app.register_blueprint(memo_bp, url_prefix='/memos')  # memo_bp 블루프린트를 등록하여 메모 관련 요청을 처리
app.register_blueprint(memo_views_bp, url_prefix='/memos_views')  # memo_views_bp 블루프린트를 등록하여 메모 관련 요청을 처리

if __name__ == '__main__':
    app.run(debug=True)
