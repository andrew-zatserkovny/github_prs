from typing import List
from fastapi import APIRouter, HTTPException
from app.api import crud
from app.models.pydantic import TopThreeFilesResponseSchema, PullRequestStatsResponseSchema


router = APIRouter()


@router.get("/top/", response_model=List[TopThreeFilesResponseSchema])
async def read_top_three_files() -> List[TopThreeFilesResponseSchema]:
    return await crud.get_top_three_files()


@router.get("/stats/", response_model=List[PullRequestStatsResponseSchema])
async def read_pr_stats() -> List[PullRequestStatsResponseSchema]:
    return await crud.get_pr_stats()
