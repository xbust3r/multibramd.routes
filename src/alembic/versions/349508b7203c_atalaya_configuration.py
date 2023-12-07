"""atalaya_configuration

Revision ID: 349508b7203c
Revises: f04e6950473a
Create Date: 2023-10-11 03:36:06.810545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '349508b7203c'
down_revision: Union[str, None] = 'f04e6950473a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "atalaya_configuration",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("title", sa.String(220), nullable=False),
        sa.Column("language", sa.String(3), nullable=False),
        sa.Column("insurance", sa.String(10), nullable=False),
        sa.Column("device", sa.String(5), nullable=False),
        sa.Column("media", sa.String(10), nullable=False),
        sa.Column("state", sa.String(3), nullable=False),
        sa.Column("type", sa.Boolean, nullable=False),
        sa.Column("brand_id", sa.BigInteger, sa.ForeignKey("atalaya_brands.id"), nullable=False),
        sa.Column("brand", sa.String(120), nullable=False),
        sa.Column("system", sa.String(20), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("atalaya_configuration")
