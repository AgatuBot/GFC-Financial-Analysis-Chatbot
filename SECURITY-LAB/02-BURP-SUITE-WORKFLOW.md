# Burp Suite Workflow

## Lab topology
Browser on Kali/Parrot -> Burp Suite -> Internet -> GFC chatbot on Render.

## Proxy setup
1. Start Burp Suite.
2. Confirm the local proxy listener.
3. Configure the test browser to use Burp.
4. Open the GFC chatbot.
5. Confirm the request appears in HTTP history.

## Attack-surface mapping
Record observable routes, methods, parameters, content types, response codes and session behavior.

## Capture the chatbot request
Send a normal question through the UI and capture the request to /chat. Save a sanitized copy with cookies and secrets removed.

## Controlled request modification
Change one input at a time: empty input, missing JSON field, unexpected field, null value, wrong data type, controlled long input, Unicode/special characters, unsupported company, unsupported year and unsupported metric.

## Session analysis
Inspect session behavior and cookie attributes. Never publish live session cookies.

## Security headers
Review Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, Strict-Transport-Security, Permissions-Policy and frame protection.

## Evidence
For each finding capture the request, modified input, response, expected behavior, actual behavior, impact, reproduction steps, fix and retest result.