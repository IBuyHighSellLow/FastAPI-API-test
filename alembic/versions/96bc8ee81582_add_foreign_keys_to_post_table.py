"""add foreign keys to post table

Revision ID: 96bc8ee81582
Revises: da5ea9248f4a
Create Date: 2022-10-22 03:49:18.506400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96bc8ee81582'
down_revision = 'da5ea9248f4a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass