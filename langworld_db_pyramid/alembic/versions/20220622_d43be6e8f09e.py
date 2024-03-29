"""add attribute 'entails_empty_value' to FeatureValueType

Revision ID: d43be6e8f09e
Revises: 66ae23254e01
Create Date: 2022-06-22 12:43:35.925685

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd43be6e8f09e'
down_revision = '66ae23254e01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature_value_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('entails_empty_value', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature_value_types', schema=None) as batch_op:
        batch_op.drop_column('entails_empty_value')

    # ### end Alembic commands ###
