from app.cafe import NotWearingMaskError, NotVaccinatedError
from app.errors import OutdatedVaccineError


def go_to_cafe(friends: list, cafe: type) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass
    masks_to_buy = sum(
        1
        for friend in friends
        if not friend.get("wearing_a_mask"))
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
