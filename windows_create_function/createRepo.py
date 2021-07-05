import sys, os
from github import Github
from secretData import gitToken, gitIgnoreList

def create_local_repo(repo_name=str, repo_path=str, gitIgnoreList=list) -> None:
    """Create a local repository in a given projects folder

    Args:
        repo_name (str, optional): Project or repository name. Defaults to str.
        projects_path (str, optional): Projects folder location. Defaults to str.
        gitIgnoreList (list, optional): git ignore list for new project. Defaults to list.
    """
    # create a folder of new repo
    os.mkdir(repo_path)
    os.chdir(repo_path)

    # files needed in new repos
    for file in gitIgnoreList:
        os.system(f'echo {file} >> .gitignore')
    os.system(f'echo {repo_name} >> README.md')

    # Start local repo
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "first commit"')

    print('\nLocal repository sucessfully created in ' + repo_path)


def create_github_repo(token=str, repo_name=str) -> str:
    """Create a new repo in github using the name given in terminal.

    Args:
        token (string): usr and password for github generated for this specific task. Defaults to str.
        repo_name (string): The name for new repository. Defaults to str.
        webpage (string, optional): github webpage. Defaults to 'https://github.com/'.
    """
    g = Github(token)
    user = g.get_user()
    username = user.login
    user.create_repo(repo_name)
    repo_url = f'https://github.com/{username}/{repo_name}.git'

    print('\nRemote repository sucessfully created in ' + repo_url)
    return repo_url


def link_repos(repo_path=str, repo_url=str) -> None:
    """use the terminal to link a remote branch to a new local branch.

    Args:
        repo_name (string, optional): The projects name. Defaults to str.
        projects_path (string, optional): the project location using absolute path. Defaults to str.
        webpage (string, optional): github webpage. Defaults to 'https://github.com/'.
    """
    os.system('cd ' + repo_path)
    os.system('git remote add origin ' + repo_url)
    os.system('git push -u origin master')

    print('\nProject Linked sucessfully!')


def create_pyenv(repo_path=str) -> None:
    """Create a Python3 virtual enviroment inside a new local project

    Args:
        projects_path (str, optional): Projects folder location in absolute path. Defaults to str.
        repo_name (str, optional): name of the project or repository. Defaults to str.
    """
    os.system('cd ' + repo_path)
    
    py = ('python3' if os.name != 'nt' else 'py')
    os.system(f'{py} -m venv env')
    print('\nvitual enviroment sucessfully created in ' + repo_path)


def main():
    # Arguments for functions in secrets
    token = gitToken
    git_ignore_list = gitIgnoreList

    # get path
    current_path = os.getcwd().replace('\\', '/').split('/')
    current_path = os.path.abspath(__file__).replace('\\', '/').split('/')
    
    if os.name == 'nt':
        projects_path = 'C:'
    else:
        projects_path = ''
    for folder in current_path[1:-3]:  # 2 levels up
        projects_path += '/' + folder
    print(projects_path)
    # System arguments
    args = sys.argv
    repo_name = ''
    if len(args) < 2:
        repo_name = input("\nWrite the project's name without spaces between words: ")
        if type(repo_name) is not str or repo_name == '' or ' ' in repo_name:
            print('[ERROR]: Write a name to your new project')
            return None

    # set repository name if is after command
    if repo_name == '':
        repo_name = args[1]
    repo_path = f'{projects_path}/{repo_name}'

    # Main functions
    try:
        if '--help' in args:
            print("""

              You shoud write: create <project_name> <options>

              Options: -no_local : Only make a remote repo
                       -no_remote : Only make a local repo
                       -pyenv : Create a python vitual enviroment

                       """)
            return None

        if '-no_local' not in args:
            create_local_repo(repo_name, repo_path, git_ignore_list)
        if '-no_remote' not in args:
            repo_url = create_github_repo(token, repo_name)
        if '-no_local' not in args and '-no_remote' not in args:
            link_repos(repo_path, repo_url)
        if '-pyenv' in args and '-no_local' not in args:
            create_pyenv(repo_path)
        if '-no_local' not in args:
            os.system('code .')
        if '-no_local' in args and '-no_remote' in args:
            print('\n[ERROR]: Create a repo in local or remote.')

    except Exception as e:
        print('[ERROR]:', e)
        return None


if __name__ == "__main__":
    main()
