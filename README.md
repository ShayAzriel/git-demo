
assumptions:
1)	The task interacts with the GitHub API only (thus the use of PygitHub library, can be also - GitHub public REST API). general use for interacting with git repositories needs to be done with GitPython library.
2)	The user needs to install PyGithub via "pip install PyGithub" command or via some Python IDE's.
3)	This task handles public repositories only, as requested.
4)	I didn’t implement try-except on some cases, as we didn't discuss that– but the libraries I used throw exceptions and exits (if we encounter any error).  I will add it if needed for informative error messages or other error handling and logging options.

command: python3 main.py username repository --branch <branch_name> --commits_num <num>
optional flags: --branch ; --commits_num  (int)
