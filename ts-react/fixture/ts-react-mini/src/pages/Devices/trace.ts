/**
 * Attaches the operator's trace id to the request headers. The service echoes
 * it on every response, so log lines and their request can be joined later.
 * The id is opaque to the dashboard, so it stays a plain string.
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
