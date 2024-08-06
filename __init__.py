from .reader import SeaboardReaderNode
from .wordweighter import WordWeighterNode
from .composer import PromptComposerNode

NODE_CLASS_MAPPINGS = {
    "enki.seaboard.reader" : SeaboardReaderNode,
    "enki.prompt.wordweighter" : WordWeighterNode,
    "enki.prompt.composer" : PromptComposerNode,
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "enki.seaboard.reader": "Seaboard Reader",
    "enki.prompt.wordweighter": "Word Weighter",
    "enki.prompt.composer": "Prompt Composer",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
