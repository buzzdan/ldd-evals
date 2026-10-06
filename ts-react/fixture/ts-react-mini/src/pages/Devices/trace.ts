/**
 * Attaches the operator's trace id to a request's headers.
 *
 * The id is echoed by the service on every response it produces for the
 * request, so a device's log lines and the request that produced them can be
 * joined later. It is opaque to the dashboard: nothing here parses or checks
 * it, so it stays a string.
 */
export function withTrace(
  headers: Record<string, string>,
  traceId: string
): Record<string, string> {
  if (!traceId) {
    return headers
  }
  return { ...headers, 'X-Trace': traceId }
}

/** Reads the trace id the operator put in the URL, if any. */
export function traceFromSearch(search: URLSearchParams): string {
  return search.get('trace') ?? ''
}
