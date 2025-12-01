
"""
Base abstractions for agents in the multi-agent system.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class Agent(ABC):
    """
    Abstract base class for all agents.

    Each agent implements a `run` method that receives an input
    payload and returns a structured output payload.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable agent name."""
        raise NotImplementedError

    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """Execute the agent's core logic."""
        raise NotImplementedError

    def to_dict(self) -> Dict[str, Any]:
        """Minimal metadata for logging / observability."""
        return {"name": self.name, "type": self.__class__.__name__}
