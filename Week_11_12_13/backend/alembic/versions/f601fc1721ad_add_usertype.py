"""add usertype

Revision ID: f601fc1721ad
Revises: ed27fd602dbf
Create Date: 2025-10-31 10:30:22.121457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f601fc1721ad'
down_revision: Union[str, Sequence[str], None] = 'ed27fd602dbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    column = "ALTER TABLE user ADD COLUMN usertype VARCHAR(20) DEFAULT 'student' "
    op.execute(column)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    column = "ALTER TABLE user DROP COLUMN usertype"

    op.execute()
    pass
