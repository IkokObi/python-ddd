from typing import Callable, ContextManager, List

from display.domain.entity.room import Room
from display.infra.repository import RoomRDBRepository
from shared_kernel.domain.value_object import RoomStatus
from sqlalchemy.orm import Session


class DisplayQueryUseCase:
    def __init__(
        self,
        room_repo: RoomRDBRepository,
        db_session: Callable[[], ContextManager[Session]],
    ):
        self.room_repo = room_repo
        self.db_session = db_session

    def get_room(self, room_status: RoomStatus) -> List[Room]:
        room_status: RoomStatus = RoomStatus.from_value(room_status)

        with self.db_session() as session:
            rooms: List[Room] = list(
                self.room_repo.get_rooms_by_status(
                    session=session, room_status=room_status
                )
            )

        return rooms
