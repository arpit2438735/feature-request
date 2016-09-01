"""empty message

Revision ID: 05a9274e867d
Revises: None
Create Date: 2016-09-01 21:32:20.111819

"""

# revision identifiers, used by Alembic.
revision = '05a9274e867d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.String(length=22), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.String(length=22), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('request',
    sa.Column('id', sa.String(length=22), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('client', sa.String(), nullable=True),
    sa.Column('client_priority', sa.Integer(), nullable=False),
    sa.Column('target_date', sa.Date(), nullable=True),
    sa.Column('ticket_url', sa.String(length=300), nullable=True),
    sa.Column('product_area', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['client'], ['client.id'], ),
    sa.ForeignKeyConstraint(['product_area'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    op.drop_table('product')
    op.drop_table('client')
    ### end Alembic commands ###
