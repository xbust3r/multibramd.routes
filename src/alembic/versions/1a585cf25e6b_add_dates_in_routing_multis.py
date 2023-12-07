"""add dates in routing_multis

Revision ID: 1a585cf25e6b
Revises: 42377e8220b3
Create Date: 2023-10-22 05:48:59.757396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a585cf25e6b'
down_revision: Union[str, None] = '42377e8220b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('atalaya_routing_multi', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('atalaya_routing_multi', sa.Column('updated_at', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('atalaya_routing_multi', 'updated_at')
    op.drop_column('atalaya_routing_multi', 'created_at')
