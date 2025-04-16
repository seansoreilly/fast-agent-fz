# Webhooks `[WEBHOOKS]`

This section describes how to use webhooks to receive real-time notifications about events happening in your Fat Zebra account.

## Overview

_(High-level description of webhooks and their benefits needs to be extracted from the 'Webhooks > Overview' page)_

Webhooks allow Fat Zebra to send automated messages (HTTP POST requests) to your application's endpoint when specific events occur (e.g., a purchase succeeds, a direct debit fails, a card is updated). This avoids the need for constant polling of the API.

## Handling Webhooks

_(Details on setting up endpoints, validation, and responding need to be extracted from the 'Handling Webhooks' page)_

1.  **Create an Endpoint:** You need to create a publicly accessible HTTPS endpoint (URL) in your application that can receive POST requests with JSON payloads.
2.  **Configure in Dashboard:** Register your endpoint URL within the Fat Zebra Merchant Dashboard (provide path/location if known).
3.  **Receive Events:** Your endpoint will receive POST requests containing JSON data for subscribed events.
4.  **Validate Requests (Recommended):**
    - _(Describe validation mechanism if available, e.g., checking a signature header using a shared secret)_
    - **Signature Header:** `(e.g., X-FZ-Signature)`
    - **Secret:** _(Where to find the webhook secret in the dashboard)_
    - **Validation Logic:** _(Pseudo-code or example of how to compute and compare the signature)_
5.  **Respond Quickly:** Your endpoint should acknowledge receipt of the webhook immediately with an HTTP `200 OK` status code before performing any complex business logic. Processing should happen asynchronously to avoid timeouts.
6.  **Handle Failures/Retries:** _(Explain Fat Zebra's retry policy if a webhook delivery fails, e.g., endpoint returns non-200 status)_

## Events `[WEBHOOK_EVENT]`

_(List of available event types and example payloads need to be extracted from the 'Events' page and sub-pages)_

Fat Zebra sends webhooks for various events. You can typically select which events you want to subscribe to in the dashboard.

**Common Event Types:**

- `purchase.succeeded`: A card purchase was successfully authorized/captured.
- `purchase.failed`: A card purchase failed.
- `refund.succeeded`: A refund was processed successfully.
- `refund.failed`: A refund attempt failed.
- `direct_debit.cleared`: A direct debit has cleared.
- `direct_debit.failed`: A direct debit failed (e.g., insufficient funds, invalid account).
- `card.updated`: A tokenized card's details were updated (e.g., expiry).
- _(List other relevant event types, e.g., dispute events, subscription events)_

**Example Payload (`purchase.succeeded` - Illustrative):**

_(Example JSON payload needs to be extracted from 'Example Webhooks' page)_

```json
{
  "event": "purchase.succeeded",
  "payload": {
    "successful": true,
    "authorized": true,
    "captured": true,
    "id": "txn_xxxxxxxxxxxx",
    "amount": 1000,
    "currency": "AUD",
    "reference": "YourReference123",
    "message": "Approved",
    "response_code": "00",
    "transaction_time": "...",
    "card": {
      "holder": "...",
      "number": "411111...1111",
      "scheme": "Visa",
      "token": "tok_...",
      "expiry_month": 12,
      "expiry_year": 2029
    },
    "metadata": {
      "order_id": "SO-987"
    }
    // ... other relevant fields ...
  },
  "webhook_id": "wh_...",
  "timestamp": "..."
}
```

---

_See also: [Getting Started](./getting-started.md), [Purchases](./purchases.md), [Direct Entries](./direct-entries.md)_
