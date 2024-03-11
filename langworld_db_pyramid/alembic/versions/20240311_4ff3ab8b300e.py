"""add_value_description

Revision ID: 4ff3ab8b300e
Revises: 8bbc29e60d27
Create Date: 2024-03-11 13:27:56.699071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ff3ab8b300e'
down_revision = '8bbc29e60d27'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature_values', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description_html_en', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('description_html_ru', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature_values', schema=None) as batch_op:
        batch_op.drop_column('description_html_ru')
        batch_op.drop_column('description_html_en')

    # ### end Alembic commands ###
