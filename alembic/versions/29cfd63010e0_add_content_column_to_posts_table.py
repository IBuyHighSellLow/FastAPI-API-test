"""add content column to posts table

Revision ID: 29cfd63010e0
Revises: 96bc8ee81582
Create Date: 2022-10-22 03:51:30.615354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29cfd63010e0'
down_revision = '96bc8ee81582'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
