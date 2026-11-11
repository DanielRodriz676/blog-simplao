from datetime import datetime
from sqlalchemy.orm import Mapped, registry, mapped_column, registry

from sqlalchemy import func

table_registry = registry()

@table_registry.mapped_as_dataclass()
class Article:
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())