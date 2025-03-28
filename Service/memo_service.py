from abc import ABC, abstractmethod

class MemoService(ABC):
    @abstractmethod
    def get_all_memos(self):
        pass

    @abstractmethod
    def get_memo_by_id(self, memo_id: int):
        pass

    @abstractmethod
    def create_memo(self, title: str, content: str):
        pass

    @abstractmethod
    def update_memo(self, memo_id: int, title: str, content: str):
        pass

    @abstractmethod
    def delete_memo(self, memo_id: int):
        pass
