# Purchases API

This section details how to create card payments (purchases) using the Fat Zebra API.

## Overview

_(High-level description of the purchase process needs to be extracted from the 'Purchases > Overview' page)_

The Purchases API endpoint allows you to charge a credit or debit card.

## API Endpoint `[API_ENDPOINT:/purchases]`

_(Confirm endpoint path and details from documentation)_

- **Method:** `POST`
- **Path:** `/v1.0/purchases`

## Request Payload `[API_EXAMPLE]`

_(Specific required and optional fields, and their data types/formats need to be extracted from the documentation)_

```json
{
  "card_holder": "(String - Cardholder Name)",
  "card_number": "(String - Card PAN)",
  "card_expiry": "(String - MM/YYYY)",
  "cvv": "(String - CVV/CVC)",
  "amount": "(Integer - Amount in cents)",
  "currency": "(String - ISO Currency Code, e.g., AUD)",
  "reference": "(String - Your unique reference)",
  "customer_ip": "(String - Customer's IP address)",
  "metadata": {
    // Optional
    "(key)": "(value)",
    "(key)": "(value)"
  },
  "card": {
    // Alternative to providing raw card details if using token
    "token": "(Card Token - See [Card On File](./card-on-file.md))"
  }
  // Add other fields like address (for AVS), 3DS details, etc. as specified
}
```

## Response Payload `[API_EXAMPLE]`

_(Specific response fields need to be extracted)_

```json
{
  "successful": true, // Or false
  "authorized": true, // Or false
  "captured": true, // Or false
  "id": "(String - Transaction ID)",
  "amount": 1000,
  "currency": "AUD",
  "reference": "YourReference123",
  "message": "(String - e.g., Approved, Declined)",
  "response_code": "(String - Specific FZ code, e.g., 00)",
  "transaction_time": "(Timestamp)",
  "card": {
    "holder": "Cardholder Name",
    "number": "411111...1111", // Masked number
    "scheme": "(e.g., Visa, Mastercard)",
    "token": "(Card Token if generated/used)",
    "expiry_month": 12,
    "expiry_year": 2029
  },
  "avs_result": "(AVS Result Code - See AVS section below)",
  "cvv_result": "(CVV Result Code)"
  // Add other fields like 3DS results, settlement details etc. as specified
}
```

## Response Codes `[API_RESPONSE_CODE]`

_(Specific Fat Zebra response codes and their meanings need to be extracted from the 'Response Codes' sub-page)_

Fat Zebra uses specific codes in the `response_code` field to indicate the outcome.

- `00`: Approved
- `05`: Declined (Generic)
- `51`: Insufficient Funds
- _(List other common codes)_

Refer to [Getting Started](./getting-started.md#errors--timeouts) for general HTTP status codes.

## Metadata

_(Explanation of how to use the `metadata` field needs to be extracted)_

You can include custom key-value pairs in the `metadata` object within the request. This data is stored with the transaction and returned in the response and webhooks.

## Addendum Data

_(Explanation of Addendum Data needs to be extracted)_

## Extra and Extended Fields

_(Details on fields for specific use cases need to be extracted from sub-pages)_

- **Card On File:** Using tokens. _(See [Card On File](./card-on-file.md))_.
- **3D Secure Card Payments:** Fields related to 3DS authentication. _(See [3DS2 Integration](./3ds2.md))_.
- **Mail Order / Telephone Order (MOTO):** Specific flags or fields for MOTO transactions.
- **Dynamic Descriptors:** How to set custom statement descriptors.
- **Payment Aggregators:** Fields relevant for aggregators.
- **Remittance Merchants:** Fields relevant for remittance.

## Chargebacks and Fraud

_(Summary of information on chargebacks and fraud prevention needs to be extracted)_

## Supported Currencies `[DATA:CURRENCY]`

_(List or link to the supported currencies needs to be extracted from the 'Supported Currencies' page)_

Common examples: AUD, USD, GBP, EUR, NZD. Refer to the documentation for the full list and ISO codes.

## AVS (Address Verification System)

_(Details on AVS fields in request and `avs_result` in response need to be extracted from the 'AVS' page)_

Provide address details in the request (e.g., `address_line1`, `address_postcode`) to perform AVS checks. The result is returned in the `avs_result` field of the response.

## Merchant Advice Codes (Retries)

_(Explanation of MACs and how they appear in responses needs to be extracted from the 'Merchant Advice Codes (Retries)' page)_

---

_See also: [Getting Started](./getting-started.md), [Testing](./testing.md), [Card On File](./card-on-file.md), [3DS2 Integration](./3ds2.md)_
