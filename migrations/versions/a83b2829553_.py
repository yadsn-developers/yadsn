"""empty message

Revision ID: a83b2829553
Revises: None
Create Date: 2015-01-25 01:57:00.238498

"""

# revision identifiers, used by Alembic.
revision = 'a83b2829553'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriber',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('codecha_language', sa.String(), nullable=True),
                    sa.Column('added_at', sa.DateTime(), nullable=True),
                    sa.Column('http_referrer', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscriber')
    ### end Alembic commands ###
