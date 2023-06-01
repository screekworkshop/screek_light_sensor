import esphome.codegen as cg

KEY_ESP32 = "esp32"
KEY_BOARD = "board"
KEY_VARIANT = "variant"
KEY_SDKCONFIG_OPTIONS = "sdkconfig_options"
KEY_COMPONENTS = "components"
KEY_REPO = "repo"
KEY_REF = "ref"
KEY_REFRESH = "refresh"
KEY_PATH = "path"

VARIANT_ESP32 = "ESP32"
VARIANT_ESP32S2 = "ESP32S2"
VARIANT_ESP32S3 = "ESP32S3"
VARIANT_ESP32C3 = "ESP32C3"
VARIANT_ESP32H2 = "ESP32H2"
VARIANTS = [
    VARIANT_ESP32,
    VARIANT_ESP32S2,
    VARIANT_ESP32S3,
    VARIANT_ESP32C3,
    VARIANT_ESP32H2,
]

VARIANT_FRIENDLY = {
    VARIANT_ESP32: "ESP32",
    VARIANT_ESP32S2: "ESP32-S2",
    VARIANT_ESP32S3: "ESP32-S3",
    VARIANT_ESP32C3: "ESP32-C3",
    VARIANT_ESP32H2: "ESP32-H2",
}

esp32_ns = cg.esphome_ns.namespace("esp32")