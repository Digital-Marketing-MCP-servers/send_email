# mcp_email_tool.py
import os
import smtplib
from email.mime.text import MIMEText
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# Create MCP server
mcp = FastMCP("Email Tool")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")


@mcp.tool()
def send_email(subject: str, body: str, to_email: str) -> dict:
    """
    Send an email using SMTP.
    
    Args:
        subject: Email subject line
        body: Email body content
        to_email: Recipient email address
    
    Returns:
        Dictionary with status and message
    """
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server: # Use SMTP server from environment variables
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, [to_email], msg.as_string())
        return {"status": "success", "message": "Email sent!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
   
   
if __name__=="__main__": 
         mcp.run(transport="streamable-http",
                    host="127.0.0.1",
                    port=8004)
