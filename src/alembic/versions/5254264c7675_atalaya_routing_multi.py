"""atalaya_routing_multi

Revision ID: 5254264c7675
Revises: 2e03b560b9a7
Create Date: 2023-10-11 04:02:20.288483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5254264c7675'
down_revision: Union[str, None] = '2e03b560b9a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "atalaya_routing_multi",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("current", sa.Integer, nullable=False),
        sa.Column("total", sa.Integer, nullable=False),
        sa.Column("variables", sa.JSON, nullable=False),
        sa.Column("brand_id", sa.BigInteger, sa.ForeignKey("atalaya_brands.id"), nullable=False),
        sa.Column("configuration_id", sa.BigInteger, sa.ForeignKey("atalaya_configuration.id"), nullable=False),
        
    )


def downgrade() -> None:
    op.drop_table("atalaya_routing_multi")
