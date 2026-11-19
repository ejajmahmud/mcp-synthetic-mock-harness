"""CLI for Mock Harness."""
import argparse
from .core import SyntheticMockHarness, MockResponse

def main():
    parser = argparse.ArgumentParser(description="MCP Synthetic Mock Harness CLI")
    parser.add_argument("--demo", action="store_true", help="Run mock harness demo")
    args = parser.parse_args()

    harness = SyntheticMockHarness()
    harness.register_mock("calculator", lambda args: MockResponse(args.get("a", 0) + args.get("b", 0)))
    result = harness.invoke("calculator", {"a": 10, "b": 32})
    print(f"Mock result: {result}")
    harness.assert_called("calculator", times=1)
    print("Assertion verified successfully!")

if __name__ == "__main__":
    main()
