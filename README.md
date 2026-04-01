# Telemetry JSON Converter

Python solution that converts two telemetry JSON telemetry formats into a single unified schema.

## Files Included
- `data-1.json` → Input format 1
- `data-2.json` → Input format 2
- `data-result.json` → Expected unified output
- `main.py` → Conversion logic + unit tests

## Problem Summary
The task converts two different telemetry payload structures into one normalized format:
- Standard device metadata
- UTC timestamp in **milliseconds since Unix epoch**
- Structured location object
- Nested telemetry data object

## How to Run
```bash
python main.py
```

## Expected Output
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.00s

OK
```

## Notes
- `convertFromFormat1()` parses the slash-delimited location string
- `convertFromFormat2()` converts ISO-8601 UTC timestamp into epoch milliseconds
- Unit tests validate both formats against the expected result
