from constants import ___

from collections.abc import Callable


def create_user(user_name: str, user_age: int, after_created: Callable[[int], None]) -> None:
    pass


def send_test_email(user_id: int) -> None:
    pass


if __name__ == "__main__":
    assert create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) is None
