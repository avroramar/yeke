# Architecture

```
main.py
    │
    ▼
inventory/
│
├── manager.py
├── models.py
├── validator.py
├── pricing.py
├── history.py
└── storage.py
         │
         ▼
reports/
├── exporter.py
├── summary.py
└── report.py
```

## Components

### Manager

Coordinates inventory operations.

### Models

Defines product data models.

### Validator

Validates product information.

### Pricing

Calculates inventory value and pricing statistics.

### History

Stores inventory activity.

### Storage

Loads and saves inventory data.

### Reports

Creates text summaries and exports reports.
