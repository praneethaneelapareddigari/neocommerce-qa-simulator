# Chaos Workflows

- **Timeouts**: enable `chaos_timeout=true` and set `chaos_delay_ms` in Postman environment.
- **Throttling**: set `chaos_throttle=true` to branch into a 429 test.
- **Forced 5xx**: enable `chaos_force_5xx=true` and assert resiliency of refund flow.
