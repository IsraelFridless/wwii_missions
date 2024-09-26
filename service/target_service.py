from typing import List, Dict, Any

from model import Target
from repository import target_repository


def find_all_targets() -> List[Target]:
    return (target_repository.find_all_targets()
    .map(lambda li: [target_to_dict(t) for t in li])
    .value_or([]))

def target_to_dict(target: Target) -> Dict[str, Any]:
    return {
        "id": target.id,
        "target_priority": target.priority if target.priority else 0,
        "target_latitude": str(target.latitude),
        "target_longitude": str(target.longitude),
        "target_city": {
            "id": target.city.id,
            "city_name": target.city.city_name,
            "country": target.city.country.country_name
        },
        "target_industry": {
            "id": target.industry.id,
            "industry_name": target.industry.industry_name
        },
        "target_type": {
            "id": target.type.id,
            "type_name": target.type.target_type_name
        }
    }

