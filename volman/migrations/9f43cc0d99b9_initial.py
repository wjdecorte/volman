"""Initial

Revision ID: 9f43cc0d99b9
Revises:
Create Date: 2020-12-15 12:09:18.172191

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9f43cc0d99b9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "file_connector",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("create_date", sa.DateTime(), nullable=True),
        sa.Column("modify_date", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=40), nullable=False),
        sa.Column("protocol", sa.String(length=10), nullable=False),
        sa.Column("connection_name", sa.String(length=50), nullable=True),
        sa.Column("source_file_path", sa.String(length=500), nullable=True),
        sa.Column("target_file_path", sa.String(length=500), nullable=False),
        sa.Column("append_timestamp", sa.Boolean(), nullable=True),
        sa.Column("schema_id", sa.String(length=100), nullable=True),
        sa.Column("client_id", sa.String(length=100), nullable=True),
        sa.Column("user_id", sa.String(length=100), nullable=True),
        sa.Column("tags", sa.JSON(), nullable=True),
        sa.Column("file_name_tags_regex", sa.JSON(), nullable=True),
        sa.Column("file_format", sa.String(length=20), nullable=True),
        sa.Column("file_format_regex", sa.String(length=100), nullable=True),
        sa.Column("file_type", sa.String(length=20), nullable=True),
        sa.Column("column_mapping_policy", sa.String(length=20), nullable=True),
        sa.Column("delimiter", sa.String(length=1), nullable=True),
        sa.Column("header_rows", sa.Integer(), nullable=True),
        sa.Column("trailer_rows", sa.Integer(), nullable=True),
        sa.Column("xml_path", sa.String(length=500), nullable=True),
        sa.Column("json_path", sa.String(length=500), nullable=True),
        sa.Column("excel_sheet_number", sa.Integer(), nullable=True),
        sa.Column("excel_header_row_numbers", sa.ARRAY(sa.Integer()), nullable=True),
        sa.Column("dag_config", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("file_connector")
    # ### end Alembic commands ###
