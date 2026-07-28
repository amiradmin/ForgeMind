# Maintenance Domain

## Overview

The Maintenance domain provides functionality for managing preventive and corrective maintenance activities for assets within ForgeMind.

The domain is responsible for:

* Defining recurring maintenance plans for assets.
* Recording maintenance requests.
* Managing work orders generated from maintenance activities.
* Associating maintenance activities with assets.
* Tracking maintenance types, priorities, statuses, schedules, and completion information.
* Providing authenticated REST APIs for maintenance operations.
* Supporting filtering, searching, ordering, and pagination.
* Providing automated tests for models, business logic, and REST APIs.

The Maintenance domain is implemented as a Django application under:

```text
apps/maintenance/
```

---

## Domain Structure

The Maintenance application is organised into the following main components:

```text
apps/maintenance/
├── api/
│   └── v1/
│       ├── permissions.py
│       ├── serializers/
│       │   ├── maintenance_plan.py
│       │   ├── maintenance_request.py
│       │   └── work_order.py
│       ├── urls.py
│       └── views/
│           ├── maintenance_plan.py
│           ├── maintenance_request.py
│           └── work_order.py
│
├── models/
│   ├── enums.py
│   ├── maintenance_plan.py
│   ├── maintenance_request.py
│   └── work_order.py
│
├── services/
│   └── maintenance_plan_service.py
│
└── tests/
    ├── conftest.py
    ├── factories.py
    ├── test_api.py
    ├── test_maintenance_plan_service.py
    └── test_models.py
```

The domain follows a layered architecture:

```text
HTTP Request
     │
     ▼
API View
     │
     ▼
Serializer
     │
     ▼
Service Layer
     │
     ▼
Domain Model
     │
     ▼
Database
```

For operations that require business logic, the service layer is responsible for encapsulating domain-specific behaviour.

---

# Domain Models

The Maintenance domain currently contains three primary models:

1. `MaintenancePlan`
2. `MaintenanceRequest`
3. `WorkOrder`

---

## MaintenancePlan

A `MaintenancePlan` defines a recurring maintenance schedule for an asset.

It is primarily used for preventive maintenance activities.

A maintenance plan contains information such as:

* The asset being maintained.
* Plan name.
* Description.
* Maintenance type.
* Maintenance frequency.
* Frequency unit.
* Start date.
* Next due date.

Conceptually:

```text
Asset
  │
  └── MaintenancePlan
          │
          ├── Name
          ├── Description
          ├── Maintenance Type
          ├── Frequency
          ├── Frequency Unit
          ├── Start Date
          └── Next Due Date
```

### Maintenance Type

Maintenance plans can distinguish between different maintenance types, including preventive maintenance.

Example:

```text
Maintenance Type: preventive
Frequency: 1
Frequency Unit: months
Start Date: 2026-07-01
```

The resulting plan represents a recurring monthly maintenance activity.

### Next Due Date

The `next_due_date` field represents the next scheduled date on which the maintenance activity is due.

The calculation of the next due date is handled by the Maintenance Plan business logic.

---

## MaintenanceRequest

A `MaintenanceRequest` represents a request for maintenance work associated with an asset.

A request can contain information such as:

* Asset.
* Title.
* Description.
* Maintenance type.
* Priority.
* Status.
* Requesting user.

Example:

```text
Asset:
    Main Cooling Pump

Title:
    Pump Failure

Description:
    Main pump is not working

Maintenance Type:
    corrective

Priority:
    high
```

A maintenance request represents the initial identification or reporting of a maintenance requirement.

---

## WorkOrder

A `WorkOrder` represents an actionable maintenance task.

A work order can be associated with:

* An asset.
* An optional maintenance request.
* A title.
* A description.
* A maintenance type.
* A priority.
* A status.
* An assigned user.
* Scheduled start and end times.
* Actual start and completion timestamps.
* Completion notes.

Conceptually:

```text
Asset
  │
  ├── MaintenancePlan
  │
  └── MaintenanceRequest
          │
          ▼
      WorkOrder
          │
          ├── Assigned To
          ├── Scheduled Start
          ├── Scheduled End
          ├── Started At
          ├── Completed At
          └── Completion Notes
```

A work order can optionally be linked to a maintenance request.

---

# Maintenance Workflow

The Maintenance domain supports the following conceptual workflow:

```text
Maintenance Plan
       │
       │ Preventive maintenance becomes due
       ▼
Maintenance Request
       │
       │ Maintenance work is approved
       ▼
Work Order
       │
       ▼
Work Execution
       │
       ▼
Completion
```

