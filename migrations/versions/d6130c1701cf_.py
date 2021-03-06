"""empty message

Revision ID: d6130c1701cf
Revises: 
Create Date: 2018-07-09 14:51:09.011567

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd6130c1701cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=True)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('params', postgresql.JSONB(astext_type=False), nullable=True),
    sa.Column('img_path', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_description'), 'product', ['description'], unique=False)
    op.create_index(op.f('ix_product_img_path'), 'product', ['img_path'], unique=True)
    op.create_index(op.f('ix_product_params'), 'product', ['params'], unique=False)
    op.create_index(op.f('ix_product_title'), 'product', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_title'), table_name='product')
    op.drop_index(op.f('ix_product_params'), table_name='product')
    op.drop_index(op.f('ix_product_img_path'), table_name='product')
    op.drop_index(op.f('ix_product_description'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
