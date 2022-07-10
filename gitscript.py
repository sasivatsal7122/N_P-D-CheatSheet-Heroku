import streamlit as st
# from streamlit.commands.page_config import PageIcon


# st.set_page_config(layout="wide",page_title="GitHub CheatSheet",PageIcon='📝')



def cs_body():
    st.title("Git Cheatsheet: ")
    st.markdown("<p><TT>Designed and Developed by <a style='text-decoration:none;color:red' target='_blank' href='https://github.com/sasivatsal7122'>B.Sasi Vatsal</a> & <a style='text-decoration:none;color:red' target='_blank' href='https://github.com/SaiMowli'>D.Sai Mowli</a></TT></p>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.subheader('Setup')
    col1.code('''
 # Set the name and email that will be
 # attached to your commits and tags
 $ git config --global
 user.name "Sai Mowli"
 $ git config --global
 user.mail "Mymail@gmail.com"
    ''')

    col1.subheader('Start a Project')
    col1.code('''
 #Create a local repo(omit<dictionary>) to 
 # initialize the current repo as a git repo
 $ git init <dictionary>
 # Download a remote repo
 $ git clone <url>
    ''')

    col1.subheader('Make Change')
    col1.code('''
 # Add a file to staging
 $ git add <file>
 #Stage all files
 $ git add .
 # Commit all staged files to git
 $ git commit -m "Commit message"
 # Add all changes made to 
 # tracked files and commit
 $ git commit -am "Commit message"

    ''')

    col1.subheader('Basic commands')
    col1.code('''
 # List which files are staged,
 # unstaged, and untracked.
 $ git status
 # Display the entire commit history
 # using the default format.
 # For customization see additional options.
 $ git log
 # Show unstaged changes between 
 # your index and working directory.
 $ git diff
    ''')

    col1.subheader('Undoing Changes')
    col1.code('''
 # Create new commit that undoes all of the changes made in
 # <commit>, then apply it to the current branch.
 $ git revert <commit>
 # Remove <file> from the staging area, but leave the working
 # directory unchanged. This unstages a file 
 # without overwriting any changes.
 $ git reset <file>
 # Shows which files would be removed from working directory.
 # Use the -f flag in place of the -n flag to execute the clean.
 $ git clean -n
    ''')

    col1.subheader('Rewriting Git History')
    col1.code('''
 # Replace the last commit with the staged changes and last commit
 # combined. Use with nothing staged to edit the last commit's message.
 $ git commit --amend
 # Rebase the current branch onto <base>. <base> can be a commit ID,
 # branch name, a tag, or a relative reference to HEAD.
 $ git rebase <base>
 # Show a log of changes to the local repository's HEAD.
 # Add --relative-date flag to show date info or --all to show all refs. 
 $ git reflog
    ''')

    col1.subheader('Git Reset')
    col1.code('''
    # Reset staging area to match most recent commit,
    # but leave the working directory unchanged.
    $ git reset
    # Reset staging area and working directory to match most recent
    # commit and overwrites all changes in the working directory.
    $ git reset --hard
    # Move the current branch tip backward to <commit>, reset the
    # staging area to match, but leave the working directory alone.
    $ git reset <commit>
    # Same as previous, but resets both the staging area & working directory to
    # match. Deletes uncommitted changes, and all commits after <commit>.
    $ git reset --hard <commit>
    ''')

    col1.subheader('Git Diff')
    col1.code('''
    # Show difference between working directory and last commit.
    $ git diff HEAD
    # Show difference between staged changes and last commit
    $ git diff --cached
    ''')


    col2.subheader('Git Branches')
    col2.code('''
  # List all of the branches in your repo. Add a <branch> argument to
  # create a new branch with the name <branch>.
  $ git branch
  # Create and check out a new branch named <branch>.
  # Drop the -b flag to checkout an existing branch.
  $ git checkout -b <branch>
  # Merge <branch> into the current branch.
  $ git merge <branch>
    ''')

    col2.subheader('Remote Repositories')
    col2.code('''
  # Create a new connection to a remote repo. After adding a remote,
  # you can use <name> as a shortcut for <url> in other commands.
  $ git remote add <name> <url> 
  # Fetches a specific <branch>, from the repo. Leave off <branch>
  # to fetch all remote refs.
  $ git fetch <remote> <branch>
  # Fetch the specified remote's copy of current branch and
  # immediately merge it into the local copy.
  $ git pull <remote>
  # Push the branch to <remote>, along with necessary commits and
  # objects. Creates named branch in the remote repo if it doesn't exist.
  $ git push <remote> <branch>
    ''')

    col2.subheader('Other Git Config Commands')
    col2.code('''
  # Create shortcut for a Git command. E.g. alias.glog “log --graph
  # --oneline” will set ”git glog” equivalent to ”git log --graph --oneline.
  $ git config --global
  alias. <alias-name>
  <git-command>
  # Set text editor used by commands for all users on the machine. <editor>
  # arg should be the command that launches the desired editor (e.g., vi).
  $ git config --system
  core.editor <editor>
  # Open the global configuration file in a text editor for manual editing.
  $ git config --global --edit
    ''')

    col2.subheader('Git Log')
    col2.code('''
    # Limit number of commits by <limit>.
    # E.g. ”git log -5” will limit to 5 commits.
    $ git log -<limit>
    # Condense each commit to a single line.
    $ git log --oneline
    # Display the full diff of each commit.
    $ git log -p
    # Include which files were altered and the relative number of
    # lines that were added or deleted from each of them.
    $ git log --stat
    # Search for commits by a particular author.
    $ git log --author=”<pattern>”
    # Search for commits with a commit message that
    # matches <pattern>.
    $ git log --grep=”<pattern>”
    # Show commits that occur between <since> and <until>. Args can be a
    # commit ID, branch name, HEAD, or any other kind of revision reference.
    $ git log <since>..<until>
    # Only display commits that have the specified file.
    $ git log -- <file>
    # --graph flag draws a text based graph of commits on left side of commit
    # msgs. --decorate adds names of branches or tags of commits shown.
    $ git log --graph --decorate
    ''')

    col2.subheader('Git Rebase')
    col2.code('''
    # Interactively rebase current branch onto <base> . Launches editor to enter
    # commands for how each commit will be transferred to the new base.
    $ git rebase -i <base>
    ''')

    col2.subheader('Git Pull')
    col2.code('''
    # Fetch the remote's copy of current branch and rebases it into the local
    # copy. Uses git rebase instead of merge to integrate the branches.
    $ git pull --rebase <remote>
    ''')

    col2.subheader('Git Push')
    col2.code('''
    # Forces the git push even if it results in a non-fast-forward merge. Do not use
    # the --force flag unless you're absolutely sure you know what you're doing.
    $ git push <remote> --force
    # Push all of your local branches to the specified remote.
    $ git push <remote> --all
    # Tags aren't automatically pushed when you push a branch or use the
    # --all flag. The --tags flag sends all of your local tags to the remote repo.
    $ git push <remote> --tags
    ''')


def main():
    st.header('')
    cs_body()