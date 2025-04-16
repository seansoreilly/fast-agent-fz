# Network Token Passthrough

This section explains the "Bring Your Own Network Token" (BYONT) feature.

## Overview

_(Details on the purpose and functionality of network token passthrough need to be extracted from the 'Bring Your Own Network Token' page)_

Network Token Passthrough allows merchants who obtain network tokens (e.g., Visa VTS, Mastercard MDES) directly or via a third-party provider to pass these tokens to Fat Zebra for processing, instead of using Fat Zebra's tokenization or raw PANs.

## Benefits

- Potential for higher authorization rates.
- Reduced risk associated with storing PAN data.
- Consistency if using multiple PSPs with the same network tokens.

## API Integration

_(Details on how to pass network tokens via the API need to be extracted)_

When making an API request (e.g., [Purchases](./purchases.md)), instead of providing raw card details or a Fat Zebra token, you would provide the network token and related information.

**Example Request Snippet (Illustrative - confirm actual fields):**

```json
{
  // ... other purchase details like amount, reference ...
  "network_token": {
    "token": "(The network token value)",
    "cryptogram": "(The transaction cryptogram)",
    "eci_indicator": "(The E-commerce Indicator)",
    "expiry_month": "(Token expiry month MM)",
    "expiry_year": "(Token expiry year YYYY)",
    "source": "(e.g., visa, mastercard)" // Indicate the network source
  }
}
```

## Considerations

- **Enrollment:** You must be enrolled with the card networks (Visa, Mastercard) for network tokenization.
- **Cryptograms:** Generating transaction-specific cryptograms is required.
- **Token Lifecycle Management:** Managing the lifecycle (e.g., updates, expiry) of the network tokens is your responsibility.

---

_See also: [Purchases](./purchases.md), [Card On File](./card-on-file.md), [Security](./security.md)_
