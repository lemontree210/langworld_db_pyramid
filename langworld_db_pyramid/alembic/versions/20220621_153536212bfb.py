"""add class DoculectFeatureValueComment

Revision ID: 153536212bfb
Revises: dc033efc3629
Create Date: 2022-06-21 17:11:04.002726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '153536212bfb'
down_revision = 'dc033efc3629'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doculect_feature_value_comment',
    sa.Column('doculect_id', sa.Integer(), nullable=False),
    sa.Column('feature_value_id', sa.Integer(), nullable=False),
    sa.Column('text_en', sa.Text(), nullable=True),
    sa.Column('text_ru', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['doculect_id'], ['doculects.id'], name=op.f('fk_doculect_feature_value_comment_doculect_id_doculects')),
    sa.ForeignKeyConstraint(['feature_value_id'], ['feature_values.id'], name=op.f('fk_doculect_feature_value_comment_feature_value_id_feature_values')),
    sa.PrimaryKeyConstraint('doculect_id', 'feature_value_id', name=op.f('pk_doculect_feature_value_comment'))
    )
    with op.batch_alter_table('doculect_to_feature_value', schema=None) as batch_op:
        batch_op.drop_column('comment_en')
        batch_op.drop_column('comment_ru')

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('doculect_to_feature_value', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_ru', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('comment_en', sa.TEXT(), nullable=True))

    op.drop_table('doculect_feature_value_comment')
    # ### end Alembic commands ###