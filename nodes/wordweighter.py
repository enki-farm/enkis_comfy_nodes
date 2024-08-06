class WordWeighterNode:
    def __init__(self):
        self.weighted_word = None

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "chan": ("INT", {
                    "forceInput": True
                }),
                "value": ("FLOAT", {
                    "forceInput": True
                }),
                "listen_chan": ("INT", {
                    "default": 0,
                    "display": "number",
                }),
                "weight_word": ("STRING", {}),
            }
        }


    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weighted_word",)
    CATEGORY = "enki"
    FUNCTION = "main"

    def main(self, chan, value, listen_chan, weight_word):
        # init safe value
        if self.weighted_word is None:
            self.weighted_word = f"({weight_word}:1.0)"

        if chan == listen_chan:
            weighted_word = f"({weight_word}:{value})"
            self.weighted_word = weighted_word

        return (self.weighted_word,)