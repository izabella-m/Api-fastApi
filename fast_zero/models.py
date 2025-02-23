from sqlalchemy.orm import registry, Mapped, mapped_column

table_registry = registry()
@table_registry.mapped_as_dataclass # Data class que representa uma tabela de banco

class User: 
    __tablename__ = 'users' 
    
    id: Mapped[int] = mapped_column(init=False,primary_key=True) 
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] 