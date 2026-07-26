# backend/apps/maintenance/services/maintenance_plan_service.py

import calendar
from datetime import date, timedelta

from apps.maintenance.models import (
    MaintenanceFrequencyUnit,
    MaintenancePlan,
)


class MaintenancePlanService:
    """
    Business logic for maintenance plans.
    """

    @staticmethod
    def calculate_next_due_date(
        *,
        start_date: date,
        frequency: int,
        frequency_unit: str,
    ) -> date:
        """
        Calculate the next maintenance due date based on
        the start date, frequency, and frequency unit.
        """

        if frequency <= 0:
            raise ValueError("Frequency must be greater than zero.")

        if frequency_unit == MaintenanceFrequencyUnit.DAYS:
            return start_date + timedelta(days=frequency)

        if frequency_unit == MaintenanceFrequencyUnit.WEEKS:
            return start_date + timedelta(weeks=frequency)

        if frequency_unit == MaintenanceFrequencyUnit.MONTHS:
            return MaintenancePlanService._add_months(
                start_date,
                frequency,
            )

        if frequency_unit == MaintenanceFrequencyUnit.YEARS:
            return MaintenancePlanService._add_months(
                start_date,
                frequency * 12,
            )

        raise ValueError(f"Unsupported maintenance frequency unit: {frequency_unit}")

    @staticmethod
    def _add_months(
        start_date: date,
        months: int,
    ) -> date:
        """
        Add a number of months to a date while handling
        different month lengths safely.
        """

        month_index = start_date.month - 1 + months

        year = start_date.year + month_index // 12
        month = month_index % 12 + 1

        last_day = calendar.monthrange(year, month)[1]

        day = min(
            start_date.day,
            last_day,
        )

        return date(
            year=year,
            month=month,
            day=day,
        )

    @classmethod
    def create_plan(
        cls,
        *,
        asset,
        name: str,
        maintenance_type: str,
        frequency: int,
        frequency_unit: str,
        start_date: date,
        description: str = "",
    ) -> MaintenancePlan:
        """
        Create a maintenance plan with its initial next due date.
        """

        next_due_date = cls.calculate_next_due_date(
            start_date=start_date,
            frequency=frequency,
            frequency_unit=frequency_unit,
        )

        return MaintenancePlan.objects.create(
            asset=asset,
            name=name,
            description=description,
            maintenance_type=maintenance_type,
            frequency=frequency,
            frequency_unit=frequency_unit,
            start_date=start_date,
            next_due_date=next_due_date,
        )
