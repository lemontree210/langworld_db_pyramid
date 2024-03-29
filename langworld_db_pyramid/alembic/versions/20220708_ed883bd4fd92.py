"""create table for families (genealogy)


Revision ID: ed883bd4fd92
Revises: 98874f7b044e
Create Date: 2022-07-08 13:26:21.208902

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ed883bd4fd92'
down_revision = '98874f7b044e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'families', sa.Column('id', sa.Integer(), nullable=False), sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('man_id', sa.String(length=50), nullable=True),
        sa.Column('name_en', sa.String(length=255), nullable=True),
        sa.Column('name_ru', sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(['parent_id'], ['families.id'], name=op.f('fk_families_parent_id_families')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_families')))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('families')
    # ### end Alembic commands ###
