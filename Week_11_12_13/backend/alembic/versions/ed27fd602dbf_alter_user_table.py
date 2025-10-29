"""alter user table

Revision ID: ed27fd602dbf
Revises: 
Create Date: 2025-10-29 14:26:16.908875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed27fd602dbf'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    column = "ALTER TABLE user ADD COLUMN Gender VARCHAR(20) DEFAULT 'FEMALE' "
    op.execute(column)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    column = "ALTER TABLE user DROP COLUMN Gender"

    op.execute()
    pass
