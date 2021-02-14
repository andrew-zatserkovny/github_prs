from pydantic import BaseModel


class TopThreeFilesResponseSchema(BaseModel):
    filename: str
    total_count: int


class PullRequestStatsResponseSchema(BaseModel):
    min: float
    max: float
    avg: float
