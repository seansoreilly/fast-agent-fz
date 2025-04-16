# API Pagination `[API_PAGINATION]`

This section describes how pagination is handled for API endpoints that return lists of resources (e.g., lists of transactions, customers).

## Requesting Pages

_(Specific query parameters used for pagination need to be extracted from the 'Pagination' page)_

- **Page Parameter:** `(e.g., page=2)` - Specifies the page number to retrieve (usually 1-indexed).
- **Size/Limit Parameter:** `(e.g., per_page=50)` - Specifies the number of items to return per page.

**Example Request:**

```
GET /v1.0/purchases?page=3&per_page=20
Host: gateway.fatzebra.com.au
Authorization: Basic ...
Accept: application/json
```

## Reading Pagination Info from Responses

_(Specific response headers or fields indicating pagination status need to be extracted from the 'Pagination' page)_

Responses for paginated endpoints typically include information to navigate through the result set.

- **Total Count:** May be provided in a header `(e.g., X-Total-Count)` or within the JSON body `(e.g., "pagination": {"total_entries": 123})`.
- **Total Pages:** May be provided in a header `(e.g., X-Total-Pages)` or within the JSON body `(e.g., "pagination": {"total_pages": 7})`.
- **Current Page:** Often indicated in the JSON body `(e.g., "pagination": {"current_page": 3})`.
- **Next/Previous Links:** Some APIs provide direct URLs for the next and previous pages in `Link` headers or within the JSON body.

**Example Response Snippet (Illustrative):**

```json
{
  "purchases": [
    {...},
    {...}
  ],
  "pagination": {
    "total_entries": 123,
    "total_pages": 7,
    "current_page": 3,
    "per_page": 20
  }
}
```

---

_See also: [Getting Started](./getting-started.md)_
