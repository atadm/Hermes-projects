# Agent Data Access

Architecture proposals for securely connecting AI agents to company data for customer success automation.

## Contents

| File | Description |
|---|---|
| `design.md` | Summary of the 3 architectural approaches |
| `architecture.html` | Interactive dark-mode diagrams (open in browser) |
| `architecture.png` | Preview render of the diagrams |

## Quick Summary

- **Option A (Recommended):** Warehouse + Real-Time Permission Cache
- **Option B:** Warehouse + Source API Fallback
- **Option C:** Source APIs Only (maximum security)

## Core Security Principle

Never give the agent direct database or API access — every data access goes through a permission-checking gateway. See `design.md` for full detail.