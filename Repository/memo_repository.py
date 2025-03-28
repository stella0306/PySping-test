from Entity.memo_entity import MemoEntity
from config.database import db

class MemoRepository:
    @staticmethod
    def find_all():
        return MemoEntity.query.all()
    
    @staticmethod
    def find_by_id(memo_id: int):
        return MemoEntity.query.filter_by(id=memo_id).first()
    
    @staticmethod
    def save(memo: MemoEntity):
        db.session.add(memo)
        db.session.commit()
    
    @staticmethod
    def delete(memo_id: int):
        memo = MemoEntity.query.filter_by(id=memo_id).first()
        if memo:
            db.session.delete(memo)
            db.session.commit()
            