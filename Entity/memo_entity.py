from dataclasses import dataclass

try:
    from config.database import db
except ImportError:
    from ..config.database import db

@dataclass
class MemoEntity(db.Model):
    __tablename__ = "memo_data"

    id: int
    title: str
    content: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<MemoData(id={self.id}, title={self.title})>"