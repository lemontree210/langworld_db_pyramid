"""FeatureValue: children->elements, add m2m

Revision ID: 710efc914057
Revises: 5c12c8e2a74b
Create Date: 2023-04-25 21:55:21.937565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '710efc914057'
down_revision = '5c12c8e2a74b'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature_value_compound_to_element',
    sa.Column('compound_id', sa.Integer(), nullable=False),
    sa.Column('element_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['compound_id'], ['feature_values.id'], name=op.f('fk_feature_value_compound_to_element_compound_id_feature_values')),
    sa.ForeignKeyConstraint(['element_id'], ['feature_values.id'], name=op.f('fk_feature_value_compound_to_element_element_id_feature_values')),
    sa.PrimaryKeyConstraint('compound_id', 'element_id', name=op.f('pk_feature_value_compound_to_element'))
    )
    with op.batch_alter_table('feature_values', schema=None) as batch_op:
        batch_op.add_column(sa.Column('element_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_feature_values_parent_id_feature_values', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_feature_values_element_id_feature_values'), 'feature_values', ['element_id'], ['id'])
        batch_op.drop_column('parent_id')

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature_values', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parent_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_feature_values_element_id_feature_values'), type_='foreignkey')
        batch_op.create_foreign_key('fk_feature_values_parent_id_feature_values', 'feature_values', ['parent_id'], ['id'])
        batch_op.drop_column('element_id')

    op.drop_table('feature_value_compound_to_element')
    # ### end Alembic commands ###
