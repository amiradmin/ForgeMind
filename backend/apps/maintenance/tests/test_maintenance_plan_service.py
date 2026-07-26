from datetime import date

import pytest

from apps.assets.tests.factories import AssetFactory
from apps.maintenance.models import (
    MaintenanceFrequencyUnit,
    MaintenanceType,
)
from apps.maintenance.services.maintenance_plan_service import (
    MaintenancePlanService,
)


class TestMaintenancePlanService:
    def test_calculate_next_due_date_in_days(self):
        result = MaintenancePlanService.calculate_next_due_date(
            start_date=date(2026, 7, 1),
            frequency=10,
            frequency_unit=MaintenanceFrequencyUnit.DAYS,
        )

        assert result == date(2026, 7, 11)

    def test_calculate_next_due_date_in_weeks(self):
        result = MaintenancePlanService.calculate_next_due_date(
            start_date=date(2026, 7, 1),
            frequency=2,
            frequency_unit=MaintenanceFrequencyUnit.WEEKS,
        )

        assert result == date(2026, 7, 15)

    def test_calculate_next_due_date_in_months(self):
        result = MaintenancePlanService.calculate_next_due_date(
            start_date=date(2026, 7, 1),
            frequency=3,
            frequency_unit=MaintenanceFrequencyUnit.MONTHS,
        )

        assert result == date(2026, 10, 1)

    def test_calculate_next_due_date_in_years(self):
        result = MaintenancePlanService.calculate_next_due_date(
            start_date=date(2026, 7, 1),
            frequency=1,
            frequency_unit=MaintenanceFrequencyUnit.YEARS,
        )

        assert result == date(2027, 7, 1)

    def test_calculate_next_due_date_handles_end_of_month(self):
        result = MaintenancePlanService.calculate_next_due_date(
            start_date=date(2026, 1, 31),
            frequency=1,
            frequency_unit=MaintenanceFrequencyUnit.MONTHS,
        )

        assert result == date(2026, 2, 28)

    def test_zero_frequency_is_rejected(self):
        with pytest.raises(ValueError, match="greater than zero"):
            MaintenancePlanService.calculate_next_due_date(
                start_date=date(2026, 7, 1),
                frequency=0,
                frequency_unit=MaintenanceFrequencyUnit.DAYS,
            )

    def test_negative_frequency_is_rejected(self):
        with pytest.raises(ValueError, match="greater than zero"):
            MaintenancePlanService.calculate_next_due_date(
                start_date=date(2026, 7, 1),
                frequency=-1,
                frequency_unit=MaintenanceFrequencyUnit.DAYS,
            )

    def test_unsupported_frequency_unit_is_rejected(self):
        with pytest.raises(ValueError, match="Unsupported"):
            MaintenancePlanService.calculate_next_due_date(
                start_date=date(2026, 7, 1),
                frequency=1,
                frequency_unit="invalid",
            )

    @pytest.mark.django_db
    def test_create_plan_sets_next_due_date(self):
        asset = AssetFactory()

        plan = MaintenancePlanService.create_plan(
            asset=asset,
            name="Monthly Pump Inspection",
            maintenance_type=MaintenanceType.PREVENTIVE,
            frequency=1,
            frequency_unit=MaintenanceFrequencyUnit.MONTHS,
            start_date=date(2026, 7, 1),
            description="Monthly inspection of the pump.",
        )

        assert plan.asset == asset
        assert plan.name == "Monthly Pump Inspection"
        assert plan.maintenance_type == MaintenanceType.PREVENTIVE
        assert plan.frequency == 1
        assert plan.frequency_unit == MaintenanceFrequencyUnit.MONTHS
        assert plan.start_date == date(2026, 7, 1)
        assert plan.next_due_date == date(2026, 8, 1)
