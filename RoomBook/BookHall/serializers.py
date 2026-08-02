from rest_framework import serializers
from datetime import datetime

from .models import RoomBook


class RoomBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomBook
        fields = "__all__"

    def validate(self, data):
        booking_date = data["booking_date"]
        start_time = data["start_time"]
        end_time = data["end_time"]

        # Convert time to datetime to calculate duration
        start = datetime.combine(booking_date, start_time)
        end = datetime.combine(booking_date, end_time)

        # End time must be greater than start time
        if end <= start:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        # Calculate duration in minutes
        duration = (end - start).total_seconds() / 60

        # Minimum 15 minutes
        if duration < 15:
            raise serializers.ValidationError(
                "Booking must be at least 15 minutes."
            )

        # Maximum 4 hours = 240 minutes
        if duration > 240:
            raise serializers.ValidationError(
                "Booking cannot exceed 4 hours."
            )

        # Must use 5-minute slots
        if start_time.minute % 5 != 0 or end_time.minute % 5 != 0:
            raise serializers.ValidationError(
                "Booking time must be in 5-minute slots."
            )

        # Check for overlapping booking
        conflict = RoomBook.objects.filter(
            booking_date=booking_date,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).first()

        if conflict:
            raise serializers.ValidationError(
                f"Slot unavailable, conflicts with existing booking "
                f"{conflict.start_time.strftime('%H:%M')}-"
                f"{conflict.end_time.strftime('%H:%M')}"
            )

        return data

