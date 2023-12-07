"""atalaya_brands

Revision ID: f04e6950473a
Revises: 
Create Date: 2023-10-11 03:30:07.399349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f04e6950473a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "atalaya_brands",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("brand", sa.String(120), nullable=False),
        sa.Column("brand_code", sa.String(40), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("brand_id", sa.BigInteger, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("atalaya_brands")
