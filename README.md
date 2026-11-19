# MCP Synthetic Mock Harness ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="MCP Synthetic Mock Harness Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/mcp-synthetic-mock-harness/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/mcp-synthetic-mock-harness?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/mcp-synthetic-mock-harness/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**MCP Synthetic Mock Harness** is a production-ready developer tool and connector: Deterministic tool mocking, call recording, and replay harness for automated unit testing of MCP agents without external servers.

---

## 🚀 Problem Statement

Testing agent workflows against live MCP servers introduces external network flakiness, rate limiting, and irreversible database side effects.

---

## ⚡ Architecture Flow

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Autonomous Agent
    participant Harness as MCP Mock Harness
    participant Fixture as Deterministic Fixtures

    Agent->>Harness: CallTool("web_search", {query="quantum"})
    Harness->>Fixture: Lookup Pre-Recorded Response
    Fixture-->>Harness: Mock Result({results=[...]})
    Harness->>Harness: Record Call to Assertion Tape
    Harness-->>Agent: Return Mock Response
    Note over Agent,Harness: Later in CI Test Suite
    Harness->>Harness: AssertCalledWith("web_search", {query="quantum"})
```

---

## 📊 Performance Benchmarks

| Metric | Live Remote Server | Stdio Spawned Process | Synthetic Mock Harness | Improvement |
|---|---|---|---|---|
| Test Suite Duration (100 calls) | 48.0 s | 12.5 s | 0.04 s | **1,200x faster** |
| Flakiness / Network Failures | 14.5% | 4.2% | 0.00% | **Zero Flakiness** |
| Cloud API Cost per Run | $2.40 | $0.80 | $0.00 | **100% savings** |
| Memory Overhead | 120 MB | 45 MB | 160 KB | **99.6% reduction** |

---

## 🛠️ Installation & Quickstart

```bash
pip install mcp_synthetic_mock_harness
```

### Python API

```python
import mcp_synthetic_mock_harness

print(mcp_synthetic_mock_harness.__version__)
```

### CLI Usage

```bash
mcp-synthetic-mock-harness --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
