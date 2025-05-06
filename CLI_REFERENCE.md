# CLI Reference

Command Line Interface of template-demo

**Usage**:

```console
$ template-demo [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

🧠 template-demo v0.0.1 - built with love in Berlin 🐻

**Commands**:

* `gui`: Open graphical user interface (GUI).
* `notebook`: Run notebook server.
* `hello`: Hello commands
* `system`: Determine health, info and further...

## `template-demo gui`

Open graphical user interface (GUI).

**Usage**:

```console
$ template-demo gui [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `template-demo notebook`

Run notebook server.

**Usage**:

```console
$ template-demo notebook [OPTIONS]
```

**Options**:

* `--host TEXT`: Host to bind the server to  [default: 127.0.0.1]
* `--port INTEGER`: Port to bind the server to  [default: 8001]
* `--help`: Show this message and exit.

## `template-demo hello`

Hello commands

**Usage**:

```console
$ template-demo hello [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `echo`: Echo the text.
* `world`: Print hello world message and what&#x27;s in...

### `template-demo hello echo`

Echo the text.

Args:
    text (str): The text to echo.
    json (bool): Print as JSON.

**Usage**:

```console
$ template-demo hello echo [OPTIONS] [TEXT]
```

**Arguments**:

* `[TEXT]`: The text to echo  [default: Lorem ipsum dolor sit amet, consectetur adipiscing elit.]

**Options**:

* `--json / --no-json`: Print as JSON  [default: no-json]
* `--help`: Show this message and exit.

### `template-demo hello world`

Print hello world message and what&#x27;s in the environment variable THE_VAR.

**Usage**:

```console
$ template-demo hello world [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `template-demo system`

Determine health, info and further utillities.

**Usage**:

```console
$ template-demo system [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `health`: Determine and print system health.
* `info`: Determine and print system info.
* `serve`: Start the web server, hosting the...
* `openapi`: Dump the OpenAPI specification.
* `fail`: Fail by dividing by zero.
* `sleep`: Sleep given for given number of seconds.

### `template-demo system health`

Determine and print system health.

Args:
    output_format (OutputFormat): Output format (JSON or YAML).

**Usage**:

```console
$ template-demo system health [OPTIONS]
```

**Options**:

* `--output-format [yaml|json]`: Output format  [default: json]
* `--help`: Show this message and exit.

### `template-demo system info`

Determine and print system info.

Args:
    include_environ (bool): Include environment variables.
    filter_secrets (bool): Filter secrets from the output.
    output_format (OutputFormat): Output format (JSON or YAML).

**Usage**:

```console
$ template-demo system info [OPTIONS]
```

**Options**:

* `--include-environ / --no-include-environ`: Include environment variables  [default: no-include-environ]
* `--filter-secrets / --no-filter-secrets`: Filter secrets  [default: filter-secrets]
* `--output-format [yaml|json]`: Output format  [default: json]
* `--help`: Show this message and exit.

### `template-demo system serve`

Start the web server, hosting the graphical web application and/or webservice API.

Args:
    app (bool): Enable web application.
    api (bool): Enable webservice API.
    host (str): Host to bind the server to.
    port (int): Port to bind the server to.
    watch (bool): Enable auto-reload on changes of source code.
    open_browser (bool): Open app in browser after starting the server.

**Usage**:

```console
$ template-demo system serve [OPTIONS]
```

**Options**:

* `--app / --no-app`: Enable web application  [default: app]
* `--api / --no-api`: Enable webservice API  [default: api]
* `--host TEXT`: Host to bind the server to  [default: 127.0.0.1]
* `--port INTEGER`: Port to bind the server to  [default: 8000]
* `--watch / --no-watch`: Enable auto-reload on changes of source code  [default: watch]
* `--open-browser / --no-open-browser`: Open app in browser after starting the server  [default: no-open-browser]
* `--help`: Show this message and exit.

### `template-demo system openapi`

Dump the OpenAPI specification.

Args:
    api_version (str): API version to dump.
    output_format (OutputFormat): Output format (JSON or YAML).

Raises:
    typer.Exit: If an invalid API version is provided.

**Usage**:

```console
$ template-demo system openapi [OPTIONS]
```

**Options**:

* `--api-version TEXT`: API Version. Available: v1, v2  [default: v1]
* `--output-format [yaml|json]`: Output format  [default: json]
* `--help`: Show this message and exit.

### `template-demo system fail`

Fail by dividing by zero.

- Used to validate error handling and instrumentation.

**Usage**:

```console
$ template-demo system fail [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `template-demo system sleep`

Sleep given for given number of seconds.

Args:
    seconds (int): Number of seconds to sleep.

- Used to validate performance profiling.

**Usage**:

```console
$ template-demo system sleep [OPTIONS]
```

**Options**:

* `--seconds INTEGER`: Duration in seconds  [default: 2]
* `--help`: Show this message and exit.
