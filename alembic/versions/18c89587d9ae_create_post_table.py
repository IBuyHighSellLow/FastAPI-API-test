"""create post table

Revision ID: 18c89587d9ae
Revises: 
Create Date: 2022-10-21 04:20:20.383426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18c89587d9ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
        primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
