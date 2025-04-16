# Direct Entries (Direct Debits & Credits)

This section details how to perform Direct Debits (pulling funds from bank accounts) and Direct Credits (pushing funds to bank accounts) via the Fat Zebra API or batch uploads.

## Overview

_(High-level description of Direct Entries needs to be extracted from the 'Direct Entries > Overview' page)_

Direct Entries allow for bank-to-bank transfers, typically used for scenarios like subscription billing (debits) or payouts (credits) in supported regions (e.g., Australia - BECS).

## Direct Debits `[API_ENDPOINT:/direct_debits]`

_(Details on the Direct Debit API endpoint, request/response need to be extracted from the 'Direct Debits' page)_

- **Purpose:** To pull funds from a customer's bank account.
- **Prerequisites:** Requires customer authorization (e.g., a Direct Debit Request - DDR) and valid bank account details (BSB, Account Number).
- **API Endpoint:** (Specify the endpoint, e.g., `POST /v1.0/direct_debits` or similar).
- **Request Payload:** (Detail fields like amount, reference, customer name, BSB, account number, lodging reference).
  ```json
  {
    "amount": "(Integer - Amount in cents)",
    "reference": "(String - Payment Reference)",
    "bsb": "(String - BSB Number)",
    "account_number": "(String - Account Number)",
    "account_name": "(String - Account Holder Name)",
    "lodgement_reference": "(String - Reference on customer's statement)",
    "metadata": {
      // Optional
      "(key)": "(value)"
    }
  }
  ```
- **Response Payload:** (Detail the response indicating acceptance for processing, transaction ID, status).
- **Processing Time:** Note that Direct Debits are not instant and take time to clear/settle through the banking network. Status updates may occur via webhooks.

## Direct Credits `[API_ENDPOINT:/direct_credits]`

_(Details on the Direct Credit API endpoint, request/response need to be extracted from the 'Direct Credits' page)_

- **Purpose:** To push funds to a payee's bank account.
- **API Endpoint:** (Specify the endpoint, e.g., `POST /v1.0/direct_credits` or similar).
- **Request Payload:** (Detail fields, likely similar to Direct Debits: amount, reference, payee name, BSB, account number).
- **Response Payload:** (Detail the response indicating acceptance for processing).
- **Processing Time:** Similar to Direct Debits, credits are processed through the banking network and are not instant.

## Batch Processing

Direct Debits can also be processed in bulk via file upload. _(See [Batches](./batches.md#direct-debit-batch-file-columns))_.

---

_See also: [Batches](./batches.md), [Webhooks](./webhooks.md), [Glossary](./glossary.md)_
