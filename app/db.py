import logging
import os
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise
from tortoise.transactions import in_transaction

log = logging.getLogger("uvicorn")


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"model": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initalizing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"), modules={"model": ["models.tortoise"]}
    )

    log.info("Generating database schema via Tortoise...")

    await Tortoise.generate_schemas(safe=True)

    log.info("Populating pull requests...")

    async with in_transaction("default") as tconn:
        await tconn.execute_script("""
            TRUNCATE TABLE pullrequest;

            INSERT INTO pullrequest (
              number,
              title,
              url,
              created_at,
              merged_at,
              duration,
              state
            )
            SELECT
              number,
              title,
              url,
              created_at,
              merged_at,
              EXTRACT(EPOCH FROM merged_at - created_at) AS duration,
              state
            FROM airflow.pull_requests
        """)

        await tconn.execute_script("""
            TRUNCATE TABLE pullrequestfile;

            INSERT INTO pullrequestfile (
              pr_number,
              filename,
              raw_url
            )
            SELECT
              pr_number,
              filename,
              raw_url
            FROM airflow.files
        """)

    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
