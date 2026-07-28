# Industrial Event and Telemetry Domain

## 1. Overview

The Industrial Event and Telemetry Domain extends ForgeMind's existing Asset Management and Maintenance capabilities with operational data collection and intelligence.

The purpose of this domain is to capture and manage two primary categories of operational information:

* **Industrial Events** — discrete occurrences associated with an industrial asset.
* **Telemetry** — time-based measurements representing the operational state or behaviour of an asset.

Together, these data sources provide the operational context required to understand asset behaviour, calculate asset health, identify abnormal conditions, and eventually support predictive maintenance and AI-powered decision-making.

The domain is designed to integrate with the existing:

* Organization domain
* Plant domain
* Area domain
* Asset domain
* Maintenance domain
* Audit domain
* Background task infrastructure

The target architectural flow is:

```text
Organization
    │
    └── Plant
          │
          └── Area
                │
                └── Asset
                     │
          ┌──────────┴──────────┐
          │                     │
    Industrial Events       Telemetry
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
              Asset Health
                     │
                     ▼
          Predictive Maintenance
                     │
                     ▼
               AI Pipeline
```

This domain establishes the data foundation for future capabilities including:

* Asset health scoring
* Anomaly detection
* Predictive maintenance
* Failure prediction
* Intelligent maintenance recommendations
* AI-assisted operational decision support

---

## 2. Goals

The primary goals of the Industrial Event and Telemetry Domain are:

* Capture operational events associated with industrial assets.
* Store telemetry measurements associated with assets.
* Provide a consistent data model for operational information.
* Connect operational data with the existing Asset domain.
* Integrate operational events with Maintenance.
* Support asset health calculations.
* Enable future predictive maintenance capabilities.
* Provide a foundation for AI and machine learning workflows.
* Maintain strong authentication and RBAC controls.
* Support auditability and traceability.
* Provide APIs suitable for operational applications and future integrations.
* Design the system for future high-volume telemetry requirements.

---

## 3. Non-Goals

The initial implementation does not attempt to provide:

* A complete industrial IoT platform.
* Direct PLC or SCADA integration.
* Real-time streaming infrastructure.
* A dedicated time-series database.
* Machine learning models.
* Predictive maintenance algorithms.
* Advanced anomaly detection.
* Edge computing infrastructure.
* Real-time dashboards.

These capabilities may be introduced in future phases.

The initial implementation focuses on creating a clean and extensible domain model and API foundation.

---

# 4. Domain Context

ForgeMind already provides an enterprise asset hierarchy:

```text
Organization
    │
    └── Plant
          │
          └── Area
                │
                └── Asset
```

The Industrial Event and Telemetry Domain extends this hierarchy by attaching operational information to assets.

An asset may have:

* Multiple operational events
* Multiple telemetry measurements
* Multiple maintenance requests
* Multiple work orders
* Multiple lifecycle events
* Multiple audit records

The asset becomes the central entity connecting operational, maintenance, and historical information.

The resulting conceptual model is:

```text
                    Asset
                      │
       ┌──────────────┼───────────────┐
       │              │               │
       ▼              ▼               ▼
   Maintenance      Events        Telemetry
       │              │               │
       ▼              ▼               │
   Work Orders    Event History       │
       │                              │
       └──────────────┬───────────────┘
                      │
                      ▼
                 Asset Health
                      │
                      ▼
             Predictive Maintenance
                      │
                      ▼
                  AI/ML
```

---

# 5. Industrial Event Domain

## 5.1 Definition

An Industrial Event represents a discrete occurrence associated with an industrial asset.

Examples include:

* Equipment failure
* Equipment warning
* Alarm
* Emergency stop
* Overheating
* Excessive vibration
* Pressure threshold exceeded
* Power loss
* Unexpected shutdown
* Startup
* Maintenance required
* Inspection required
* Operational state change

Events represent occurrences rather than continuous measurements.

For example:

```text
Telemetry:
Temperature = 95°C

Event:
Temperature threshold exceeded
```

Telemetry describes the measured state.

The event describes the operational significance of that state.

---

## 5.2 Event Categories

The initial event model should support categorisation.

Suggested categories include:

