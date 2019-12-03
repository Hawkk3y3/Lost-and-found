"""Updated Items Model and Added foreign key

Revision ID: e118477f1c48
Revises: 63039513dff0
Create Date: 2019-11-27 15:59:58.125844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e118477f1c48'
down_revision = '63039513dff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Items', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Items', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Items', type_='foreignkey')
    op.drop_column('Items', 'user_id')
    # ### end Alembic commands ###
