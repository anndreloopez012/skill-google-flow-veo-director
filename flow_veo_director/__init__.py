"""
Google Flow & Veo Cinematic Director Package.
"""

__version__ = "1.0.0"
__author__ = "ALCORE Technologies & Andre Lopez"

from flow_veo_director.builder import VeoShotBlueprint
from flow_veo_director.continuity import FlowSequence, FlowShot
from flow_veo_director.timing import evaluate_segment_timing, count_words
from flow_veo_director.validator import ScriptValidator

__all__ = [
    "VeoShotBlueprint",
    "FlowSequence",
    "FlowShot",
    "evaluate_segment_timing",
    "count_words",
    "ScriptValidator",
]
