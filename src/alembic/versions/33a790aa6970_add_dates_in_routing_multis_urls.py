"""add dates in routing_multis_urls

Revision ID: 33a790aa6970
Revises: 1a585cf25e6b
Create Date: 2023-10-22 06:50:02.878822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33a790aa6970'
down_revision: Union[str, None] = '1a585cf25e6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('atalaya_routing_multi_urls', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('atalaya_routing_multi_urls', sa.Column('updated_at', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('atalaya_routing_multi_urls', 'updated_at')
    op.drop_column('atalaya_routing_multi_urls', 'created_at')
