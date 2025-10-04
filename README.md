# Email Tool (MCP Server)

This is a simple service to send emails via SMTP, wrapped as an MCP tool using **FastMCP**.

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration / Environment Variables](#configuration--environment-variables)  
- [Usage](#usage)  
  - [Running the server](#running-the-server)  
  - [Calling the tool (RPC / HTTP)]  
- [API / Tool Definition](#api--tool-definition)  
- [Error Handling](#error-handling)  
- [Security Considerations](#security-considerations)  
- [License](#license)  

---

## Features

- Sends plain-text emails over SMTP  
- Wrapped as an **MCP tool** using `FastMCP`  
- Configurable via environment variables  
- Minimal dependencies  

---

## Prerequisites

- Python 3.7+  
- Access to an SMTP server (e.g. Gmail SMTP, SendGrid, etc.)  
- Basic familiarity with MCP / FastMCP  
- `pip` (or `poetry` / `pipenv`) for dependency management  

---

## Installation

1. Clone the repository (or place `server.py` in your project folder):

    ```bash
    git clone <repo-url>
    cd <repo-folder>
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install fastmcp python-dotenv
    ```

4. Create a `.env` file in the same directory as `server.py` with the required SMTP settings (see next section).

---

## Configuration / Environment Variables

The server expects the following environment variables to be defined (e.g. via a `.env` file):

```dotenv
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_username@example.com
SMTP_PASS=your_smtp_password