* `operational`
* `alarm`
* `failure`
* `warning`
* `safety`
* `maintenance`
* `lifecycle`
* `system`

The category should be extensible so that additional event types can be introduced without requiring major architectural changes.

---

## 5.3 Event Severity

Events should support a severity level.

Suggested values:

* `info`
* `low`
* `medium`
* `high`
* `critical`

Severity is important for:

* Asset health calculations
* Operational dashboards
* Maintenance prioritisation
* Notifications
* AI analysis

Example:

```text
Event:
Main Cooling Pump Overheating

Category:
warning

Severity:
high
```

---

## 5.4 Event Status

Events may have a lifecycle status.

Suggested values:

* `active`
* `acknowledged`
* `resolved`
* `cancelled`

This allows ForgeMind to distinguish between an event that is currently active and one that has already been resolved.

Example:

```text
Active Alarm
      │
      ▼
Acknowledged
      │
      ▼
Resolved
```

Not every event necessarily requires a status lifecycle. Informational events may remain immutable historical records.

---

## 5.5 Event Data

An Industrial Event should conceptually contain:

* Unique identifier
* Asset
* Event type
* Category
* Severity
* Status
* Title
* Description
* Occurred timestamp
* Resolved timestamp
* Source
* External reference
* Metadata
* Created timestamp
* Updated timestamp

The exact implementation may evolve during model implementation.

---

## 5.6 Event Source

Events may originate from multiple sources.

Examples:

* Manual user entry
* Asset management system
* Maintenance system
* IoT device
* PLC
* SCADA
* External API
* Automated rule
* AI system

The source should be represented in a provider-neutral manner.

Example:

```text
source = "manual"
source = "scada"
source = "iot"
source = "external_api"
source = "automated_rule"
source = "ai"
```

The design should avoid tightly coupling the domain to a specific industrial integration technology.

---

# 6. Telemetry Domain

## 6.1 Definition

Telemetry represents a measurement or observation of an asset's operational state at a specific point in time.

Examples include:

* Temperature
* Pressure
* Vibration
* Flow rate
* Voltage
* Current
* Power consumption
* RPM
* Humidity
* Oil level

Telemetry is inherently time-based.

A telemetry record should answer:

> What was measured, for which asset, at what time, and what was the value?

---

## 6.2 Telemetry Measurement

A telemetry measurement conceptually contains:

* Unique identifier
* Asset
* Metric name
* Metric key
* Value
* Unit
* Timestamp
* Source
* Quality indicator
* Metadata
* Created timestamp

Example:

```text
Asset:
Main Cooling Pump

Metric:
Temperature

Value:
87.5

Unit:
°C

Timestamp:
2026-07-28T10:30:00Z
```

---

## 6.3 Metric Definition

Telemetry metrics should be identified consistently.

A metric should have a stable machine-readable key.

Examples:

```text
temperature
pressure
vibration
flow_rate
power_consumption
motor_speed
```

The metric key should be suitable for programmatic processing.

A human-readable metric name may also be supported.

Example:

```text
key: temperature
name: Motor Temperature
unit: °C
```

---

## 6.4 Measurement Units

Telemetry measurements should include their unit.

Examples:

* `°C`
* `°F`
* `bar`
* `psi`
* `mm/s`
* `rpm`
* `kW`
* `V`
* `A`
* `%`

The initial implementation may store units as strings.

A future dedicated unit system may be introduced if ForgeMind requires unit conversion or standardisation.

---

## 6.5 Telemetry Value Types

The initial implementation should primarily support numeric measurements.

Examples:

```text
temperature = 87.5
pressure = 5.2
vibration = 3.7
rpm = 1450
```

Future versions may support:

* Boolean values
* String values
* Enumerated states

However, numeric telemetry should remain the primary use case for health scoring and predictive maintenance.

---

## 6.6 Telemetry Quality

Telemetry data may be incomplete or unreliable.

Possible quality states include:

* `good`
* `uncertain`
* `bad`
* `missing`

Quality information is important because AI and health scoring systems should not treat unreliable telemetry as trustworthy.

Example:

```text
Temperature:
87.5°C

Quality:
good
```

---

# 7. Entity Relationships

The primary relationship is:

