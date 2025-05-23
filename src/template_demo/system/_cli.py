"""System CLI commands."""

import json
import os
from enum import StrEnum
from importlib.util import find_spec
from typing import Annotated

import typer
import uvicorn
import yaml

from ..constants import API_VERSIONS  # noqa: TID252
from ..utils import __project_name__, console, get_logger  # noqa: TID252
from ._service import Service

logger = get_logger(__name__)

cli = typer.Typer(name="system", help="Determine health, info and further utillities.")

_service = Service()


class OutputFormat(StrEnum):
    """
    Enum representing the supported output formats.

    This enum defines the possible formats for output data:
    - YAML: Output data in YAML format
    - JSON: Output data in JSON format

    Usage:
        format = OutputFormat.YAML
        print(f"Using {format} format")
    """

    YAML = "yaml"
    JSON = "json"


@cli.command()
def health(
    output_format: Annotated[
        OutputFormat, typer.Option(help="Output format", case_sensitive=False)
    ] = OutputFormat.JSON,
) -> None:
    """Determine and print system health.

    Args:
        output_format (OutputFormat): Output format (JSON or YAML).
    """
    match output_format:
        case OutputFormat.JSON:
            console.print_json(data=_service.health().model_dump())
        case OutputFormat.YAML:
            console.print(
                yaml.dump(data=json.loads(_service.health().model_dump_json()), width=80, default_flow_style=False),
                end="",
            )


@cli.command()
def info(
    include_environ: Annotated[bool, typer.Option(help="Include environment variables")] = False,
    filter_secrets: Annotated[bool, typer.Option(help="Filter secrets")] = True,
    output_format: Annotated[
        OutputFormat, typer.Option(help="Output format", case_sensitive=False)
    ] = OutputFormat.JSON,
) -> None:
    """Determine and print system info.

    Args:
        include_environ (bool): Include environment variables.
        filter_secrets (bool): Filter secrets from the output.
        output_format (OutputFormat): Output format (JSON or YAML).
    """
    info = _service.info(include_environ=include_environ, filter_secrets=filter_secrets)
    match output_format:
        case OutputFormat.JSON:
            console.print_json(data=info)
        case OutputFormat.YAML:
            console.print(yaml.dump(info, width=80, default_flow_style=False), end="")


if find_spec("nicegui"):
    from ..utils import gui_run  # noqa: TID252

    @cli.command()
    def serve(  # noqa: PLR0913, PLR0917 # type: ignore
        app: Annotated[bool, typer.Option(help="Enable web application")] = True,
        api: Annotated[bool, typer.Option(help="Enable webservice API")] = True,
        host: Annotated[str, typer.Option(help="Host to bind the server to")] = "127.0.0.1",
        port: Annotated[int, typer.Option(help="Port to bind the server to")] = 8000,
        watch: Annotated[bool, typer.Option(help="Enable auto-reload on changes of source code")] = True,
        open_browser: Annotated[bool, typer.Option(help="Open app in browser after starting the server")] = False,
    ) -> None:
        """Start the web server, hosting the graphical web application and/or webservice API.

        Args:
            app (bool): Enable web application.
            api (bool): Enable webservice API.
            host (str): Host to bind the server to.
            port (int): Port to bind the server to.
            watch (bool): Enable auto-reload on changes of source code.
            open_browser (bool): Open app in browser after starting the server.
        """
        if api and not app:
            console.print(f"Starting webservice API server at http://{host}:{port}")
            # using environ to pass host/port to api.py to generate doc link
            os.environ["UVICORN_HOST"] = host
            os.environ["UVICORN_PORT"] = str(port)
            uvicorn.run(
                f"{__project_name__}.api:api",
                host=host,
                port=port,
                reload=watch,
            )
        elif app:
            console.print(f"Starting web application server at http://{host}:{port}")
            gui_run(native=False, host=host, port=port, with_api=api, show=open_browser)

else:

    @cli.command()
    def serve(  # type: ignore
        host: Annotated[str, typer.Option(help="Host to bind the server to")] = "127.0.0.1",
        port: Annotated[int, typer.Option(help="Port to bind the server to")] = 8000,
        watch: Annotated[bool, typer.Option(help="Enable auto-reload on changes of source code")] = True,
    ) -> None:
        """Start the web server, hosting the API.

        Args:
            api (bool): Enable webservice API.
            host (str): Host to bind the server to.
            port (int): Port to bind the server to.
            watch (bool): Enable auto-reload on changes of source code.
        """
        console.print(f"Starting webservice API server at http://{host}:{port}")
        # using environ to pass host/port to api.py to generate doc link
        os.environ["UVICORN_HOST"] = host
        os.environ["UVICORN_PORT"] = str(port)
        uvicorn.run(
            f"{__project_name__}.api:api",
            host=host,
            port=port,
            reload=watch,
        )


@cli.command()
def openapi(
    api_version: Annotated[
        str, typer.Option(help=f"API Version. Available: {', '.join(API_VERSIONS.keys())}", case_sensitive=False)
    ] = next(iter(API_VERSIONS.keys())),
    output_format: Annotated[
        OutputFormat, typer.Option(help="Output format", case_sensitive=False)
    ] = OutputFormat.JSON,
) -> None:
    """Dump the OpenAPI specification.

    Args:
        api_version (str): API version to dump.
        output_format (OutputFormat): Output format (JSON or YAML).

    Raises:
        typer.Exit: If an invalid API version is provided.
    """
    from ..api import api_instances  # noqa: PLC0415, TID252

    if api_version not in API_VERSIONS:
        available_versions = ", ".join(API_VERSIONS.keys())
        console.print(
            f"[bold red]Error:[/] Invalid API version '{api_version}'. Available versions: {available_versions}"
        )
        raise typer.Exit(code=1)

    schema = api_instances[api_version].openapi()

    match output_format:
        case OutputFormat.JSON:
            console.print_json(data=schema)
        case OutputFormat.YAML:
            console.print(yaml.dump(schema, width=80, default_flow_style=False), end="")


@cli.command()
def fail() -> None:
    """Fail by dividing by zero.

    - Used to validate error handling and instrumentation.
    """
    Service.div_by_zero()


@cli.command()
def sleep(
    seconds: Annotated[int, typer.Option(help="Duration in seconds")] = 2,
) -> None:
    """Sleep given for given number of seconds.

    Args:
        seconds (int): Number of seconds to sleep.

    - Used to validate performance profiling.
    """
    Service.sleep(seconds)
