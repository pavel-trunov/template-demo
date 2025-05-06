"""Example script demonstrating the usage of the service provided by template-demo."""

from rich.console import Console

from template_demo.hello import Service

console = Console()

service = Service()

message = service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
