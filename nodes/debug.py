from time import sleep

class SleeperNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "time_to_sleep": ("INT", {
                    "default": 1,
                    "display": "number",
                })
            },
            "optional": {
                "value": ("*", {})
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)
    CATEGORY = "enki"
    FUNCTION = "main"

    def main(self, time_to_sleep, **kwargs):
        sleep(time_to_sleep)

        if "value" in kwargs:
            value = kwargs["value"]
        return (value,)
