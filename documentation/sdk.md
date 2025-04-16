# Fat Zebra SDKs

Fat Zebra provides Software Development Kits (SDKs) to simplify integration, especially for client-side implementations (web and mobile), helping to reduce PCI scope.

## React SDK `[SDK:REACT]`

_(Details need to be extracted from the 'React SDK - Overview' page and sub-pages)_

- **Overview:** _(Summarize the purpose and features of the React SDK)_. Likely provides React components for embedding payment forms, handling tokenization, and potentially 3DS flows.
- **Installation:** _(Provide package name and install command, e.g., `npm install @fatzebra/react`)_.
- **Usage:** _(Show basic usage examples for key components, e.g., embedding a card form, handling tokenization events)_.
- **Key Components/Props:** _(List important components and their configuration options)_.

## Javascript SDK `[SDK:JS]`

_(Details need to be extracted from the Javascript SDK pages: 'Obtain an OAuth token', 'Features', 'Methods', 'Objects', 'Events', 'Event Listeners')_

This SDK is designed for direct use in web pages (non-React specific) or potentially server-side Node.js environments.

### Features

_(List key features mentioned, e.g., Card form rendering, Tokenization, 3DS handling, Payment processing)_

### Setup / Authentication

- **Obtaining OAuth Token:** _(Explain the process described for getting an OAuth token if required for initialization)_.
- **Initialization:** _(Show JS code snippet for initializing the SDK, potentially including the OAuth token or API key)_.
  ```javascript
  // Example Initialization (Illustrative)
  const fz = new FatZebra({
    // Configuration options: apiKey, oauthToken, etc.
  });
  ```

### Key Methods

_(Describe important methods and their parameters/usage)_

- **`constructor`:** Initialization.
- **`purchase(params)`:** Initiates a purchase. _(Detail params, likely amount, currency, potentially card details or reference to hosted fields)_.
- **`verifyCard(params)`:** Verifies card details (e.g., for tokenization without a purchase). _(Detail params)_.
- **`renderPaymentsPage(params)`:** Renders Fat Zebra's hosted payment page. _(Detail params)_.
- _(Add other methods if documented)_.

### Data Objects

_(Describe key data structures used by the SDK)_

- **`Customer`:** Customer details.
- **`PaymentIntent`:** Represents a payment intention.
- **`PaymentMethod`:** Represents a payment method (e.g., tokenized card).
- **`HppSetupParams`:** Parameters for the hosted payments page.
- **`VerifyCardParams`:** Parameters for card verification.

### Events & Listeners

_(Describe how to listen for events emitted by the SDK)_

The SDK likely emits events for various stages:

- **`Form Validation (V2)`:** Form field validation status.
- **`Validation`:** General validation events.
- **`SCA`:** Events related to Strong Customer Authentication (3DS).
- **`Tokenization`:** Card tokenization success/failure.
- **`Payment`:** Payment processing results.

**Example Listener (Illustrative):**

```javascript
fz.on("tokenization.success", (payload) => {
  console.log("Token received:", payload.token);
  // Send token to your server
});

fz.on("payment.failed", (error) => {
  console.error("Payment failed:", error.message);
  // Display error to user
});
```

---

_See also: [Getting Started](./getting-started.md), [Purchases](./purchases.md), [Card On File](./card-on-file.md), [Security](./security.md), [3DS2 Integration](./3ds2.md)_
