"""add content column to posts table

Revision ID: d5c40ae4929a
Revises: a95da613caad
Create Date: 2022-07-13 11:45:31.121454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5c40ae4929a'
down_revision = 'a95da613caad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
