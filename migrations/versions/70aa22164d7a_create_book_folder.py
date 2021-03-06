"""Create book folder

Revision ID: 70aa22164d7a
Revises: 
Create Date: 2022-07-17 22:44:29.704765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70aa22164d7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_table('reader_model',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reader_model')
    op.drop_table('books')
    # ### end Alembic commands ###
