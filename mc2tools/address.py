import socket


def get_ip_address(domain: str) -> str:
    """Get IP Address From Domain

    Args:
        domain (str): Domain to get IP Address

    Returns:
        Str: IP Address
    """
    try:
        return str(socket.gethostbyname(domain))
    except socket.gaierror as e:
        raise e
