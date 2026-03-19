"""Add index on item.owner_id

Revision ID: 3c9d2e1f4a87
Revises: fe56fa70289e
Create Date: 2026-03-19 00:00:00.000000

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '3c9d2e1f4a87'
down_revision = 'fe56fa70289e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('ix_item_owner_id', 'item', ['owner_id'])


def downgrade():
    op.drop_index('ix_item_owner_id', table_name='item')
