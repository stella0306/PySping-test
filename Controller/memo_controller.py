from flask import request, Response, render_template, Blueprint
import json

try:
    from Service.Impl.memo_serivce_impl import MemoServiceImpl
    from Repository.memo_repository import MemoRepository

except ImportError:
    from ..Service.Impl.memo_serivce_impl import MemoServiceImpl
    from ..Repository.memo_repository import MemoRepository


memo_bp = Blueprint(
    name='memos',
    import_name=__name__,
    template_folder="templates"
    )

# 서비스 계층 인스턴스 생성
memo_service = MemoServiceImpl(MemoRepository)

# 모든 메모 조회
@memo_bp.route("/", methods=["GET"])
def get_all_memos():
    memos = memo_service.get_all_memos()

    memos_dict = [memo.__dict__ for memo in memos]  # to_dict() 사용
    return Response(
        json.dumps(memos_dict, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )


# 특정 메모 조회
@memo_bp.route("/<int:memo_id>", methods=["GET"])
def get_memo_by_id(memo_id:int):
    memo = memo_service.get_memo_by_id(memo_id)

    return Response(
        json.dumps(memo.__dict__ if memo else {}, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )

# 새로운 메모 추가
@memo_bp.route("/", methods=["POST"])
def create_memo():
    data = request.get_json() # 클라이언트에서 받은 JSON 데이터
    memo = memo_service.create_memo(title=data["title"], content=data["content"])
    
    return Response(
        json.dumps(memo.__dict__ if memo else {}, ensure_ascii=False, indent=4),
        mimetype='application/json'
    ), 201

# 특정 메모 수정
@memo_bp.route("/<int:memo_id>", methods=["PUT"])
def update_memo(memo_id:int):
    data = request.get_json() # 클라이언트에서 받은 JSON 데이터
    memo = memo_service.update_memo(memo_id=memo_id, title=data["title"], content=data["content"])

    return Response(
        json.dumps(memo.__dict__ if memo else {}, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )

# 특정 메모 삭제
@memo_bp.route("/<int:memo_id>", methods=["DELETE"])
def delete_memo(memo_id:int):
    memo_service.delete_memo(memo_id=memo_id)
    return '', 204
