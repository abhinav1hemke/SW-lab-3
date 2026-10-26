"""Basic email-address and password validators for Practical 5."""


def is_valid_email(email: str) -> bool:
    """Check a basic email format with a nonempty, dotted domain.

    This educational check does not attempt to implement the full email
    address standard.
    """
    if not email or any(character.isspace() for character in email):
        return False
    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")
    if not local_part or not domain:
        return False

    domain_labels = domain.split(".")
    return (
        len(domain_labels) >= 2
        and all(domain_labels)
        and all(
            not label.startswith("-") and not label.endswith("-")
            for label in domain_labels
        )
    )


def is_valid_password(password: str) -> bool:
    """Require eight characters, an uppercase, a lowercase, and a digit."""
    return (
        len(password) >= 8
        and any(character.isupper() for character in password)
        and any(character.islower() for character in password)
        and any(character.isdigit() for character in password)
    )