For corrective maintenance, the workflow can begin directly with a maintenance request:

```text
Asset Issue
    │
    ▼
Maintenance Request
    │
    ▼
Work Order
    │
    ▼
Maintenance Work
    │
    ▼
Completed
```

The exact transition rules are enforced by the domain implementation and should not be assumed to imply automatic creation of a work order unless that behaviour is explicitly implemented.

---

# Business Logic

## MaintenancePlanService

The Maintenance domain currently provides a dedicated service layer for Maintenance Plans.

The service is implemented in:

```text
apps/maintenance/services/maintenance_plan_service.py
```

The service encapsulates business logic related to maintenance plan operations.

The service is responsible for keeping domain-specific operations separate from HTTP/API concerns.

The general architecture is:

```text
API View
    │
    ▼
MaintenancePlanService
    │
    ├── Validate business rules
    ├── Create/update domain object
    ├── Calculate scheduling information
    └── Persist changes
```

The service layer should be used when an operation involves domain behaviour rather than simple CRUD operations.

---

# REST API

The Maintenance REST API is implemented under:

```text
apps/maintenance/api/v1/
```

The API is divided into three resources.

---

## Maintenance Plans

Collection endpoint:

```text
/api/v1/maintenance-plans/
```

Supported operations include:

```text
GET     /api/v1/maintenance-plans/
POST    /api/v1/maintenance-plans/
```

Individual resource operations are exposed through the corresponding detail endpoint:

```text
/api/v1/maintenance-plans/{id}/
```

The API supports standard resource operations according to the configured view implementation.

### Example Create Request

```json
{
    "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
    "name": "Monthly Pump Maintenance",
    "description": "Monthly preventive maintenance",
    "maintenance_type": "preventive",
    "frequency": 1,
    "frequency_unit": "months",
    "start_date": "2026-07-01"
}
```

---

## Maintenance Requests

Collection endpoint:

```text
/api/v1/maintenance-requests/
```

Example create request:

```json
{
    "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
    "title": "Pump Failure",
    "description": "Main pump is not working",
    "maintenance_type": "corrective",
    "priority": "high"
}
```

The authenticated user creating the request is associated with the request as the requesting user when supported by the API implementation.

---

## Work Orders

Collection endpoint:

```text
/api/v1/work-orders/
```

Example create request:

```json
{
    "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
    "title": "Repair Main Pump",
    "description": "Repair the main cooling pump",
    "maintenance_type": "corrective",
    "priority": "high",
    "status": "open",
    "scheduled_start": "2026-07-20T08:00:00Z",
    "scheduled_end": "2026-07-20T12:00:00Z",
    "completion_notes": ""
}
```

A work order may optionally reference a maintenance request and may be assigned to a user.

---

# Filtering

The Maintenance API supports resource-specific filtering.

## Maintenance Plans

Maintenance plans can be filtered by asset:

```text
GET /api/v1/maintenance-plans/?asset={asset_id}
```

Example:

```text
/api/v1/maintenance-plans/?asset=7d9f4c8e-2f7a-4c9b-9a8a-123456789abc
```

---

## Maintenance Requests

Maintenance requests can be filtered by status:

```text
GET /api/v1/maintenance-requests/?status=open
```

---

## Work Orders

Work orders can be filtered by status:

```text
GET /api/v1/work-orders/?status=open
```

---

# Search

The Maintenance API supports search functionality.

Search is performed using the `search` query parameter.

### Maintenance Plans

```text
GET /api/v1/maintenance-plans/?search=cooling
```

The search can identify maintenance plans using searchable fields configured by the API view.

### Maintenance Requests

```text
GET /api/v1/maintenance-requests/?search=cooling
```

### Work Orders

```text
GET /api/v1/work-orders/?search=cooling
```

The exact searchable fields are defined in the corresponding API view configuration.

---

# Ordering

The Maintenance API supports ordering using the `ordering` query parameter.

### Maintenance Plans

```text
GET /api/v1/maintenance-plans/?ordering=name
```

### Maintenance Requests

```text
GET /api/v1/maintenance-requests/?ordering=title
```

### Work Orders

```text
GET /api/v1/work-orders/?ordering=title
```

Descending ordering can be requested using the `-` prefix where supported:

```text
?ordering=-created_at
```

---

# Pagination

Maintenance collection endpoints use the project's configured Django REST Framework pagination.

For example:

```text
GET /api/v1/maintenance-plans/?page=2
```

