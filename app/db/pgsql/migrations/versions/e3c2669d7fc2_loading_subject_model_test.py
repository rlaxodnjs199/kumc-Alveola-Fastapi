"""Loading Subject model test

Revision ID: e3c2669d7fc2
Revises: b6b156bdac33
Create Date: 2023-02-28 12:34:14.110918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3c2669d7fc2'
down_revision = 'b6b156bdac33'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'project', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'project', type_='unique')
    # ### end Alembic commands ###
