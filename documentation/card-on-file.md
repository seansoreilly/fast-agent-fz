# Card On File

This section covers storing card details securely (tokenization) and using these tokens for various payment types.

## Tokenized Credit Cards `[API_ENDPOINT:/tokens]`

*(Details on the tokenization process, API endpoint, request/response need to be extracted from the 'Tokenized Credit Cards' page)*

Tokenization replaces sensitive card details with a unique, non-sensitive identifier (token) that can be stored and used for future payments.

*   **Purpose:** Securely store customer card details for repeat purchases, subscriptions, etc., reducing PCI scope.
*   **Process:** (Describe how tokens are created - e.g., during a purchase, via a dedicated tokenization endpoint, using SDKs).
*   **API Endpoint:** (Specify the endpoint for creating/managing tokens, e.g., `POST /v1.0/tokens` or similar).
*   **Request Payload:** (Detail the fields required to create a token, likely including card details).
*   **Response Payload:** (Detail the response containing the generated token, e.g., `{"token": "tok_...", "card": {...}}`).

**Using Tokens:**

Once a token is created, use it in place of raw card details in subsequent API calls (e.g., Purchases). Reference the `token` within the `card` object:

```json
{
  // ... other purchase details like amount, reference ...
  "card": {
    "token": "tok_xxxxxxxxxxxxxxxx"
  }
}
```

## Recurring / Installment Payments `[API_RECURRING]`

*(Details on setting up and managing recurring/installment payments using tokens need to be extracted from the 'Recurring / Installment Payments' page)*

*   **Mechanism:** (Explain how recurring/installments are implemented - e.g., using tokens with specific flags, dedicated recurring payment endpoints, or a separate scheduling system).
*   **API Request:** (Show example API calls for initiating recurring payments, potentially including frequency, amount, start/end dates).
*   **Management:** (Describe any API endpoints for updating or cancelling recurring payments).

## Merchant Initiated Transaction (MIT)

*(Details on performing MITs using tokens need to be extracted from the 'Merchant Initiated Transaction' page)*

MITs are transactions initiated by the merchant without direct cardholder interaction (e.g., for subscriptions after initial setup).

*   **Requirements:** (Mention any prerequisites, like initial cardholder consent and a successfully authenticated transaction).
*   **API Usage:** (Show how to flag a transaction as MIT in the API request when using a token).

## Incremental Authorization

*(Details on incremental authorizations need to be extracted from the 'Incremental Authorization' page)*

Incremental authorizations allow increasing the amount of a previously authorized transaction (common in hospitality/rental industries).

*   **Process:** (Explain the workflow and API calls involved).
*   **Use Cases:** (Mention typical scenarios).

---
*See also: [Purchases](./purchases.md), [SDKs](./sdk.md), [Security](./security.md)* 