A paginated response contains:

```json
{
    "count": 25,
    "next": "...",
    "previous": "...",
    "results": []
}
```

The actual page size is determined by the global REST framework configuration.

---

# Authentication and Permissions

Maintenance API endpoints require authentication.

Unauthenticated requests to protected endpoints are expected to return:

```text
401 Unauthorized
```

The Maintenance API permission configuration is located at:

```text
apps/maintenance/api/v1/permissions.py
```

Authentication and authorization rules should be applied consistently with the rest of the ForgeMind API.

---

# Serialization

The Maintenance API uses dedicated serializers for each domain resource:

```text
apps/maintenance/api/v1/serializers/
├── maintenance_plan.py
├── maintenance_request.py
└── work_order.py
```

Serializers are responsible for:

* Validating incoming API data.
* Converting request data into domain model instances.
* Serializing model instances into API responses.
* Defining read-only fields.
* Validating related resources.
* Providing OpenAPI examples and API documentation.

The Work Order serializer, for example, exposes relationships such as:

* `asset`
* `maintenance_request`
* `assigned_to`

and scheduling fields such as:

* `scheduled_start`
* `scheduled_end`
* `started_at`
* `completed_at`

---

# Automated Testing

The Maintenance domain includes automated tests under:

```text
apps/maintenance/tests/
```

The test suite currently contains:

```text
tests/
├── conftest.py
├── factories.py
├── test_api.py
├── test_maintenance_plan_service.py
└── test_models.py
```

## Model Tests

Model behaviour is tested in:

```text
test_models.py
```

These tests verify domain model behaviour and model-level constraints.

---

## Service Tests

Maintenance Plan business logic is tested in:

```text
test_maintenance_plan_service.py
```

These tests verify service-layer behaviour independently from the HTTP API.

---

## API Tests

REST API behaviour is tested in:

```text
test_api.py
```

The API test suite covers functionality including:

* Authentication requirements.
* Listing resources.
* Creating resources.
* Filtering.
* Searching.
* Ordering.
* Pagination.

Example authentication test:

```python
response = client.get(
    "/api/v1/maintenance-plans/",
)

assert response.status_code == 401
```

Example filtering test:

```python
response = authenticated_client.get(
    f"/api/v1/maintenance-plans/?asset={asset.id}",
)

assert response.status_code == 200
assert response.data["count"] == 1
```

The tests use factories defined in:

```text
apps/maintenance/tests/factories.py
```

and related Asset factories from the Assets domain.

---

# Testing Strategy

The Maintenance domain follows a layered testing strategy:

```text
                 ┌──────────────────┐
                 │   API Tests      │
                 │ Authentication   │
                 │ CRUD             │
                 │ Filtering        │
                 │ Search           │
                 │ Ordering         │
                 │ Pagination       │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │ Service Tests    │
                 │ Business Logic   │
                 │ Domain Rules     │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │  Model Tests     │
                 │ Constraints      │
                 │ Model Behaviour  │
                 └──────────────────┘
```

This approach allows domain logic to be tested independently from HTTP/API behaviour while also validating the complete API integration.

---

# API Query Examples

### List maintenance plans

```text
GET /api/v1/maintenance-plans/
```

### Filter plans by asset

```text
GET /api/v1/maintenance-plans/?asset={asset_id}
```

### Search maintenance plans

```text
GET /api/v1/maintenance-plans/?search=cooling
```

### Order maintenance plans

```text
GET /api/v1/maintenance-plans/?ordering=name
```

### List open maintenance requests

```text
GET /api/v1/maintenance-requests/?status=open
```

### Search maintenance requests

```text
GET /api/v1/maintenance-requests/?search=cooling
```

### List open work orders

```text
GET /api/v1/work-orders/?status=open
```

### Search work orders

```text
GET /api/v1/work-orders/?search=cooling
```

---

# Implementation Status

The Maintenance domain currently provides:

* [x] Maintenance Plan model
* [x] Maintenance Request model
* [x] Work Order model
* [x] Maintenance Plan business service
* [x] Maintenance Plan REST API
* [x] Maintenance Request REST API
* [x] Work Order REST API
* [x] API serializers
* [x] API permissions
* [x] Model tests
* [x] Maintenance Plan service tests
* [x] REST API tests
* [x] API filtering
* [x] API search
* [x] API ordering
* [x] API pagination
* [x] Authentication tests

The Maintenance domain is designed to provide a foundation for future maintenance automation, scheduling, work order management, and predictive maintenance capabilities within ForgeMind.
