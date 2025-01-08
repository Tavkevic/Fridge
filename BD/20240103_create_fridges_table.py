from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Идентификаторы миграции
revision: str = '20240103_create_fridges_table'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def  upgrade() -> None:
    """Создает таблицы Fridges, Shelfs и Review с каскадным удалением"""
    op.create_table(
        'Fridges',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Создаем таблицу Shelfs
    op.create_table(
        'Shelfs',
        sa.Column('id', sa.Integer(), nullable=False),  # Столбец id
        sa.Column('name', sa.String(), nullable=False),  # Имя категории

        sa.PrimaryKeyConstraint('id')  # Определяем первичный ключ
    )

    # Создаем таблицу Product
    op.create_table(
        'Product',
        sa.Column('id', sa.Integer(), nullable=False),  # Столбец id продукта
        sa.Column('category_id', sa.Integer(), nullable=False),  # Внешний ключ на Category
        sa.Column('name', sa.String(), nullable=False),  # Имя продукта
        sa.ForeignKeyConstraint(['category_id'], ['Category.id'], ondelete='CASCADE'),
        # Внешний ключ с каскадным удалением
        sa.PrimaryKeyConstraint('id')  # Определяем первичный ключ
    )

    # Создаем таблицу Review
    op.create_table(
        'Review',
        sa.Column('id', sa.Integer(), nullable=False),  # Столбец id отзыва
        sa.Column('product_id', sa.Integer(), nullable=False),  # Внешний ключ на Product
        sa.Column('content', sa.Text(), nullable=False),  # Содержимое отзыва
        sa.ForeignKeyConstraint(['product_id'], ['Product.id'], ondelete='CASCADE'),
        # Внешний ключ с каскадным удалением
        sa.PrimaryKeyConstraint('id')  # Определяем первичный ключ
    )


def downgrade() -> None:
    """Удаляет таблицы Review, Product и Category"""
    op.drop_table('Review')  # Удаляем таблицу Review
    op.drop_table('Product')  # Удаляем таблицу Product
    op.drop_table('Category')  # Удаляем таблицу Category
