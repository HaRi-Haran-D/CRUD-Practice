from django.db import models

# Create your models here.


class RoomBook(models.Model):
    room_no = models.CharField(default="Room 1", max_length=10)
    booking_date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return f"Room booked on {self.booking_date} from {self.start_time} to {self.end_time}"

