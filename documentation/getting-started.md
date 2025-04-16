# Getting Started with the Fat Zebra API

This section covers the fundamental concepts for interacting with the Fat Zebra REST API.

**Core Concepts:**

- **RESTful Design:** The API follows REST principles, using predictable URLs and standard HTTP features.
- **HTTP Verbs:** Utilizes standard HTTP verbs (GET, POST, PUT, DELETE, etc.) for different actions.
- **JSON Payloads:** Expects request data in JSON format and returns responses in JSON. It's recommended to validate JSON structures using tools like [JSONLint](https://jsonlint.com/) during development.
  - **Caution:** Do not validate sensitive data like full card numbers or CVV/CVCs in external tools. Replace holder names with examples, but be mindful of special characters.
- **Compatibility:** Compatible with most standard HTTP clients (e.g., cURL, Python's `requests`, .NET's `HttpClient`).

## Authentication `[API_AUTH]`

_(Details on authentication methods (e.g., Basic Authentication, API Keys/Tokens) need to be extracted from the 'Authentication' sub-page)_

- **Method:** (e.g., HTTP Basic Auth)
- **Credentials:** (e.g., Username = API Key, Password = API Token)
- **Example:** (Provide an example using cURL or a common language)

## Endpoint Base URLs `[API_ENDPOINT]`

_(Specific base URLs need to be extracted from the 'Endpoint Base URLs' sub-page)_

- **Sandbox/Testing URL:** `(e.g., https://gateway.sandbox.fatzebra.com.au/v1.0)`
- **Production URL:** `(e.g., https://gateway.fatzebra.com.au/v1.0)`

## Errors & Timeouts `[API_ERROR]`

_(Details on specific HTTP status codes, error response structure, and timeout handling need to be extracted from the 'Errors & Timeouts' sub-page)_

- **Error Indication:** Uses standard HTTP response codes (4xx for client errors, 5xx for server errors).
- **Error Response Body:** (Describe the standard JSON structure of error responses, e.g., `{"errors": [{"message": "...", "code": "..."}]}`)
- **Common Codes:** (List a few key codes mentioned, e.g., 400 Bad Request, 401 Unauthorized, 403 Forbidden, 422 Unprocessable Entity)
- **Timeouts:** (Explain expected timeout behaviour or recommended client-side timeout settings).

---

_See also: [Purchases](./purchases.md), [API Response Codes](./purchases.md#response-codes)_
