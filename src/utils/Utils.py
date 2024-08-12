import uuid


class Utils:

    @classmethod
    def generate_uuid(cls) -> str:
        return uuid.uuid4().hex
