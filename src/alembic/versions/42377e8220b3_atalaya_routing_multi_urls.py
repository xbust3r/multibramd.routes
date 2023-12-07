"""atalaya_routing_multi_urls

Revision ID: 42377e8220b3
Revises: 5254264c7675
Create Date: 2023-10-11 04:05:52.710602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42377e8220b3'
down_revision: Union[str, None] = '5254264c7675'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "atalaya_routing_multi_urls",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("order", sa.Integer, nullable=False),
        sa.Column("url", sa.String(220), nullable=False),
        sa.Column("domain", sa.String(60), nullable=False),
        sa.Column("routing_multi_id", sa.BigInteger, sa.ForeignKey("atalaya_routing_multi.id"), nullable=False),
    )


def downgrade() -> None:
    pass
