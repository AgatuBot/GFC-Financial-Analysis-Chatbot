# Scope and Rules of Engagement

This assessment is authorized against the author's own GFC Financial Analysis Chatbot.

## Target
- Application: GFC Financial Analysis Chatbot
- Environment: Render deployment
- Tester platforms: Kali Linux / Parrot OS
- Proxy: Burp Suite

## Permitted
Passive browsing, tester-generated HTTP interception, individual request replay, controlled parameter modification, low-volume validation tests, session checks, security-header review and controlled injection testing.

## Prohibited
Denial-of-service, high-volume attacks, unrelated systems, credential theft, persistence, malware deployment, destructive actions and attempts to compromise Render infrastructure.

## Evidence
Never commit API keys, Flask secrets, active cookies, authentication tokens or personal information. Sanitize screenshots and HTTP examples.

## Stop conditions
Stop if the application becomes unstable, unexpected third-party data appears, infrastructure outside the application is affected, or a test could cause destructive or irreversible changes.