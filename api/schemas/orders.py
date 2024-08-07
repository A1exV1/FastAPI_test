import datetime as dt

from pydantic import BaseModel, model_validator, AwareDatetime
from typing_extensions import Self


class CreateOrder(BaseModel):
    flat: int
    dog_name: str
    dog_breed: str
    walk_at: AwareDatetime

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'flat': 42,
                    'dog_name': 'Sharik',
                    'dog_breed': 'Stafford',
                    'walk_at': dt.datetime(2020, 1, 1, 12, 0, 0, tzinfo=dt.UTC),
                }
            ]
        }
    }

    @model_validator(mode='after')
    def validate_time(self) -> Self:
        if self.walk_at < dt.datetime.now(tz=dt.UTC):
            raise ValueError('Date and time must be in the future')

        if not 7 <= self.walk_at.hour <= 23:
            raise ValueError('Time must be between 7 and 23 hours')

        if self.walk_at.minute not in [0, 30]:
            raise ValueError('Time must equals 30 minutes or 0 minutes')
        self.walk_at = self.walk_at.replace(second=0, microsecond=0)
        return self


class Order(BaseModel):
    id: int
    dog_walker_id: int
    dog_id: int
    walk_at: dt.datetime
