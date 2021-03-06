"""add state column to office structures

Revision ID: aabedbfac0dd
Revises: 0f7bdb8ab991
Create Date: 2019-05-29 11:47:11.081319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aabedbfac0dd'
down_revision = '0f7bdb8ab991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('office_structures', sa.Column('state', sa.Enum('active', 'archived', 'deleted', name='statetype'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('office_structures', 'state')
    # ### end Alembic commands ###
