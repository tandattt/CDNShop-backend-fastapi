# repository/view_history_repository.py
from app.models.view_history import ViewHistory
from sqlalchemy.orm import Session
from sqlalchemy import func

class ViewHistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_view(self, user_id, product_id):
        history = ViewHistory(
            user_id=user_id,
            product_id=product_id
        )
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)
        return history
    def get_last_viewed_product(self, user_id: int,limit: int):
        subquery = (
            self.db.query(
                ViewHistory.product_id,
                func.max(ViewHistory.viewed_at).label("latest_viewed_at")
            )
            .filter(ViewHistory.user_id == user_id)
            .group_by(ViewHistory.product_id)
            .order_by(func.max(ViewHistory.viewed_at).desc())
            .limit(limit)
            .subquery()
        )

        query = (
            self.db.query(ViewHistory)
            .join(
                subquery,
                (ViewHistory.product_id == subquery.c.product_id) &
                (ViewHistory.viewed_at == subquery.c.latest_viewed_at)
            )
            .order_by(ViewHistory.viewed_at.desc())
        )

        return query.all()