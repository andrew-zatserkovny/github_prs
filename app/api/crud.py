from pypika import CustomFunction
from tortoise.expressions import F
from tortoise.functions import Function
from typing import List, Dict
from app.models.tortoise import PullRequest, PullRequestFile
from tortoise.functions import Count, Min, Max, Avg


async def get_top_three_files() -> List:
    top_three_result = (
        await PullRequestFile
            .annotate(total_count=Count("id"))
            .group_by("filename")
            .order_by("-total_count")
            .limit(3)
            .values("filename", "total_count")
    )
    print(top_three_result)
    print(type(top_three_result))
    return top_three_result


async def get_pr_stats() -> List:
    pr_stats_result = (
        await PullRequest
            .annotate(
                min=Min("duration"),
                max=Max("duration"),
                avg=Avg("duration")
            )
            .filter(state='closed')
            .limit(1)
            .values("min", "max", "avg")
    )
    print(pr_stats_result)
    print(type(pr_stats_result))
    return pr_stats_result
