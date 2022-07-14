"""create users table

Revision ID: 228c129080a2
Revises: d5c40ae4929a
Create Date: 2022-07-13 12:00:38.258698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228c129080a2'
down_revision = 'd5c40ae4929a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
