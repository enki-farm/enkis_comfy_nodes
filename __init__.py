from .nodes.reader import SeaboardReaderNode
from .nodes.wordweighter import WordWeighterNode
from .nodes.composer import PromptComposerNode
from .nodes.debug import SleeperNode

NODE_CLASS_MAPPINGS = {
    "enki.seaboard.reader" : SeaboardReaderNode,
    "enki.prompt.wordweighter" : WordWeighterNode,
    "enki.prompt.composer" : PromptComposerNode,
    "enki.debug.sleeper" : SleeperNode,
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "enki.seaboard.reader": "Seaboard Reader",
    "enki.prompt.wordweighter": "Word Weighter",
    "enki.prompt.composer": "Prompt Composer",
    "enki.debug.sleeper": "Sleeper",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
