# Architecture and product trade-offs

## Day 1 decisions

### Python backend and Django as the primary return-to-work track

This track reuses genuine prior software engineering, research and Django experience. It provides a clearer route to current evidence than positioning immediately as a Databricks specialist without recent commercial platform experience.

### Companion tool rather than official comparison engine

Version 1 explains bill inputs and creates a comparison-readiness checklist. It links users to official tools and avoids claims of official status, completeness or guaranteed savings.

### Manual input before bill parsing

Manual input keeps the first version testable and avoids collecting bill PDFs, NMIs and retailer-specific sensitive data. OCR and document parsing would expand privacy, accuracy and support risks before the calculation core is proved.

### Single-rate electricity in Victoria first

A narrow tariff and geography make calculations and caveats understandable. Time-of-use, controlled load, demand tariffs, gas and broader jurisdictions remain explicit non-goals.

### SQLite during the first learning slice

SQLite keeps Day 1 reproducible. PostgreSQL becomes the development database on Day 10, when database configuration and containers are the explicit learning goal.

