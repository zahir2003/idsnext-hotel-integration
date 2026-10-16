from app.adapters.mock_idsnext import MockIDSNextAdapter


class SyncService:

    def __init__(self):
        self.pms = MockIDSNextAdapter()
        self.external_system = {}

    def sync_reservations(self):
        reservations = self.pms.get_data("reservations")

        created = 0
        updated = 0

        for reservation in reservations:
            reservation_id = reservation["id"]

            if reservation_id in self.external_system:
                updated += 1
            else:
                created += 1

            self.external_system[reservation_id] = reservation.copy()

        return {
            "status": "success",
            "mode": "simulation",
            "destination": "mock_external_system",
            "created": created,
            "updated": updated,
            "total": len(reservations),
            "reservations": list(self.external_system.values()),
        }


sync_service = SyncService()
