import re

# Find the periods that don't have an escape char in front
# Otherwise, the column name gets replaced repeatedly
vega_replacement_pattern = r'(?<!\\)\.'

def sanitize_column_name(name):
    """
    When vega-lite sees a period ".", it assumes it's looking at data with nested properties.

    Since lux doesn't process "object"/"dict" columns, this assumption is unhelpful when trying to render the recommended graphs

    To treat "." as a regular character and not a call for nested property access, we escape it with a backslash.

    https://vega.github.io/vega-lite/docs/field.html
    """
    return re.sub(vega_replacement_pattern, "\\.", name)
