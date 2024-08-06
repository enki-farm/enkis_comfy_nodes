class SeaboardReaderNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "type": (["timbre", "pressure", "pitchBend"], {}),
                "chan": ("INT", {
                    "default": 0,
                    "display": "number",
                }),
                "value": ("FLOAT", {
                    "min": 0.0,
                    "max": 2.0,
                    "default": 1.0,
                    "step": 0.01,
                    "display": "slider",
                })
        }
    }

    RETURN_TYPES = ("INT", "FLOAT",)
    RETURN_NAMES = ("chan", "value",)
    CATEGORY = "enki"
    FUNCTION = "main"

    def main(self, type, chan, value):
        print(f"Reading {type} from channel {chan} with value {value}")
        return (chan, value)
