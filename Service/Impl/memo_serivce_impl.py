try:
    from Service.memo_service import MemoService
    from Repository.memo_repository import MemoRepository
    from DTO.memo_dto import MemoDTO
    from Entity.memo_entity import MemoEntity

except ImportError:
    from ...Service.memo_service import MemoService
    from ...Repository.memo_repository import MemoRepository
    from ...DTO.memo_dto import MemoDTO
    from ...Entity.memo_entity import MemoEntity


class MemoServiceImpl(MemoService):
    def __init__(self, memo_repository: MemoRepository):
        self.memo_repository = memo_repository
    
    def get_all_memos(self):
        memos = self.memo_repository.find_all()
        return [MemoDTO(id=memo.id, title=memo.title, content=memo.content) for memo in memos]
    
    def get_memo_by_id(self, memo_id: int):
        memo = self.memo_repository.find_by_id(memo_id)
        if memo:
            return MemoDTO(id=memo.id, title=memo.title, content=memo.content)
        return None
    
    def create_memo(self, title: str, content: str):
        memo = MemoEntity(title=title, content=content)
        self.memo_repository.save(memo)
        return MemoDTO(id=memo.id, title=memo.title, content=memo.content)
    
    def update_memo(self, memo_id: int, title: str, content: str):
        memo = self.memo_repository.find_by_id(memo_id)
        if memo:
            memo.title = title
            memo.content = content
            self.memo_repository.save(memo)
            return MemoDTO(id=memo.id, title=memo.title, content=memo.content)
    
    def delete_memo(self, memo_id: int):
        return self.memo_repository.delete(memo_id)
    
    