# Testing `[TEST_DATA]`

This section provides resources for testing your Fat Zebra integration, primarily focusing on test card numbers for simulating various transaction scenarios.

## Test Card Numbers

_(Specific test card numbers and their expected outcomes need to be extracted from the 'Test Card Numbers' page)_

Use the following card numbers in the **Sandbox Environment** (`[API_ENDPOINT]`) to simulate different responses.

**Successful Transactions:**

- Visa: `(Number needed)`
- Mastercard: `(Number needed)`
- AMEX: `(Number needed)`
- _(Add other card types if listed)_

**Declined Transactions:**

- Generic Decline: `(Number needed)`
- Insufficient Funds: `(Number needed)`
- Expired Card: `(Number needed)`
- Invalid CVV: `(Number needed)`
- _(Add other decline scenarios if listed)_

**3D Secure Simulation:**

- _(Details on simulating 3DS success, failure, or challenges need to be extracted - See also: [3DS2 Integration](./3ds2.md#3ds-cards-for-testing))_
  - Card requiring challenge: `(Number needed)`
  - Card resulting in frictionless success: `(Number needed)`
  - Card resulting in failure: `(Number needed)`

**AVS Simulation:**

- _(Details on simulating AVS matches/mismatches need to be extracted - See also: [Purchases](./purchases.md#avs))_
  - Card with AVS mismatch: `(Number needed)`
  - Card with AVS match: `(Number needed)`

**Other Scenarios:**

- _(Add any other specific test cards mentioned, e.g., for specific currencies, card-on-file tests)_

**General Test Card Parameters:**

- **Expiry Date:** Use any valid future date (e.g., MM/YY like 12/29).
- **CVV:** Use any valid CVV (e.g., 123 for Visa/Mastercard, 1234 for AMEX), unless testing an invalid CVV scenario.

## Sandbox Environment Notes

- The Sandbox environment mirrors production functionality but uses test credentials and does not process real payments.
- Refer to [Getting Started](./getting-started.md#endpoint-base-urls) for the Sandbox Base URL.
- Refer to [Getting Started](./getting-started.md#authentication) for obtaining Sandbox API credentials.

---

_See also: [Getting Started](./getting-started.md), [Purchases](./purchases.md), [3DS2 Integration](./3ds2.md)_
