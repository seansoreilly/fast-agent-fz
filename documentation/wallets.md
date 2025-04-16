# Wallets (Apple Pay & Google Pay)

This section covers integration with digital wallets like Apple Pay and Google Pay.

## Apple Pay `[WALLET:APPLE_PAY]`

_(Details specific to Apple Pay integration need to be extracted from the 'Apple Pay' sub-pages)_

### Onboarding

- **Process:** _(Summarize the steps described in 'Apple Pay Onboarding via Merchant Dashboard')_ Likely involves configuration within the Fat Zebra Merchant Dashboard and potentially certificate signing requests (CSRs).

### Certificate Renewal

- **Process:** _(Summarize steps from 'Apple Pay (app) Certificate Renewal')_ Explain how to renew expiring Apple Pay certificates.

### Get Apple Pay Session `[API_ENDPOINT:/apple_pay/session]`

- **Purpose:** An Apple Pay session must typically be requested from Fat Zebra before displaying the Apple Pay button on the web.
- **API Endpoint:** _(Confirm endpoint path, e.g., `POST /v1.0/apple_pay/sessions`)_.
- **Request Payload:** _(Detail required fields, e.g., validation URL provided by Apple)_.
- **Response Payload:** _(Detail the session object returned by Fat Zebra to be passed to Apple's SDK)_.

### Recurring & Installment Transactions

- **Process:** _(Explain how Apple Pay can be used for recurring/installment payments, likely involves tokenizing the Apple Pay payment data - see 'Recurring & Installment Transactions' page)_.

## Google Pay™ `[WALLET:GOOGLE_PAY]`

_(Details specific to Google Pay integration need to be extracted from the 'Google Pay' sub-pages)_

### Integration Methods

Fat Zebra supports multiple Google Pay integration methods:

- **Android App Integration:** _(Summarize key steps/considerations for integrating within a native Android app)_.
- **Web Integration:** _(Summarize key steps/considerations for web integration, likely involving Google's JS library and passing payment data to Fat Zebra)_.
- **Hosted Payments Page Integration:** _(Explain how Google Pay works with Fat Zebra's hosted payment page solution)_.

### Google Pay Merchant ID

- **Requirement:** _(Explain the need for a Google Pay Merchant ID and potentially how to obtain/configure it)_.

### Processing Google Pay Payments

- **Data Flow:** _(Describe how the encrypted payment data from Google Pay is passed to the Fat Zebra API (e.g., Purchases endpoint) for processing)_.
- **API Request:** _(Show an example snippet of a Fat Zebra API request containing Google Pay data)_.

---

_See also: [Purchases](./purchases.md), [Card On File](./card-on-file.md) (for tokenization), [SDKs](./sdk.md)_
