"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    quantity = int(value.strip())
    if quantity <= 0:
        raise ValueError(f"Quantity must be a positive integer, got {quantity}")
    return quantity
