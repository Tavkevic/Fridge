from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Идентификаторы миграции
revision: str = '20240103_create_fridges_table'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def  upgrade() -> None:
    """
    Создает таблицы Fridges, Shelves и Review с каскадным удалением
    """

    op.create_table(
        'Fridges',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'Shelves',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('fridges_id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('size', sa.Integer(), nullable=False),
        sa.Column('free_place', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['fridges_id'], ['Fridges.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'Product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('shelves_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('many', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['shelves_id'], ['Shelves.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """
    Удаляет таблицы Fridges, Product и Shelves
    """

    op.drop_table('Fridges')
    op.drop_table('Product')
    op.drop_table('Shelves')
