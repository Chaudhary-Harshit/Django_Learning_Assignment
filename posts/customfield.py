from django import models

class PositiveIntegerField(models.field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def get_prep_value(self, value):
        if value is not None and value < 0:
            raise ValueError("Value must be a positive integer.")
        return int(value) if value is not None else value


