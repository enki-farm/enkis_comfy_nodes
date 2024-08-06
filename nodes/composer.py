class PromptComposerNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "base_prompt": ("STRING", {
                    "multiline": True,
                    "default": "Write a story about a dragon."
                }),
            },
            "optional": {
                "weighted_word_1": ("STRING", {
                    "forceInput": True,
                }),
                "weighted_word_2": ("STRING", {
                    "forceInput": True,
                }),
                "weighted_word_3": ("STRING", {
                    "forceInput": True,
                }),
                "weighted_word_4": ("STRING", {
                    "forceInput": True,
                }),
                "weighted_word_5": ("STRING", {
                    "forceInput": True,
                }),
                "weighted_word_6": ("STRING", {
                    "forceInput": True,
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("enhanced_prompt",)
    CATEGORY = "enki"
    FUNCTION = "main"

    def main(self, base_prompt, **kwargs):
        enhanced_prompt = base_prompt
        for k in kwargs:
            word = kwargs[k].split(":")[0][1:]
            enhanced_prompt = enhanced_prompt.replace(word, kwargs[k])

        print(f"Enhanced prompt: {enhanced_prompt}")
        return (enhanced_prompt,)
