# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "template-demo==0.0.1",
# ]
# ///


import marimo
from template_demo.utils import __version__

__generated_with = "0.13.0"
app = marimo.App(app_title=f"🧠 template-demo v{__version__}", width="full")


@app.cell
def _():
    import marimo as mo
    from template_demo.hello import Service

    service = Service()
    message = service.get_hello_world()

    with mo.redirect_stdout():
        print(message)
    return


if __name__ == "__main__":
    app.run()