```text
Asset 1 ──────── * IndustrialEvent

Asset 1 ──────── * TelemetryMeasurement
```

Maintenance relationships are:

```text
Asset 1 ──────── * MaintenancePlan

Asset 1 ──────── * MaintenanceRequest

Asset 1 ──────── * WorkOrder
```

The combined operational model becomes:

```text
Asset
 │
 ├── Industrial Events
 │
 ├── Telemetry Measurements
 │
 ├── Maintenance Plans
 │
 ├── Maintenance Requests
 │
 └── Work Orders
```

This structure allows ForgeMind to correlate operational behaviour with maintenance activity.

---

# 8. Asset Integration

The Asset domain is the central integration point.

Every Industrial Event and Telemetry Measurement should reference an existing Asset.

The relationship should use the existing Asset UUID strategy.

Example:

```text
Asset UUID
    │
    ├── Event 1
    ├── Event 2
    ├── Event 3
    │
    ├── Telemetry 1
    ├── Telemetry 2
    └── Telemetry 3
```

The asset relationship should enforce referential integrity.

Events and telemetry should not exist without a valid asset association unless a future ingestion architecture explicitly supports temporary or unassigned data.

---

# 9. Maintenance Integration

Industrial Events should integrate with the Maintenance domain.

For example:

```text
Telemetry:
Vibration = 12 mm/s
        │
        ▼
Rule detects abnormal vibration
        │
        ▼
Industrial Event:
High Vibration Detected
        │
        ▼
Maintenance Request
        │
        ▼
Work Order
        │
        ▼
Repair Completed
        │
        ▼
Event Resolved
```

This creates a complete operational lifecycle.

The initial implementation does not require automatic creation of maintenance requests from events.

However, the domain should be designed so that this workflow can be introduced later.

---

# 10. Asset Operational Timeline

ForgeMind should eventually provide a unified operational timeline for an asset.

The timeline may combine:

* Asset lifecycle events
* Industrial events
* Telemetry-derived events
* Maintenance requests
* Work orders
* Maintenance plans
* Audit events

Example:

```text
2026-07-20 08:00
Maintenance started

2026-07-20 09:15
High vibration detected

2026-07-20 09:20
Maintenance request created

2026-07-20 09:30
Work order created

2026-07-20 11:30
Repair completed

2026-07-20 12:00
Event resolved
```

The operational timeline should be implemented as a read-oriented integration layer rather than duplicating all source records.

---

# 11. Data Flow

The expected data flow is:

```text
Industrial Asset
       │
       ├───────────────┐
       │               │
       ▼               ▼
Operational Event   Telemetry
       │               │
       └───────┬───────┘
               │
               ▼
        Operational Data
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
 Asset Health      Maintenance
       │                │
       └───────┬────────┘
               │
               ▼
       Predictive Layer
               │
               ▼
          AI Pipeline
```

The system should support both manually created and machine-generated data.

---

# 12. Database Design Considerations

The initial implementation should use PostgreSQL, consistent with the existing ForgeMind architecture.

The core tables are expected to be conceptually similar to:

```text
maintenance_industrial_event
maintenance_telemetry_measurement
```

The final table names should follow the project's existing naming conventions.

Recommended indexes include:

### Industrial Events

* Asset ID
* Occurred timestamp
* Event category
* Severity
* Status
* Composite `(asset_id, occurred_at)`

### Telemetry

* Asset ID
* Metric key
* Timestamp
* Composite `(asset_id, metric_key, timestamp)`

Time-based queries are expected to be common.

Example:

```text
Get temperature measurements
for Asset X
between 2026-07-01 and 2026-07-28
```

Therefore, timestamp-related indexes are important.

---

# 13. API Design Considerations

Future REST APIs should follow the existing ForgeMind API versioning strategy.

Suggested endpoints:

```text
/api/v1/industrial-events/
/api/v1/telemetry/
```

Asset-specific queries may be supported using filters:

```text
/api/v1/industrial-events/?asset=<asset_uuid>
```

```text
/api/v1/telemetry/?asset=<asset_uuid>
```

Telemetry filtering should support:

* Asset
* Metric
* Time range
* Source
* Quality

Example:

