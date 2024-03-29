"""Add column man_id to EncyclopediaMap

Revision ID: 31f7393c69c5
Revises: bc7c98b048ca
Create Date: 2022-08-21 18:30:10.497098

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '31f7393c69c5'
down_revision = 'bc7c98b048ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('encyclopedia_maps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('man_id', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('encyclopedia_maps', schema=None) as batch_op:
        batch_op.drop_column('man_id')

    # ### end Alembic commands ###
