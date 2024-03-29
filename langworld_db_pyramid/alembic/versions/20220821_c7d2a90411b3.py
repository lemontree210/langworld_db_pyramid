"""Create indices

Revision ID: c7d2a90411b3
Revises: 0c3e2f3328c3
Create Date: 2022-08-21 14:46:57.398848

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c7d2a90411b3'
down_revision = '0c3e2f3328c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('doculects', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_doculects_aliases_en'), ['aliases_en'], unique=False)
        batch_op.create_index(batch_op.f('ix_doculects_aliases_ru'), ['aliases_ru'], unique=False)
        batch_op.create_index(batch_op.f('ix_doculects_has_feature_profile'), ['has_feature_profile'], unique=False)
        batch_op.create_index(batch_op.f('ix_doculects_man_id'), ['man_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_doculects_name_en'), ['name_en'], unique=False)
        batch_op.create_index(batch_op.f('ix_doculects_name_ru'), ['name_ru'], unique=False)

    with op.batch_alter_table('families', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_families_man_id'), ['man_id'], unique=False)

    with op.batch_alter_table('feature_categories', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_feature_categories_man_id'), ['man_id'], unique=False)

    with op.batch_alter_table('feature_values', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_feature_values_man_id'), ['man_id'], unique=False)

    with op.batch_alter_table('features', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_features_man_id'), ['man_id'], unique=False)

    with op.batch_alter_table('glottocodes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_glottocodes_code'), ['code'], unique=False)

    with op.batch_alter_table('iso_639p3_codes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_iso_639p3_codes_code'), ['code'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('iso_639p3_codes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_iso_639p3_codes_code'))

    with op.batch_alter_table('glottocodes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_glottocodes_code'))

    with op.batch_alter_table('features', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_features_man_id'))

    with op.batch_alter_table('feature_values', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_feature_values_man_id'))

    with op.batch_alter_table('feature_categories', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_feature_categories_man_id'))

    with op.batch_alter_table('families', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_families_man_id'))

    with op.batch_alter_table('doculects', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_doculects_name_ru'))
        batch_op.drop_index(batch_op.f('ix_doculects_name_en'))
        batch_op.drop_index(batch_op.f('ix_doculects_man_id'))
        batch_op.drop_index(batch_op.f('ix_doculects_has_feature_profile'))
        batch_op.drop_index(batch_op.f('ix_doculects_aliases_ru'))
        batch_op.drop_index(batch_op.f('ix_doculects_aliases_en'))

    # ### end Alembic commands ###
