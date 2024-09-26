from typing import List

from returns.maybe import Maybe
from sqlalchemy.orm import joinedload

from config.base import session_factory
from model import Target

def find_all_targets() -> Maybe[List[Target]]:
    with session_factory() as session:
        targets = session.query(Target).options(
            joinedload(Target.city),
            joinedload(Target.industry),
            joinedload(Target.type)
        ).all()
        return Maybe.from_optional(targets)


def find_by_id(target_id) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Target)
            .options(
                joinedload(Target.city),
                joinedload(Target.industry),
                joinedload(Target.type)
            )
            .filter(Target.id == target_id)
            .first()
        )