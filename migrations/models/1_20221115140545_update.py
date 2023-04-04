from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "id" VARCHAR(30) NOT NULL  PRIMARY KEY,
    "role" VARCHAR(8) NOT NULL  DEFAULT 'agent',
    "account_id" VARCHAR(30) NOT NULL UNIQUE,
    "status" VARCHAR(11) NOT NULL  DEFAULT 'in_progress'
);
COMMENT ON COLUMN "users"."role" IS 'agent: agent';
COMMENT ON COLUMN "users"."status" IS 'in_progress: in_progress\nactive: active';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users";"""
