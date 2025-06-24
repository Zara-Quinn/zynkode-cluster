"""
Add cost tracking per job and team

Part of zynkode-cluster - Multi-node GPU cluster management and job scheduling.
"""

from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class Cli:
    """Implementation for: Add cost tracking per job and team"""

    def __init__(self, config: dict = None):
        self.config = config or {}
        logger.info(f"Initialized Cli")

    def run(self, **kwargs) -> Any:
        """Execute the primary operation."""
        raise NotImplementedError
