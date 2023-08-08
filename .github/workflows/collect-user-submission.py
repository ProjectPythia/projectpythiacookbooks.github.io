import json
import os
import typing

class Submission:
    def __init__(self, repo: str):
        self.repo = repo

class IssueInfo:
    def __init__(self, gh_event_path: str):
        self.gh_event_path = gh_event_path

    def get_event_data(self):
        with open(self.gh_event_path) as f:
            return json.load(f)

    def create_submission(self):
        event_data = self.get_event_data()
        issue_body = event_data["issue"]["body"]
        submission = self._create_submission_input(issue_body)
        return submission

    def _create_submission_input(self, text: str):
        left = "### Root Repository Name"
        right = "### Did you check"
        repo = text[text.index(left) + len(left) : text.index(right)].strip()
        return Submission(repo=repo)


if __name__ == "__main__":
    gh_event_path = os.environ["GITHUB_EVENT_PATH"]
    issue = IssueInfo(gh_event_path=gh_event_path).create_submission()
    with open("cookbook-submission-input.txt", "w") as f:
        f.write(issue.repo)
