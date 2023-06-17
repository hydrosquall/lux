import re

# Find the periods that don't have an escape char in front
# Otherwise, the column name gets replaced repeatedly
vega_replacement_pattern = r'(?<!\\)\.'

def sanitize_column_name(name):
    """
    When vega-lite sees a period ".", it assumes it's looking at a nested object
    Since lux doesn't process "object"/"dict" columns, this assumption is unhelpful to us

    To treat "." as a regular character and not a call for nested property access, we escape it.
    """
    return re.sub(vega_replacement_pattern, "\\.", name)
