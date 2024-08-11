from src.Flight import Flight


class FlightService:

    @classmethod
    def add(cls, flight: Flight) -> None:
        print(f"Adding flight: {flight}")

    @classmethod
    def get(cls) -> list[Flight]:
        print("Getting flights")
        return []