```text
/api/v1/telemetry/
    ?asset=<uuid>
    &metric=temperature
    &start=2026-07-01
    &end=2026-07-28
```

Industrial Event filtering should support:

* Asset
* Category
* Severity
* Status
* Source
* Time range

APIs should support:

* Authentication
* RBAC
* Pagination
* Filtering
* Ordering
* Search where appropriate

---

# 14. Telemetry Storage and Scalability

Telemetry data can grow significantly faster than traditional business data.

For example:

```text
1 Asset
× 10 Metrics
× 1 Reading / Minute
× 24 Hours
× 365 Days
```

This produces millions of records over time.

Therefore, telemetry storage must be designed with scalability in mind.

The initial ForgeMind implementation will use PostgreSQL.

However, the domain should avoid coupling business logic directly to PostgreSQL-specific telemetry behaviour.

The application should conceptually interact with telemetry through a domain/service abstraction where appropriate.

---

# 15. Future Time-Series Database Strategy

A dedicated time-series database may be introduced when telemetry volume and query requirements justify it.

Potential future technologies include:

* TimescaleDB
* InfluxDB
* Other specialised time-series storage

The recommended evolution is:

```text
Phase 1
PostgreSQL
    │
    ▼
Moderate Telemetry Volume

Phase 2
PostgreSQL + Time-Series Optimisation
    │
    ▼
Growing Telemetry Volume

Phase 3
Dedicated Time-Series Storage
    │
    ▼
High-Frequency Industrial Telemetry
```

The migration decision should be based on:

* Data volume
* Query performance
* Retention requirements
* Ingestion rate
* Infrastructure complexity
* Operational cost

No dedicated time-series database is required for the initial implementation.

---

# 16. Integration with Asset Health

Industrial Events and Telemetry will become inputs to Asset Health calculations.

Conceptually:

```text
Telemetry
    │
    ├── Temperature
    ├── Pressure
    ├── Vibration
    └── Power
          │
          ▼
     Health Signals
          │
          ├─────────────┐
          │             │
          ▼             ▼
     Event History   Maintenance
          │             │
          └──────┬──────┘
                 ▼
          Asset Health Score
```

Potential health factors include:

* Recent critical events
* Frequency of failures
* Abnormal telemetry
* Maintenance frequency
* Open maintenance requests
* Overdue maintenance plans
* Work order history

The health scoring system should remain independent from the raw event and telemetry storage models.

---

# 17. Integration with Predictive Maintenance

The Industrial Event and Telemetry Domain provides the raw data foundation required for predictive maintenance.

Potential predictive maintenance workflow:

```text
Historical Telemetry
        │
Historical Events
        │
Maintenance History
        │
        ▼
Feature Generation
        │
        ▼
ML Model
        │
        ▼
Failure Probability
        │
        ▼
Risk Assessment
        │
        ▼
Maintenance Recommendation
```

The initial domain implementation should focus on reliable data capture and retrieval.

Predictive models should be implemented as separate services or application components.

---

# 18. AI/ML Integration

The domain should support future AI/ML workloads without coupling the core domain to a specific AI provider.

Potential AI use cases include:

* Anomaly detection
* Failure prediction
* Root-cause analysis
* Maintenance recommendations
* Event classification
* Asset health prediction
* Natural language operational summaries

The architecture should support:

```text
ForgeMind
    │
    ▼
AI Provider Abstraction
    │
    ├── Local Model
    │
    ├── Self-Hosted Model
    │
    └── External AI API
```

The domain should provide structured data to AI pipelines.

AI processing should occur asynchronously where appropriate.

---

# 19. Security and RBAC

Industrial operational data may contain sensitive operational information.

Access should be controlled through the existing ForgeMind authentication and RBAC architecture.

Permissions should eventually distinguish between:

* Viewing events
* Creating events
* Updating events
* Resolving events
* Viewing telemetry
* Creating telemetry
* Managing telemetry

Access should respect the user's organisational scope where applicable.

For example:

```text
User
  │
  ▼
Organization
  │
  ▼
Plant
  │
  ▼
Area
  │
  ▼
Asset
  │
  ▼
Operational Data
```

The implementation should reuse existing authorization mechanisms instead of creating a parallel permission system.

