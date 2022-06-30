# spookyhook
Spookyhook is a proof of concept git hook for use with [pre-commit](www.pre-commit.com) that demonstrates that if write access to a git repo is compromised and that repo uses pre-commit, an attacker can perform arbitrary code execution on end users' systems when they attempt to perform a commit on that repo.


## How to Use
1. Prerequisite: [The victim system needs to have pre-commit installed on it.](https://pre-commit.com/#installation)
2. Create a repo
3. Add a file called .pre-commit-config.yaml with the following content and commit:
```
repos:
-   repo: https://github.com/aderon2/spookyhook
    rev: 0.0.9
    hooks:
    -   id: spookyhook
```
4. Now on the victim system, clone the repo that you created and use pre-commit to install the git hooks specified by the repo (spookyhook):
```
pre-commit install
```
5. As an example of arbitrary code being executed, any future commits on that repo by that end user will cause a timestamped file to be created in that directory.


## Attack Scenario
Write access to a repo that uses pre-commit is compromised.  Attacker modifies .pre-commit-config.yaml to point towards a malicious hook (such as spookyhook).  As part of their normal process, the victim uses pre-commit to install the git hooks specified by the repository in .pre-commit-config.yaml.  End user makes a commit.  Arbitrary code execution occurs.
