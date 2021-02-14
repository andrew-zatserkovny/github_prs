from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class PullRequest(models.Model):
    number = fields.IntField(pk=True)
    title = fields.CharField(max_length=250)
    url = fields.CharField(max_length=100)
    created_at = fields.DatetimeField()
    merged_at = fields.DatetimeField(null=True)
    duration = fields.FloatField(null=True)
    state = fields.CharField(max_length=20)

    def __str__(self):
        return self.title


PullRequestSchema = pydantic_model_creator(PullRequest)


class PullRequestFile(models.Model):
    pr_number = fields.IntField()
    filename = fields.CharField(max_length=250)
    raw_url = fields.CharField(max_length=250, null=True)

    def __str__(self):
        return self.filename


PullRequestFileSchema = pydantic_model_creator(PullRequestFile)
