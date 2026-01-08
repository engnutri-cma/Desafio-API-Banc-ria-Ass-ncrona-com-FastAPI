import asyncio
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from models.models import Base
target_metadata = Base.metadata

def run_migrations_offline():
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url.replace("sqlite:///", "sqlite+aiosqlite:///"),
        target_metadata=target_metadata,
        literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations_sync(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    configuration = context.config
    connectable = create_async_engine(
        configuration.get_main_option("sqlalchemy.url").replace("sqlite:///", "sqlite+aiosqlite:///")
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations_sync)
    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
