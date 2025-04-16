# Persisted Invoices

This section describes the specification for uploading persisted invoices to Fat Zebra.

## Overview

_(Purpose and use case for persisted invoices need to be extracted)_

Persisted invoices allow merchants to upload invoice data to Fat Zebra, potentially for linking with transactions or for presentment purposes.

## Upload Specification

_(Details on the upload method (API, SFTP, Dashboard?) and the required data format/schema need to be extracted from the 'Upload Specification' page)_

- **Upload Method:** (Specify how invoices are uploaded).
- **Data Format:** (Specify the format, e.g., JSON, XML, CSV).
- **Required Fields:** (List the mandatory fields for an invoice record, e.g., `invoice_id`, `customer_id`, `amount`, `due_date`, `line_items`).
- **Optional Fields:** (List optional fields).
- **Schema/Example:** (Provide a JSON/XML schema or a clear example of the expected data structure).

```json
// Example Invoice Data (Illustrative - confirm actual structure)
{
  "invoice_id": "INV-12345",
  "customer_reference": "CUST-001",
  "amount": 5500, // In cents
  "currency": "AUD",
  "issue_date": "2023-10-27",
  "due_date": "2023-11-10",
  "line_items": [
    {
      "description": "Widget A",
      "quantity": 2,
      "unit_price": 2000,
      "total": 4000
    },
    {
      "description": "Service Fee",
      "quantity": 1,
      "unit_price": 1500,
      "total": 1500
    }
  ],
  "metadata": {
    "order_id": "SO-987"
  }
}
```

## Linking to Transactions

_(Explain how uploaded invoices might be linked or referenced during payment processing, if applicable)_

---

_See also: (Link to relevant sections like Purchases or Metadata if applicable)_
