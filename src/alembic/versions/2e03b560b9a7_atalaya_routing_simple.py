"""atalaya_routing_simple

Revision ID: 2e03b560b9a7
Revises: 349508b7203c
Create Date: 2023-10-11 03:55:15.808971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e03b560b9a7'
down_revision: Union[str, None] = '349508b7203c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "atalaya_routing_single",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("url", sa.String(220), nullable=False),
        sa.Column("domain", sa.String(60), nullable=False),
        sa.Column("variables", sa.JSON, nullable=False),
        sa.Column("brand_id", sa.BigInteger, sa.ForeignKey("atalaya_brands.id"), nullable=False),
        sa.Column("configuration_id", sa.BigInteger, sa.ForeignKey("atalaya_configuration.id"), nullable=False),
        
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("atalaya_routing_simple")
