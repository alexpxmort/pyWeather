"""Add daily_summary table

Revision ID: 4179f8f535d6
Revises: 90476e67ac81
Create Date: 2024-12-01 11:17:24.010370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4179f8f535d6'
down_revision = '90476e67ac81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('avg_temperature', sa.Float(), nullable=False),
    sa.Column('avg_humidity', sa.Float(), nullable=False),
    sa.Column('record_count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_summary')
    # ### end Alembic commands ###