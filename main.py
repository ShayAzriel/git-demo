"""This python script iterates a github given branch commit history
 and prints to screen 5 recent(or as specified) commit objects main information"""
# !/usr/bin/env python3
import argparse
from github import Github


def print_commit(commit):
    """Prints git commit according to the normal format: commit id(sha)->author->date->Message->space."""
    print(f"Commit {commit.sha}")
    print(f"Author: {commit.commit.author.name}")
    print(f"Date:   {commit.commit.author.date}")
    print(f"    {commit.commit.message}", end='\n\n')


def git_handler(username, repository, branch_name=None, commits_num=5):
    """Handling the git information to get the commits history info and then printing it"""
    git = Github()
    git_repo = git.get_repo(f"{username}/{repository}")
    # use the provided branch or the default branch:
    git_branch = branch_name if branch_name is not None else git_repo.default_branch
    commits = git_repo.get_commits(sha=git_branch)[:commits_num]
    for commit in commits:
        print_commit(commit)


def arguments_handler():
    """Handles the parsing of the arguments for the required git information."""
    parser = argparse.ArgumentParser(description="GitHub Repository Information")
    parser.add_argument("username", help="The username")
    parser.add_argument("repository", help="The repository name")
    parser.add_argument("--branch_name", default=None, help="(Optional) The branch name; default: default branch")
    parser.add_argument("--commits_num", type=int, default=5,
                        help="(Optional) number of the latest commits(int); default: 5")
    return parser


if __name__ == '__main__':
    args = arguments_handler().parse_args()
    git_handler(args.username, args.repository, args.branch_name, args.commits_num)
