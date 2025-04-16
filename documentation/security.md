# Security

This section covers security aspects related to integrating with Fat Zebra, particularly PCI DSS compliance.

## Overview

_(General security best practices mentioned in the 'Security > Overview' page should be summarized here)_

Fat Zebra prioritizes security. Integrators should also follow best practices to protect sensitive data.

## PCI Certification & Compliance

_(Details about Fat Zebra's PCI status and integrator responsibilities need to be extracted from 'PCI Certification' and 'What is PCI Compliance' pages)_

- **Fat Zebra's Status:** Fat Zebra is a PCI DSS Level 1 Service Provider. _(Confirm level)_
- **What is PCI DSS:** The Payment Card Industry Data Security Standard (PCI DSS) is a set of security standards designed to ensure that all companies that accept, process, store or transmit credit card information maintain a secure environment.
- **Your Responsibility:** Your PCI DSS compliance requirements depend heavily on your integration method.
  _ **Using Hosted Solutions/SDKs:** Integrations using Fat Zebra's hosted payment pages, JavaScript SDK, or Mobile SDKs significantly reduce your PCI scope, as sensitive cardholder data (PAN, CVV) is typically sent directly from the cardholder's browser/device to Fat Zebra, bypassing your servers.
  You may only need to complete a Self-Assessment Questionnaire (SAQ) A or SAQ A-EP.
  _ **Direct API Integration (Handling PAN):** If your servers directly receive or transmit raw card numbers (PAN), your PCI compliance scope is much larger, likely requiring SAQ D. \* **Tokenization:** Using Fat Zebra's tokenization ([Card On File](./card-on-file.md)) is crucial for reducing scope if you need to store payment details for recurring billing or repeat customers.
- **Recommendation:** Always aim to minimize your PCI scope by avoiding direct handling of sensitive card data whenever possible. Utilize Fat Zebra's tokenization, hosted fields, or SDKs.

## PGP Key

_(Information about Fat Zebra's PGP key and its usage needs to be extracted from the 'PGP Key' page)_

- **Purpose:** Fat Zebra may provide a PGP public key for securely encrypting sensitive information sent via less secure channels (e.g., certain batch files, specific support communications).
- **Key Availability:** _(Where to find the key - e.g., link on the page, downloadable file)_
- **Usage:** _(How to use the key for encrypting data)_

---

_See also: [Getting Started](./getting-started.md), [Card On File](./card-on-file.md), [SDKs](./sdk.md)_
