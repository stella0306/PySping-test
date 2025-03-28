from flask import request, Response, render_template, Blueprint
import json

try:
    from Service.Impl.memo_serivce_impl import MemoServiceImpl
    from Repository.memo_repository import MemoRepository

except ImportError:
    from ..Service.Impl.memo_serivce_impl import MemoServiceImpl
    from ..Repository.memo_repository import MemoRepository

memo_views_bp = Blueprint(
    name='memos_views',
    import_name=__name__,
    template_folder="templates"
    )

# 뷰어
@memo_views_bp.route("/views", methods=["GET"])
def memo_views():
    return render_template("memos/index.html")