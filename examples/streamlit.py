"""
Streamlit web application that demonstrates a simple interface for template-demo.

This module creates a web interface using Streamlit to demonstrate the usage of the service provided by
template-demo.
"""

import streamlit as st

from template_demo.hello import Service
from template_demo.utils import __version__

sidebar = st.sidebar
sidebar.write(
    f" [template-demo v{__version__}](https://template-demo.readthedocs.io/en/latest/)",
)
sidebar.write("Built with love in Berlin 🐻")

st.title("🧠 template-demo ")

# Initialize the service
service = Service()

# Get the message
message = service.get_hello_world()

# Print the message
st.write(f"{message}")
