def mb_to_bytes(size_mb: int) -> int:
    return size_mb * 1024 * 1024


def bytes_to_mb(size_bytes: int) -> float:
    return size_bytes / (1024 * 1024)