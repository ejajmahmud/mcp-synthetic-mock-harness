"""Core Synthetic Mock Harness."""
from typing import Dict, List, Any, Optional, Callable

class MockResponse:
    def __init__(self, data: Any, should_fail: bool = False):
        self.data = data
        self.should_fail = should_fail

class SyntheticMockHarness:
    def __init__(self):
        self.mocks: Dict[str, Callable[[Dict[str, Any]], MockResponse]] = {}
        self.calls: List[Dict[str, Any]] = []

    def register_mock(self, tool_name: str, responder: Callable[[Dict[str, Any]], MockResponse]):
        self.mocks[tool_name] = responder

    def invoke(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        self.calls.append({"tool": tool_name, "args": arguments})
        if tool_name not in self.mocks:
            raise KeyError(f"No mock registered for tool: {tool_name}")
        resp = self.mocks[tool_name](arguments)
        if resp.should_fail:
            raise RuntimeError(f"Mock failure simulated for {tool_name}: {resp.data}")
        return resp.data

    def assert_called(self, tool_name: str, times: Optional[int] = None):
        matched = [c for c in self.calls if c["tool"] == tool_name]
        if times is not None and len(matched) != times:
            raise AssertionError(f"Expected {times} calls to {tool_name}, got {len(matched)}")
        elif times is None and len(matched) == 0:
            raise AssertionError(f"Expected at least one call to {tool_name}, got none")
