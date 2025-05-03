# Gemini Tools and SDK Examples with Model Context Protocol (MCP)

This repository provides examples demonstrating the integration of Gemini models with custom tools, specifically highlighting their interaction within a **Model Context Protocol (MCP)** environment. It also showcases different methods for exposing and consuming these functionalities.

**Understanding Model Context Protocol (MCP):**

In this context, the Model Context Protocol (MCP) likely defines a standardized way for language models (like Gemini) to interact with external tools. This protocol might specify:

- How tools are described and discovered by the model.
- The format for invoking tools, including necessary parameters.
- The structure of the responses expected from tools.
- Mechanisms for managing the context and state during tool interactions.

These examples aim to illustrate how to build and utilize tools that seamlessly integrate with an MCP-based system.

## Examples

This repository contains the following examples:

### 1. FastAPI Server Exposing Tools for MCP

This example demonstrates how to expose your FastAPI endpoints as **Model Context Protocol (MCP)** tools, with Auth. This allows Gemini models, operating within an MCP framework, to discover and utilize these custom functionalities.

- **File:** `fast_api_mcp_demo.py`
- **References:**
    - [Fast-API MCP](https://github.com/tadata-org/fastapi_mcp)

### 2. Gemini Model Consuming MCP Tools

This example showcases how a Gemini model, operating within an **MCP** environment, can consume the tools exposed by an MCP-compliant server. This demonstrates the complete cycle of a Gemini model discovering, invoking, and utilizing external tools through the defined protocol.

- **File:** `gemini_mcp_demo.py`
- **Key Features:**
    - Demonstrates the process of an MCP-enabled Gemini model discovering available tools.
    - Provides code snippets showing how to format tool invocation requests according to the MCP specification.
    - Likely includes examples of processing the structured responses from the executed MCP tools and integrating them into the model's reasoning.
- **References:**
    - [Using MCP with Gemini](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#use_model_context_protocol_mcp)

### 3. SDK Server with Server-Sent Events (SSE) for MCP Interaction

This example illustrates creating a server using an SDK and exposing functionalities via Server-Sent Events (SSE) in the context of **MCP**. While SSE is a transport mechanism, this example likely shows how it can be used to facilitate communication or stream information relevant to the MCP workflow.

- **File:** `mcp_server_demo.py`
- **Key Features:**
    - Shows the server-side implementation using the specified SDK, focusing on its role within an MCP architecture.
    - Illustrates how to configure and send events using SSE that might be relevant to the MCP interaction lifecycle.
    - May include examples of how an MCP agent or the Gemini model itself could consume this SSE stream for real-time updates or information related to tool execution.

### Prerequisites

Before running the examples, ensure you have the following installed:

- Python >= 3.10
- Pip (Python package installer)
- Any specific libraries required by each example (listed in their respective requirements files or documentation).
- Access to the Gemini models and the necessary infrastructure to interact within an **MCP** environment. This might involve specific SDKs or API endpoints related to your MCP implementation.
- (For the FastAPI example) A running MCP server or the necessary components to simulate its behavior and interaction with the exposed tools.

## Contributing

Contributions are welcome! If you find bugs or have suggestions for improving the application, please open an issue or submit a pull request.

Made with ❤ by  [jggomez](https://devhack.co).

[![Twitter Badge](https://img.shields.io/badge/-@jggomezt-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/jggomezt)](https://twitter.com/jggomezt)
[![Linkedin Badge](https://img.shields.io/badge/-jggomezt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/jggomezt/)](https://www.linkedin.com/in/jggomezt/)
[![Medium Badge](https://img.shields.io/badge/-@jggomezt-03a57a?style=flat-square&labelColor=000000&logo=Medium&link=https://medium.com/@jggomezt)](https://medium.com/@jggomezt)

## License

    Copyright 2025 Juan Guillermo Gómez

