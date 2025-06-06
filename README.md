
[//]: # (README.md generated from docs/partials/README_*.md)

# 🧠 template-demo

[![License](https://img.shields.io/github/license/pavel-trunov/template-demo?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/pavel-trunov/template-demo/blob/main/LICENSE)

[![CI](https://github.com/pavel-trunov/template-demo/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/pavel-trunov/template-demo/actions/workflows/ci-cd.yml)
[![Read the Docs](https://img.shields.io/readthedocs/template-demo)](https://template-demo.readthedocs.io/en/latest/)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=pavel-trunov_template-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pavel-trunov_template-demo)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=pavel-trunov_template-demo&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=pavel-trunov_template-demo)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=pavel-trunov_template-demo&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=pavel-trunov_template-demo)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=pavel-trunov_template-demo&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=pavel-trunov_template-demo)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pavel-trunov_template-demo&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pavel-trunov_template-demo)
[![CodeQL](https://github.com/pavel-trunov/template-demo/actions/workflows/codeql.yml/badge.svg)](https://github.com/pavel-trunov/template-demo/security/code-scanning)
[![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot)](https://github.com/pavel-trunov/template-demo/security/dependabot)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://github.com/pavel-trunov/template-demo/issues?q=is%3Aissue%20state%3Aopen%20Dependency%20Dashboard)
[![Coverage](https://codecov.io/gh/pavel-trunov/template-demo/graph/badge.svg?token=SX34YRP30E)](https://codecov.io/gh/pavel-trunov/template-demo)
[![Ruff](https://img.shields.io/badge/style-Ruff-blue?color=D6FF65)](https://github.com/pavel-trunov/template-demo/blob/main/noxfile.py)
[![MyPy](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/pavel-trunov/template-demo/blob/main/noxfile.py)
[![GitHub - Version](https://img.shields.io/github/v/release/pavel-trunov/template-demo?label=GitHub&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/pavel-trunov/template-demo/releases)
[![GitHub - Commits](https://img.shields.io/github/commit-activity/m/pavel-trunov/template-demo/main?label=commits&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/pavel-trunov/template-demo/commits/main/)




[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/pavel-trunov/template-demo)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/pavel-trunov/template-demo)
No
No

<!---
[![ghcr.io - Version](https://ghcr-badge.egpl.dev/pavel-trunov/template-demo/tags?color=%2344cc11&ignore=0.0%2C0%2Clatest&n=3&label=ghcr.io&trim=)](https://github.com/pavel-trunov/template-demo/pkgs/container/template-demo)
[![ghcr.io - Sze](https://ghcr-badge.egpl.dev/pavel-trunov/template-demo/size?color=%2344cc11&tag=latest&label=size&trim=)](https://github.com/pavel-trunov/template-demo/pkgs/container/template-demo)
-->

> [!TIP]
> 📚 [Online documentation](https://template-demo.readthedocs.io/en/latest/) - 📖 [PDF Manual](https://template-demo.readthedocs.io/_/downloads/en/latest/pdf/)

> [!NOTE]
> 🧠 This project was scaffolded using the template [oe-python-template](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template) with [copier](https://copier.readthedocs.io/).

---


Python project testing an oe-template usability and convenience.

### Scaffolding

This [Copier](https://copier.readthedocs.io/en/stable/) template enables you to quickly generate (scaffold) a Python package with fully functioning build and test automation:

1. Projects generated from this template can be [easily updated](https://copier.readthedocs.io/en/stable/updating/) to benefit from improvements and new features of the template.
2. During project generation, you can flexibly configure naming of the Python distribution, import package, main author, GitHub repository, organization, and many other aspects to match your specific requirements (see [copier.yml](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/copier.yml) for all available options).

### Development Infrastructure

Projects generated with this template come with a comprehensive development toolchain and quality assurance framework that supports the entire software development lifecycle - from coding and testing to documentation, release management, and compliance auditing. This infrastructure automates routine tasks, enforces code quality standards, and streamlines the path to production:

1. Linting with [Ruff](https://github.com/astral-sh/ruff)
2. Static type checking with [mypy](https://mypy.readthedocs.io/en/stable/)
3. Complete set of [pre-commit](https://pre-commit.com/) hooks including [detect-secrets](https://github.com/Yelp/detect-secrets) and [pygrep](https://github.com/pre-commit/pygrep-hooks)
4. Unit and E2E testing with [pytest](https://docs.pytest.org/en/stable/) including parallel test execution
5. Matrix testing in multiple environments with [nox](https://nox.thea.codes/en/stable/)
6. Test coverage reported with [Codecov](https://codecov.io/) and published as release artifact
7. CI/CD pipeline automated with [GitHub Actions](https://github.com/features/actions) with parallel and reusable workflows, including scheduled testing, release automation, and multiple reporting channels and formats
8. CI/CD pipeline can be run locally with [act](https://github.com/nektos/act)
9. Code quality and security checks with [SonarQube](https://www.sonarsource.com/products/sonarcloud) and [GitHub CodeQL](https://codeql.github.com/)
10. Dependency monitoring and vulnerability scanning with [pip-audit](https://pypi.org/project/pip-audit/), [trivy](https://trivy.dev/latest/), [Renovate](https://github.com/renovatebot/renovate), and [GitHub Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
11. Error monitoring and profiling with [Sentry](https://sentry.io/)  (optional)
12. Logging and metrics with [Logfire](https://logfire.dev/) (optional)
13. Prepared for uptime monitoring and scheduled tests with [betterstack](https://betterstack.com/) or alternatives
14. Licenses of dependencies extracted with [pip-licenses](https://pypi.org/project/pip-licenses/), matched with allow list, and published as release artifacts in CSV and JSON format for further compliance checks
15. Generation of attributions from extracted licenses
16. Software Bill of Materials (SBOM) generated in [CycloneDX](https://cyclonedx.org/) and [SPDX](https://spdx.dev/) formats with [cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) resp. [trivy](https://trivy.dev/latest/), published as release artifacts
17. Version and release management with [bump-my-version](https://callowayproject.github.io/bump-my-version/)
18. Changelog and release notes generated with [git-cliff](https://git-cliff.org/)
19. Documentation generated with [Sphinx](https://www.sphinx-doc.org/en/master/) including reference documentation for the library, CLI, and API
20. Documentation published to [Read The Docs](https://readthedocs.org/) including generation of PDF and single page HTML versions
21. Documentation including dynamic badges, setup instructions, contribution guide and security policy
22. Interactive OpenAPI specification with [Swagger](https://swagger.io/)
23. Python package published to [PyPI](https://pypi.org/)
24. Multi-stage build of fat (all extras) and slim (no extras) multi-arch (arm64 and amd64) Docker images, running non-root within immutable container
25. Docker images published to [Docker.io](https://hub.docker.com/) and [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) with [artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)
26. One-click development environments with [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) and [GitHub Codespaces](https://github.com/features/codespaces)
27. Settings for use with [VSCode](https://code.visualstudio.com/)
28. Settings and custom instructions for use with [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
29. API deployed as serverless function to [Vercel](https://vercel.com/) (optional)

### Multi-head Application Features

Beyond development tooling, projects generated with this template include the code, documentation, and configuration of a fully functioning service and multi-head application. This reference implementation serves as a starting point for your own business logic with modern patterns and enterprise practices already in place:

1. Usable as library with "Hello" module exposing a simple service that can say "Hello, world!" and echo utterances.
2. Comfortable command-line interface (CLI) with [Typer](https://typer.tiangolo.com/)
3. Versioned webservice API with [FastAPI](https://fastapi.tiangolo.com/)
4. Cross-platform Graphical User Interface (GUI) with
   [NiceGUI](https://nicegui.io/) running in a browser or native window
5. [Interactive Jupyter notebook](https://jupyter.org/) and [reactive Marimo notebook](https://marimo.io/)
6. Simple Web UI with [Streamlit](https://streamlit.io/)
7. Modular architecture auto-discovers and registers services, CLI commands, API routes and GUI pages exposed by domain modules
8. Validation and settings management with [pydantic](https://docs.pydantic.dev/)
9. System module providing aggregate health and info to the runtime, compiled settings, and further info provided by domain modules
10. Health and Info available via command, webservice API (info passsword protected) and GUI
11. Flexible logging and instrumentation, including support for [Sentry](https://sentry.io/) and [Logfire](https://logfire.dev/) 
12. Hello service demonstrates use of custom real time metrics collected via Logfire
13. Configuration to run the CLI and API in a Docker container including setup for [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/)

Explore [here](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example) for what's generated out of the box. While this template comes with multiple application interfaces ("heads") - Library, CLI, API, GUI, notebooks, and Streamlit; running native and within Docker - they're included to demonstrate capabilities and provide implementation patterns. You're expected to use this as a foundation, keeping only the interfaces relevant to your project's requirements. The modular architecture makes it easy to:

1. Remove unnecessary interfaces to simplify your codebase
2. Adapt existing interfaces to your specific use cases 
3. Focus on your core business logic without reimplementing infrastructure
4. Add new interfaces while leveraging the existing patterns


## Generate a new project

To generate, build and release a fully functioning project in a few minutes, follow these 5 steps:

**Step 1**: Execute the following command to install or update tooling.
```shell
# Install Homebrew, uv package manager, copier and further dev tools
curl -LsSf https://raw.githubusercontent.com/helmut-hoffer-von-ankershoffen/oe-python-template/HEAD/install.sh | sh
```

**Step 2**: [Create a repository on GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), clone to your local machine, and change into it's directory.

**Step 3**: Execute the following command to generate a new project based on this template.
```shell
# Ensure to stand in your freshly created git repository before executing this command
copier copy --trust gh:helmut-hoffer-von-ankershoffen/oe-python-template .
```

**Step 4**: Execute the following commands to push your initial commit to GitHub.
```shell
git add .
git commit -m "chore: Initial commit"
git push
```

Check the [Actions tab](https://github.com/pavel-trunov/template-demo/actions) of your GitHub repository: The CI/CD workflow of your project is already running!

The workflow will fail at the SonarQube step, as this external service is not yet configured for our new repository. We will configure SonarQube and other services in the next step!

Notes:
1. Check out [this manual](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key) on how to set up signed commits

**Step 5**: Follow the [instructions](SERVICE_CONNECTIONS.md) to wire up
external services such as CloudCov, SonarQube Cloud, Read The Docs, Docker.io, and Streamlit Community Cloud.

**Step 6**: Release the first version of your project
```shell
make bump
```
Notes:
1. You can remove the above sections - from "Scaffolding" to this notes - post having successfully generated your project.
2. The following sections refer to the dummy application and service generated into the `tests` and `src` folder by this template.
   Use the documentation and code as inspiration, adapt to your business logic, or remove and start documenting and coding from scratch.


## Overview

Adding template-demo to your project as a dependency is easy. See below for usage examples.

```shell
uv add template-demo             # add dependency to your project
```

If you don't have uv installed follow [these instructions](https://docs.astral.sh/uv/getting-started/installation/). If you still prefer pip over the modern and fast package manager [uv](https://github.com/astral-sh/uv), you can install the library like this:


```shell
pip install template-demo        # add dependency to your project
```

Executing the command line interface (CLI) in an isolated Python environment is just as easy:

```shell
uvx template-demo hello world               # prints "Hello, world! [..]"
uvx template-demo hello echo "Lorem Ipsum"  # echos "Lorem Ipsum"
uvx template-demo gui                       # opens the graphical user interface (GUI)
uvx --with "template-demo[examples]" template-demo gui  # opens the graphical user interface (GUI) with support for scientific computing
uvx template-demo system serve              # serves web API
uvx template-demo system serve --port=4711  # serves web API on port 4711
uvx template-demo system openapi            # serves web API on port 4711
```

Notes:
1. The API is versioned, mounted at `/api/v1` resp. `/api/v2`
2. While serving the web API go to [http://127.0.0.1:8000/api/v1/hello-world](http://127.0.0.1:8000/api/v1/hello-world) to see the respons of the `hello-world` operation.
3. Interactive documentation is provided at [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)


The CLI provides extensive help:

```shell
uvx template-demo --help                # all CLI commands
uvx template-demo hello world --help    # help for specific command
uvx template-demo hello echo --help
uvx template-demo gui --help
uvx template-demo system serve --help
uvx template-demo system openapi --help
```


## Operational Excellence

This project is designed with operational excellence in mind, using modern Python tooling and practices. It includes:

1. Various examples demonstrating usage:
  a. [Simple Python script](https://github.com/pavel-trunov/template-demo/blob/main/examples/script.py)
  b. [Streamlit web application](https://template-demo.streamlit.app/) deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  c. [Jupyter](https://github.com/pavel-trunov/template-demo/blob/main/examples/notebook.ipynb) and [Marimo](https://github.com/pavel-trunov/template-demo/blob/main/examples/notebook.py) notebook
2. Complete reference documentation [for the library](https://template-demo.readthedocs.io/en/latest/lib_reference.html), [for the CLI](https://template-demo.readthedocs.io/en/latest/cli_reference.html) and [for the API](https://template-demo.readthedocs.io/en/latest/api_reference_v1.html) on Read the Docs
3. [Transparent test coverage](https://app.codecov.io/gh/pavel-trunov/template-demo) including unit and E2E tests (reported on Codecov)
4. Matrix tested with [multiple python versions](https://github.com/pavel-trunov/template-demo/blob/main/noxfile.py) to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
5. Compliant with modern linting and formatting standards (powered by [Ruff](https://github.com/astral-sh/ruff))
6. Up-to-date dependencies (monitored by [Renovate](https://github.com/renovatebot/renovate) and [Dependabot](https://github.com/pavel-trunov/template-demo/security/dependabot))
7. [A-grade code quality](https://sonarcloud.io/summary/new_code?id=pavel-trunov_template-demo) in security, maintainability, and reliability with low technical debt and codesmell (verified by SonarQube)
8. Additional code security checks using [CodeQL](https://github.com/pavel-trunov/template-demo/security/code-scanning)
9. [Security Policy](SECURITY.md)
10. [License](LICENSE) compliant with the Open Source Initiative (OSI)
11. 1-liner for installation and execution of command line interface (CLI) via [uv(x)](https://github.com/astral-sh/uv) or [Docker](https://hub.docker.com/r/pavel-trunov/template-demo/tags)
12. Setup for developing inside a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included (supports VSCode and GitHub Codespaces)


## Usage Examples

The following examples run from source - clone this repository using
`git clone git@github.com:pavel-trunov/template-demo.git`.

### Minimal Python Script:

```python
"""Example script demonstrating the usage of the service provided by template-demo."""

from rich.console import Console

from template_demo.hello import Service

console = Console()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
```

[Show script code](https://github.com/pavel-trunov/template-demo/blob/main/examples/script.py) - [Read the reference documentation](https://template-demo.readthedocs.io/en/latest/lib_reference.html)


### Streamlit App

Serve the functionality provided by template-demo in the web by easily integrating the service into a Streamlit application.

[Try it out!](https://template-demo.streamlit.app) - [Show the code](https://github.com/pavel-trunov/template-demo/blob/main/examples/streamlit.py)

... or serve the app locally
```shell
uv sync --all-extras                                # Install streamlit dependency part of the examples extra, see pyproject.toml
uv run streamlit run examples/streamlit.py          # Serve on localhost:8501, opens browser
```


## Notebooks

### Jupyter

[Show the Jupyter code](https://github.com/pavel-trunov/template-demo/blob/main/examples/notebook.ipynb)

... or run within VSCode

```shell
uv sync --all-extras                                # Install dependencies required for examples such as Juypyter kernel, see pyproject.toml
```
Install the [Jupyter extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Click on `examples/notebook.ipynb` in VSCode and run it.

### Marimo

[Show the marimo code](https://github.com/pavel-trunov/template-demo/blob/main/examples/notebook.py)

Execute the notebook as a WASM based web app

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo run examples/notebook.py --watch      # Serve on localhost:2718, opens browser
```

or edit interactively in your browser

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo edit examples/notebook.py --watch     # Edit on localhost:2718, opens browser
```

... or edit interactively within VSCode

Install the [Marimo extension for VSCode](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)

Click on `examples/notebook.py` in VSCode and click on the caret next to the Run icon above the code (looks like a pencil) > "Start in marimo editor" (edit).

... or without prior cloning of the repository

```shell
uvx marimo run https://raw.githubusercontent.com/pavel-trunov/template-demo/refs/heads/main/examples/notebook.py
```

## Command Line Interface (CLI)

### Run with [uvx](https://docs.astral.sh/uv/guides/tools/)

Show available commands:

```shell
uvx template-demo --help
```

Execute commands:

```shell
uvx template-demo hello world
uvx template-demo hello echo --help
uvx template-demo hello echo "Lorem"
uvx template-demo hello echo "Lorem" --json
uvx template-demo gui
uvx --with "template-demo[examples]" template-demo gui  # opens the graphical user interface (GUI) with support for scientific computing
uvx template-demo system info
uvx template-demo system health
uvx template-demo system openapi
uvx template-demo system openapi --output-format=json
uvx template-demo system serve
```

See the [reference documentation of the CLI](https://template-demo.readthedocs.io/en/latest/cli_reference.html) for detailed documentation of all CLI commands and options.


### Environment

The service loads environment variables including support for .env files.

```shell
cp .env.example .env              # copy example file
echo "THE_VAR=MY_VALUE" > .env    # overwrite with your values
```

Now run the usage examples again.

### Run with Docker

You can as well run the CLI within Docker.

```shell
docker run pavel-trunov/template-demo --help
docker run pavel-trunov/template-demo hello world
docker run pavel-trunov/template-demo hello echo --help
docker run pavel-trunov/template-demo hello echo "Lorem"
docker run pavel-trunov/template-demo hello echo "Lorem" --json
docker run pavel-trunov/template-demo system info
docker run pavel-trunov/template-demo system health
docker run pavel-trunov/template-demo system openapi
docker run pavel-trunov/template-demo system openapi --output-format=json
docker run pavel-trunov/template-demo system serve
```

The default Docker image includes all extras. Additionally a slim image is provided, with no extras. Run as follows

```shell
docker run pavel-trunov/template-demo-slim --help
docker run pavel-trunov/template-demo-slim hello world
```

You can pass environment variables as parameters:

```shell
docker run --env TEMPLATE_DEMO_HELLO_LANGUAGE=de_DE pavel-trunov/template-demo hello world
docker run --env TEMPLATE_DEMO_HELLO_LANGUAGE=en_US pavel-trunov/template-demo hello world
```

A docker compose stack is provided. Clone this repository using
`git clone git@github.com:pavel-trunov/template-demo.git` and enter the repository folder.

The .env is passed through from the host to the Docker container.

```shell
docker compose run --remove-orphans template-demo --help
docker compose run --remove-orphans template-demo hello world
docker compose run --remove-orphans template-demo hello echo --help
docker compose run --remove-orphans template-demo hello echo "Lorem"
docker compose run --remove-orphans template-demo hello echo "Lorem" --json
docker compose run --remove-orphans template-demo system info
docker compose run --remove-orphans template-demo system health
docker compose run --remove-orphans template-demo system openapi
docker compose run --remove-orphans template-demo system openapi --output-format=json
echo "Running template-demo's API container as a daemon ..."
docker compose up -d
echo "Waiting for the API server to start ..."
sleep 5
echo "Checking health of v1 API ..."
curl http://127.0.0.1:8000/api/v1/healthz
echo ""
echo "Saying hello world with v1 API ..."
curl http://127.0.0.1:8000/api/v1/hello/world
echo ""
echo "Swagger docs of v1 API ..."
curl http://127.0.0.1:8000/api/v1/docs
echo ""
echo "Checking health of v2 API ..."
curl http://127.0.0.1:8000/api/v2/healthz
echo ""
echo "Saying hello world with v1 API ..."
curl http://127.0.0.1:8000/api/v2/hello/world
echo ""
echo "Swagger docs of v2 API ..."
curl http://127.0.0.1:8000/api/v2/docs
echo ""
echo "Shutting down the API container ..."
docker compose down
```

* See the [reference documentation of the API](https://template-demo.readthedocs.io/en/latest/api_reference_v1.html) for detailed documentation of all API operations and parameters.


## Extra: Lorem Ipsum

Dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam.


## Further Reading

* Inspect our [security policy](https://template-demo.readthedocs.io/en/latest/security.html) with detailed documentation of checks, tools and principles.
* Check out the [CLI reference](https://template-demo.readthedocs.io/en/latest/cli_reference.html) with detailed documentation of all CLI commands and options.
* Check out the [library reference](https://template-demo.readthedocs.io/en/latest/lib_reference.html) with detailed documentation of public classes and functions.
* Check out the [API reference](https://template-demo.readthedocs.io/en/latest/api_reference_v1.html) with detailed documentation of all API operations and parameters.
* Our [release notes](https://template-demo.readthedocs.io/en/latest/release-notes.html) provide a complete log of recent improvements and changes.
* In case you want to help us improve 🧠 template-demo: The [contribution guidelines](https://template-demo.readthedocs.io/en/latest/contributing.html) explain how to setup your development environment and create pull requests.
* We gratefully acknowledge the [open source projects](https://template-demo.readthedocs.io/en/latest/attributions.html) that this project builds upon. Thank you to all these wonderful contributors!

## Star History

<a href="https://star-history.com/#pavel-trunov/template-demo">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=pavel-trunov/template-demo&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=pavel-trunov/template-demo&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=pavel-trunov/template-demo&type=Date" />
 </picture>
</a>
