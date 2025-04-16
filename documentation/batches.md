# Batches `[BATCH_FORMAT]`

This section describes the process for submitting transactions in bulk using batch file uploads.

## Overview

_(High-level description of batch processing needs to be extracted from the 'Batches > Overview' page)_

Batch processing allows merchants to submit multiple transactions (Purchases, Refunds, Direct Debits) simultaneously by uploading a formatted file, typically in CSV format. This is useful for high-volume processing.

## Uploading Batches

_(Details on how batches are uploaded (e.g., via Merchant Dashboard, SFTP, API endpoint) need to be extracted)_

- **Method:** (e.g., Manual upload via Merchant Dashboard -> Direct Entries -> Upload Batch Files)
- **Format:** Typically CSV, adhering to the specific column requirements below.

## File Formats

Files must contain specific columns in the correct order. Header rows may or may not be required (clarify from docs).

### Purchase Batch File Columns

_(Specific columns, order, data types, and mandatory/optional status need to be extracted from the 'Purchase Batch File Columns' page)_

- `Column 1 Name (e.g., amount)`: Description (e.g., Amount in cents)
- `Column 2 Name (e.g., reference)`: Description
- `Column 3 Name (e.g., card_number)`: Description
- `Column 4 Name (e.g., card_holder)`: Description
- `Column 5 Name (e.g., card_expiry_month)`: Description
- `Column 6 Name (e.g., card_expiry_year)`: Description
- `Column 7 Name (e.g., cvv)`: Description
- _(Add all required/optional columns)_

### Refund Batch File Columns

_(Specific columns, order, data types, and mandatory/optional status need to be extracted from the 'Refund Batch File Columns' page)_

- `Column 1 Name (e.g., original_transaction_id)`: Description (e.g., The ID of the purchase to refund)
- `Column 2 Name (e.g., amount)`: Description (e.g., Amount in cents, optional - defaults to full amount if omitted)
- `Column 3 Name (e.g., reference)`: Description
- _(Add all required/optional columns)_

### Direct Debit Batch File Columns

_(Specific columns, order, data types, and mandatory/optional status need to be extracted from the 'Direct Debit Batch File Columns' page)_

- `Column 1 Name (e.g., amount)`: Description (e.g., Amount in cents)
- `Column 2 Name (e.g., reference)`: Description
- `Column 3 Name (e.g., bsb)`: Description
- `Column 4 Name (e.g., account_number)`: Description
- `Column 5 Name (e.g., account_name)`: Description
- `Column 6 Name (e.g., lodgement_reference)`: Description
- _(Add all required/optional columns)_

## Result Files

_(Details on how results are provided (e.g., downloaded from Dashboard, emailed, webhook notification) and the format of result files need to be extracted from the 'Result Files' page)_

After a batch file is processed, a result file is typically generated indicating the success or failure of each transaction within the batch.

- **Retrieval:** (How to get the result file).
- **Format:** (Describe the columns and content of the result file, e.g., original reference, transaction ID, status, message).

---

_See also: [Purchases](./purchases.md), [Direct Entries](./direct-entries.md), [Merchant Dashboard](./merchant-dashboard.md)_