---

# 20. Auditability

Important changes to operational events should be auditable.

Examples include:

* Event creation
* Event status changes
* Event resolution
* Severity changes
* Manual modifications

Telemetry data generated by automated systems may not require individual audit records for every measurement due to potentially high volume.

However, changes to telemetry configuration, metric definitions, and ingestion sources should be auditable.

The existing Audit domain should be reused where applicable.

---

# 21. Testing Strategy

The Industrial Event and Telemetry Domain should include automated tests at multiple levels.

### Model Tests

Test:

* Model creation
* Relationships
* Validation
* Constraints
* String representations
* Timestamps

### Service Tests

Test:

* Event processing
* Telemetry processing
* Health-related calculations
* Validation rules

### API Tests

Test:

* Authentication
* RBAC
* CRUD operations
* Filtering
* Search
* Ordering
* Pagination
* Time-range queries

### Integration Tests

Test:

```text
Asset
   │
   ├── Event
   │
   ├── Telemetry
   │
   └── Maintenance
```

Tests should verify that the new domain integrates correctly with existing Asset and Maintenance domains.

---

# 22. Future Evolution

The Industrial Event and Telemetry Domain is intended to evolve incrementally.

The expected roadmap is:

```text
Phase 1
Industrial Event and Telemetry Models
        │
        ▼
Phase 2
REST APIs
        │
        ▼
Phase 3
Operational Timeline
        │
        ▼
Phase 4
Asset Health Scoring
        │
        ▼
Phase 5
Predictive Maintenance
        │
        ▼
Phase 6
AI Inference Pipeline
        │
        ▼
Phase 7
Real-Time Industrial Intelligence
```

Future capabilities may include:

* IoT ingestion
* MQTT integration
* OPC-UA integration
* SCADA integration
* Real-time event streaming
* Kafka or RabbitMQ event pipelines
* Time-series databases
* Edge computing
* Real-time anomaly detection
* Digital twins
* Advanced predictive maintenance

These capabilities should be introduced only when justified by actual platform requirements.

---

# 23. Architectural Principles

The following principles should guide implementation:

### 1. Asset-Centric Design

All operational data should be associated with an industrial asset whenever possible.

### 2. Separation of Concerns

Raw events and telemetry should remain separate from health scoring, predictive maintenance, and AI logic.

### 3. Provider Independence

The domain should not depend on a specific IoT, telemetry, or AI provider.

### 4. API-First Architecture

Operational data should be accessible through versioned REST APIs.

### 5. Security by Default

All APIs should require authentication and enforce RBAC.

### 6. Auditability

Important operational changes should be traceable.

### 7. Scalability

The system should support migration from standard relational storage to specialised time-series infrastructure when required.

### 8. Asynchronous Processing

High-cost or long-running operations should use the existing background task infrastructure.

### 9. AI-Ready Data

Operational data should be structured and consistent enough to support future AI and ML workloads.

### 10. Incremental Evolution

The platform should start with a simple PostgreSQL-based implementation and evolve toward more advanced infrastructure as real operational requirements emerge.

---

# 24. Final Architecture

The target architecture for this phase is:

```text
┌─────────────────────────────────────────────┐
│              Industrial Assets              │
└──────────────────────┬──────────────────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
┌───────────────────┐     ┌───────────────────┐
│ Industrial Events │     │     Telemetry     │
└─────────┬─────────┘     └─────────┬─────────┘
          │                         │
          └────────────┬────────────┘
                       │
                       ▼
             ┌──────────────────┐
             │ Operational Data │
             └────────┬─────────┘
                      │
             ┌────────┴─────────┐
             │                  │
             ▼                  ▼
    ┌─────────────────┐  ┌───────────────┐
    │  Asset Health   │  │  Maintenance  │
    │    Scoring      │  │    Domain     │
    └────────┬────────┘  └───────┬───────┘
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
             ┌──────────────────┐
             │    Predictive    │
             │    Maintenance   │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │   AI Inference   │
             │     Pipeline     │
             └──────────────────┘
```

This architecture provides ForgeMind with a clear path from traditional industrial asset management toward intelligent, data-driven operations while keeping the initial implementation simple, maintainable, and extensible.
