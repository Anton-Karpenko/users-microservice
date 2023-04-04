# Users Private Service

## Local development

### Setup

We highly recommend to use provided script to setup everything by single command.
Just run the following command from project's root directory and follow instructions:

* `bin/setup`

That's all!

### Style guides and name conventions

#### Linters and code-formatters

We use git-hooks to run linters and formatters before any commit.
It installs git-hooks automatically if you used `bin/setup` command.
So, if your commit is failed then check console to see details and fix linter issues.

We use:

* black - code formatter
* mypy - static type checker
* flake8 - logical and stylistic lint
* flake8-bandit - security linter
* safety - security check for requirements

and few other flake8 plugins, check `requirements/development.txt` for more details.

In order to run checkers manually use the following bash script:

```bash
bin/pre-commit
```

### Base commands

```bash
docker-compose up  # To run FastAPI application server

# Useful commands
bin/pytest # Run tests
bin/aerich migrate  # Create migrations files based on `models` files
bin/aerich upgrade  # Run database migrations
bin/shell  # Run python shell
```

### Invite an agent
`python -m apps.common.run_command users.invite_agent -email=<TYPE EMAIL>`
